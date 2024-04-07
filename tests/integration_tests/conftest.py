from typing import AsyncGenerator, Dict

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.app import app


@pytest.fixture
def mock_load_data(mocker):
    """Мокируем вызов load_data для модулей news и comments"""

    def _mock_load_data(data):
        mocker.patch("app.services.news.load_data", return_value=data)
        mocker.patch("app.services.comments.load_data", return_value=data)

    return _mock_load_data


# SETUP
@pytest_asyncio.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as async_client:
            yield async_client
