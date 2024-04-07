from app.data.utils.data_loader import load_data, DataFile
from app.modules.comments.schemas.comments import Comment


class CommentsService:
    def __init__(self):
        """Загрузка данных о комментариях из файла JSON"""
        self.comments_data = load_data(DataFile.COMMENTS)["comments"]

    def get_comments_count(self, news_id: int) -> int:
        """Функция для получения количества комментариев к новости по ее ID"""
        return sum(1 for comment in self.comments_data if comment["news_id"] == news_id)

    def get_comments_by_news_id(self, news_id: int) -> map:
        """Фильтрация и преобразование комментариев в объекты Comment"""
        filtered_comments = filter(
            lambda comment: comment["news_id"] == news_id, self.comments_data
        )
        comments_objects = map(lambda comment: Comment(**comment), filtered_comments)
        return comments_objects
