import typing
from typing import Any, Dict

from .api import ApiClient, ApiMethod
from .exceptions import NotFound
from .page import Page
from .paginator import Paginator
from .utils import prepare_dict


class BaseManager:
    """Class for description API object"""

    object_name = None

    def __init__(self, api_client: ApiClient):
        self._api_client = api_client

    async def _get_result(
        self,
        api_method: ApiMethod,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        json: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Dict[str, typing.Any]:
        params = prepare_dict(params)

        if api_method == ApiMethod.LIST:
            params["per-page"] = json.pop("count", 100)

        json = prepare_dict(json)
        url = self._api_client.get_url_for_method(self.object_name, api_method.value)
        return await self._api_client.request(url, json=json, params=params)

    async def _list(
        self,
        page: int,
        count: int = 100,
        params: typing.Dict[str, typing.Any] | None = None,
        **kwargs,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get objects list from api
        :param page: number of page
        :param count: count items on page
        :param params: url dict_ for filtering
        :param kwargs: additional filters
        :return: objects list
        """
        payload = {
            "page": page,
            **kwargs,
            "count": count,
        }
        return await self._get_result(
            params=params,
            json=payload,
            api_method=ApiMethod.LIST,
        )

    async def _get(
        self,
        id_: int,
        params: typing.Dict[str, typing.Any] | None = None,
        **kwargs,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get one object from api
        :param id_: object id
        :param params: additional entity ids
        :return: object
        """
        result = await self._get_result(
            params=params,
            json={"id": id_},
            api_method=ApiMethod.LIST,
        )
        if result["count"] == 0:
            raise NotFound(message=f"{self.object_name} not found")
        return result["items"][0]

    async def _create(
        self,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create object in api
        :param kwargs: fields
        :return: created object
        """
        result = await self._get_result(
            api_method=ApiMethod.CREATE,
            params=params,
            json=kwargs,
        )
        return result["model"]

    async def _update(
        self,
        id_: int,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update object in api
        :param id_: object id
        :param kwargs: fields
        :return: updated object
        """
        result = await self._get_result(
            api_method=ApiMethod.UPDATE,
            params={"id": id_} if params is None else {**params, "id": id_},
            json=kwargs,
        )
        return result["model"]

    async def _save(
        self,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs,
    ) -> typing.Dict[str, typing.Any]:
        if "id" in kwargs:
            return await self._update(kwargs.pop("id"), params=params, **kwargs)
        else:
            return await self._create(params=params, **kwargs)


T = typing.TypeVar("T")


class EntityManager(BaseManager, typing.Generic[T]):
    def __init__(self, api_client: ApiClient, entity_class: typing.Type[T], **kwargs):
        super(EntityManager, self).__init__(api_client=api_client)
        self._entity_class = entity_class

    async def list(
        self, page: int = 0, count: int = 100, *args, **kwargs
    ) -> typing.List[T]:
        raw_data = await self._list(page, count, **kwargs)
        return self._result_to_entities(raw_data)

    async def get(
        self,
        id_: int,
        **kwargs,
    ) -> T:
        raw_data = await self._get(id_, **kwargs)
        return self._result_to_entity(raw_data)

    async def save(
        self,
        model: T,
        **url_params: Any,
    ) -> T:
        """
        Create or update an entity. Accepts either legacy AlfaEntity, Pydantic v2 model,
        or plain dict-like. Extra kwargs are passed as URL params (e.g., customer_id).
        """
        payload: Dict[str, Any]
        if hasattr(model, "serialize") and callable(getattr(model, "serialize")):
            payload = typing.cast(Dict[str, Any], model.serialize())
        elif hasattr(model, "model_dump"):
            payload = typing.cast(
                Dict[str, Any],
                model.model_dump(by_alias=True, exclude_none=True, mode="json"),
            )
        elif isinstance(model, dict):
            payload = typing.cast(Dict[str, Any], model)
        else:
            try:
                payload = dict(model)
            except Exception:
                raise TypeError("Unsupported model type for save")

        raw_data = await self._save(params=url_params or None, **payload)
        return self._result_to_entity(raw_data)

    async def page(
        self,
        page: int = 0,
        count: int = 100,
        **kwargs,
    ) -> Page[T]:
        raw_data = await self._list(page, count, **kwargs)
        items = self._result_to_entities(raw_data)
        return Page(
            number=page,
            items=items,
            total=raw_data["total"],
        )

    def paginator(
        self,
        start_page: int = 0,
        page_size: int = 100,
        **kwargs,
    ) -> Paginator[T]:
        return Paginator(
            alfa_object=self,
            start_page=start_page,
            page_size=page_size,
            filters=kwargs,
        )

    def _result_to_entities(
        self, result: typing.Dict[str, typing.Any]
    ) -> typing.List[T]:
        items = result["items"]
        return [self._result_to_entity(item) for item in items]

    def _result_to_entity(self, result: typing.Dict[str, typing.Any]) -> T:
        cls = self._entity_class
        model_validate = getattr(cls, "model_validate", None)
        if callable(model_validate):
            return typing.cast(T, model_validate(result))
        return typing.cast(T, cls(**result))
