# Alfacrm

Асинхронный Python‑клиент для [AlfaCRM REST API v2](https://alfacrm.pro/knowledge/integration/api#googtrans(ru|null)).

Библиотека построена на `aiohttp` и `pydantic v2`, предоставляет удобные менеджеры сущностей (list/get/save) и асинхронную пагинацию.

## Требования

- Python >= 3.12
- Зависимости устанавливаются автоматически: `aiohttp`, `pydantic`

## Установка

```bash
pip install alfacrm
```

## Быстрый старт

```python
import asyncio
import os

from alfacrm import AlfaClient

ALFACRM_API_KEY = os.getenv("ALFACRM_API_KEY")
ALFACRM_EMAIL = os.getenv("ALFACRM_EMAIL")
ALFACRM_BASE_URL = os.getenv("ALFACRM_BASE_URL")  # например: "demo.s20.online" или полный URL
ALFACRM_DEFAULT_BRANCH_ID = 1


async def main():
    client = AlfaClient(
        hostname=ALFACRM_BASE_URL,
        email=ALFACRM_EMAIL,
        api_key=ALFACRM_API_KEY,
        branch_id=ALFACRM_DEFAULT_BRANCH_ID,
    )
    try:
        # Проверка авторизации (опционально)
        if not await client.check_auth():
            print("Auth error")
            return

        # Пример: получить урок с id=1
        lesson = await client.lesson.get(1)
        print(lesson)

        # Пример: изменить и сохранить филиалы
        branches = await client.branch.list(page=0, count=20)
        for b in branches:
            b.name = f"{b.name} - Edited"
            await client.branch.save(b)
    finally:
        await client.close()


if __name__ == "__main__":
    # На Windows может понадобиться политика цикла событий
    # import asyncio; asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
```

## Клиент и аутентификация

- Параметры клиента: `hostname`, `email`, `api_key`, `branch_id`.
- Токен авторизации обновляется автоматически через `AuthManager`.
- Метод `check_auth()` возвращает `True/False` без исключений.
- Закрывайте соединение вызовом `await client.close()`.

## Операции с сущностями

Каждая сущность доступна через менеджер, например `client.customer`, `client.branch` и т.д.

- list: `items = await client.customer.list(page=0, count=100, **filters)`
- get: `customer = await client.customer.get(123)`
- save: `await client.customer.save(model)` — создаёт или обновляет по наличию `id` в модели

Модели — это Pydantic‑классы (v2). Метод `serialize()` формирует JSON‑совместимый payload; поля дат/времени преобразуются автоматически.

## Пагинация

Асинхронный итератор страниц:

```python
async for page in client.customer.paginator(page_size=100, is_study=True):
    for customer in page.items:
        print(customer.id, customer.name)
```

Где `page.items` — элементы текущей страницы, `page.total` — всего записей, `page.count` — элементов на странице.

## Кастомные модели (пользовательские поля)

Вы можете расширять встроенные модели и подменять их в менеджерах.

```python
from alfacrm import AlfaClient, managers
from alfacrm.entities import Customer


class CustomCustomer(Customer):
    custom_field: int | None = None


class CustomAlfaClient(AlfaClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Подменяем модель в соответствующем менеджере
        self.customer = managers.Customer(
            api_client=self.api_client,
            entity_class=CustomCustomer,
        )
```

## Доступные сущности

- Branch, Location, Customer, StudyStatus, Subject
- LeadStatus, LeadSource, LeadReject, Communication, Log
- Group, Lesson, LessonType, RegularLesson, Room, Task
- Tariff, CustomerTariff, Discount
- Pay, PayAccount, PayItem, PayItemCategory
- CGI

Доступ к ним через одноимённые менеджеры `client.<name>`.

## Обработка ошибок

Исключения (все наследуются от `ApiException`):

- BadRequest (400), Unauthorized (401), Forbidden (403), NotFound (404), MethodNotAllowed (405)

Полезно оборачивать вызовы в `try/except` при интеграции и логировать `str(e)`.

## Примечания

- `hostname` можно указывать как короткое имя (`demo`) или полный хост/URL — клиент приведёт к `*.s20.online` автоматически.
- Параметр `branch_id` включается в путь `v2api/{branch_id}/...` (глобальные методы вызываются без него).
