import pytest
from fastapi import status
from httpx import AsyncClient


class TestNews:
    mock_data = {
        "news": [
            {
                "id": 1,
                "title": "Test News 1",
                "date": "2024-01-01T20:56:35",
                "body": "The news",
                "deleted": False,
            }
        ],
        "comments": [
            {
                "id": 1,
                "news_id": 1,
                "title": "comment_1",
                "date": "2024-01-02T21:58:25",
                "comment": "Comment",
            },
            {
                "id": 2,
                "news_id": 1,
                "title": "comment_2",
                "date": "2024-01-02T21:58:25",
                "comment": "Another comment",
            },
        ],
    }

    async def test_news_list(self, async_client: AsyncClient, mock_load_data):
        mock_load_data(self.mock_data)

        response = await async_client.get("/")

        assert (
            response.status_code == status.HTTP_200_OK
        ), "Не удалось получить список новостей"

        data = response.json()
        news_list = data.get("news")
        assert news_list
        first_element = news_list[0]
        assert "id" in first_element
        assert "title" in first_element
        assert "date" in first_element
        assert "body" in first_element
        assert "deleted" in first_element
        assert "comments_count" in first_element

    @pytest.mark.parametrize(
        "mock_data",
        [
            {"news": [], "comments": []},
            {
                "news": [dict(mock_data["news"][0], deleted=True)],
                "comments": mock_data["comments"],
            },
        ],
    )
    async def test_news_list_empty_or_deleted(
        self, async_client: AsyncClient, mock_load_data, mock_data
    ):
        mock_load_data(mock_data)

        response = await async_client.get("/")

        assert (
            response.status_code == status.HTTP_200_OK
        ), "Не удалось получить список новостей"

        data = response.json()
        news_list = data.get("news")
        assert not news_list, "Список новостей не пуст"

    @pytest.mark.parametrize(
        "mock_data",
        [
            mock_data,
            pytest.param(
                {"news": [], "comments": []},
                marks=pytest.mark.xfail(
                    reason="Отсутствующая новость не должна быть отображена",
                    strict=False,
                ),
            ),
            pytest.param(
                {
                    "news": [dict(mock_data["news"][0], deleted=True)],
                    "comments": mock_data["comments"],
                },
                marks=pytest.mark.xfail(
                    reason="Удалённая новость не должна быть отображена", strict=True
                ),
            ),
        ],
    )
    async def test_news_card(
        self, async_client: AsyncClient, mock_load_data, mock_data
    ):
        mock_load_data(mock_data)

        news_id = 1
        response = await async_client.get(f"/news/{news_id}")

        assert (
            response.status_code == status.HTTP_200_OK
        ), "Должен вернуться код 200 для активной новости"

        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            assert "id" in data
            assert "title" in data
            assert "date" in data
            assert "body" in data
            assert "deleted" in data
            assert "comments_count" in data
            assert data["comments_count"] == 2, "Количество комментариев не совпадает"
