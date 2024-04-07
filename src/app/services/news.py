from typing import Optional

from app.data.utils.data_loader import load_data, DataFile
from app.modules.news.schemas.news import (
    NewsReadSchema,
    CardNewsReadSchema,
    ListNewsReadSchema,
)
from app.services.comments import CommentsService


class NewsService:
    @staticmethod
    def _load_news_data():
        """Приватный метод для загрузки данных о новостях из файла JSON"""
        return load_data(DataFile.NEWS)["news"]

    @staticmethod
    def get_news_by_id(news_id: int) -> Optional[CardNewsReadSchema]:
        """Функция для получения новости по ее ID"""
        news_data = NewsService._load_news_data()

        news = next(
            (
                news
                for news in news_data
                if news["id"] == news_id and not news["deleted"]
            ),
            None,
        )
        if not news:
            return None

        comments_service = CommentsService()
        comments = list(comments_service.get_comments_by_news_id(news_id=news["id"]))

        return CardNewsReadSchema(
            **news,
            comments=comments,
            comments_count=comments_service.get_comments_count(news_id)
        )

    @staticmethod
    def get_all_news() -> ListNewsReadSchema:
        """Функция для получения всех новостей"""
        news_data = NewsService._load_news_data()

        active_news = filter(lambda news: not news["deleted"], news_data)

        # Для большого проекта, по хорошему, использовать итераторы, т.к. они выполняются лениво, по мере необходимости
        # В общем, для оптимизации использования ресурсов, но у нас список небольшой и данные нужны сразу,
        # поэтому использую списковое включение.
        #
        # iter_news_with_comments = map(
        #     lambda news: NewsReadSchema(**news, comments_count=get_comments_count(news["id"])),
        #     active_news,
        # )

        news_with_comments = [
            NewsReadSchema(
                **news, comments_count=CommentsService().get_comments_count(news["id"])
            )
            for news in active_news
        ]

        return ListNewsReadSchema(
            news=news_with_comments, news_count=len(news_with_comments)
        )
