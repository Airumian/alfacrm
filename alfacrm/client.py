import aiohttp

from . import entities, managers
from .core.api import ApiClient
from .core.auth import AuthManager
from .core.exceptions import Forbidden
from .core.utils import parse_hostname


class AlfaClient:
    """Class for work with AlfaCRM API"""

    def __init__(
        self,
        hostname: str,
        email: str,
        api_key: str,
        branch_id: int,
        connections_limit: int | None = None,
        session: aiohttp.ClientSession | None = None,
    ):
        self._connector_class: type[aiohttp.TCPConnector] = aiohttp.TCPConnector

        if session is None:
            session = self._create_session()

        self._hostname = parse_hostname(hostname)
        self._branch_id = branch_id
        self._session = session
        self._email = email
        self._api_key = api_key
        self.auth_manager = AuthManager(
            email,
            api_key,
            hostname,
            session,
        )

        self.api_client = ApiClient(
            self._hostname,
            self._branch_id,
            self.auth_manager,
            self._session,
        )

        # Set API objects
        self.branch = managers.Branch(self.api_client, entities.Branch)
        self.location = managers.Location(self.api_client, entities.Location)
        self.customer = managers.Customer(self.api_client, entities.Customer)
        self.study_status = managers.StudyStatus(self.api_client, entities.StudyStatus)
        self.subject = managers.Subject(self.api_client, entities.Subject)
        self.lead_status = managers.LeadStatus(self.api_client, entities.LeadStatus)
        self.lead_source = managers.LeadSource(self.api_client, entities.LeadSource)
        self.group = managers.Group(self.api_client, entities.Group)
        self.lesson = managers.Lesson(self.api_client, entities.Lesson)
        self.room = managers.Room(self.api_client, entities.Room)
        self.task = managers.Task(self.api_client, entities.Task)
        self.tariff = managers.Tariff(self.api_client, entities.Tariff)
        self.regular_lesson = managers.RegularLesson(
            self.api_client, entities.RegularLesson
        )
        self.pay_item = managers.PayItem(self.api_client, entities.PayItem)
        self.pay_item_category = managers.PayItemCategory(
            self.api_client, entities.PayItemCategory
        )
        self.pay_account = managers.PayAccount(self.api_client, entities.PayAccount)
        self.pay = managers.Pay(self.api_client, entities.Pay)
        self.lesson_type = managers.LessonType(self.api_client, entities.LessonType)
        self.lead_reject = managers.LeadReject(self.api_client, entities.LeadReject)
        self.discount = managers.Discount(self.api_client, entities.Discount)
        self.cgi = managers.CGI(self.api_client, entities.CGI)
        self.customer_tariff = managers.CustomerTariff(
            self.api_client, entities.CustomerTariff
        )
        self.communication = managers.Communication(
            self.api_client, entities.Communication
        )
        self.log = managers.Log(self.api_client, entities.Log)

    @classmethod
    def _create_session(cls) -> aiohttp.ClientSession:
        """
        Create session
        :return: session
        """
        return aiohttp.ClientSession()

    async def auth(self):
        await self.auth_manager.refresh_token()

    async def check_auth(self) -> bool:
        """Check authentification"""
        try:
            await self.auth()
            return True
        except Forbidden:
            return False

    async def close(self):
        """Close connections"""
        await self._session.close()

    @property
    def hostname(self) -> str:
        return self._hostname

    @property
    def email(self) -> str:
        return self._email

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def branch_id(self) -> int:
        return self._branch_id
