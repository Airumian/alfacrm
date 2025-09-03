from __future__ import annotations

import datetime as _dt
from typing import Any

from pydantic import BaseModel, ConfigDict
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


def _parse_date(value: Any) -> _dt.date | None:
    if value is None or value == "":
        return None
    if isinstance(value, _dt.date) and not isinstance(value, _dt.datetime):
        return value
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, str):
        # Support ISO (YYYY-MM-DD) and DD.MM.YYYY
        for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
            try:
                return _dt.datetime.strptime(value, fmt).date()
            except Exception:
                pass
    return value  # let Pydantic raise if incompatible


def _parse_datetime(value: Any) -> _dt.datetime | None:
    if value is None or value == "":
        return None
    if isinstance(value, _dt.datetime):
        return value
    if isinstance(value, str):
        # Accept ISO forms with 'T' or space
        # Try explicit formats first, then fall back to fromisoformat
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
            try:
                return _dt.datetime.strptime(value, fmt)
            except Exception:
                pass
        try:
            # Python accepts both 'T' and space in fromisoformat
            return _dt.datetime.fromisoformat(value)
        except Exception:
            pass
    return value  # let Pydantic raise if incompatible


def _parse_time(value: Any) -> _dt.time | None:
    if value is None or value == "":
        return None
    if isinstance(value, _dt.time):
        return value
    if isinstance(value, _dt.datetime):
        return value.time()
    if isinstance(value, str):
        for fmt in ("%H:%M:%S", "%H:%M"):
            try:
                return _dt.datetime.strptime(value, fmt).time()
            except Exception:
                pass
        try:
            return _dt.time.fromisoformat(value)
        except Exception:
            pass
    return value  # let Pydantic raise if incompatible


# Reusable annotated types that parse AlfaCRM formats
AlfaDate = Annotated[_dt.date | None, BeforeValidator(_parse_date)]
AlfaDateTime = Annotated[_dt.datetime | None, BeforeValidator(_parse_datetime)]
AlfaTime = Annotated[_dt.time | None, BeforeValidator(_parse_time)]


def _parse_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except Exception:
        return value


def _parse_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except Exception:
        return value


def _parse_bool(value: Any) -> bool | None:
    if value is None:
        return None
    return bool(value)


def _parse_dict(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    if isinstance(value, dict):
        return value
    if isinstance(value, list):
        return {}
    if isinstance(value, str):
        s = value.strip()
        if s == "":
            return {}
        try:
            import json

            parsed = json.loads(s)
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return value


AlfaInt = Annotated[int | None, BeforeValidator(_parse_int)]
AlfaFloat = Annotated[float | None, BeforeValidator(_parse_float)]
AlfaBool = Annotated[bool | None, BeforeValidator(_parse_bool)]
AlfaDict = Annotated[dict[str, Any] | None, BeforeValidator(_parse_dict)]


class AlfaModel(BaseModel):
    """Shared base for AlfaCRM Pydantic models.

    - Allows extra fields (API often returns more keys)
    - Uses aliases for API field names
    - Provides serialize() producing JSON-ready payload (strings for dates)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        validate_assignment=False,
        arbitrary_types_allowed=True,
        str_strip_whitespace=False,
    )

    def serialize(self) -> dict[str, Any]:
        # mode='json' ensures JSON-compatible types (e.g., datetime -> ISO strings)
        return self.model_dump(by_alias=True, exclude_none=True, mode="json")

    def __str__(self) -> str:
        return str(self.serialize())

    def __repr__(self) -> str:
        return str(self.serialize())
