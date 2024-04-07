import pytest
from unittest.mock import patch
from app.services.news import NewsService


@pytest.fixture
def mock_load_data():
    mock_data = [
        {
            "id": 1,
            "title": "Test News 1",
            "date": "2024-01-01T20:56:35",
            "body": "The news",
            "deleted": False,
        }
    ]
    with patch("app.services.news.NewsService._load_news_data", return_value=mock_data):
        yield


@pytest.fixture
def mock_load_data_comments():
    mock_data = {
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
        ]
    }
    with patch("app.services.comments.load_data", return_value=mock_data):
        yield


def test_get_news_by_id(mock_load_data, mock_load_data_comments):
    news_service = NewsService()
    news_item = news_service.get_news_by_id(1)
    assert news_item.title == "Test News 1"
    assert len(news_item.comments) == 2
    assert news_item.comments_count == 2
