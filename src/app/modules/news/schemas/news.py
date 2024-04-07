from typing import Optional, List
from pydantic import BaseModel

from app.modules.comments.schemas.comments import Comment


# Модель данных для новости
class NewsReadSchema(BaseModel):
    id: int
    title: str
    date: str
    body: str
    deleted: bool
    comments_count: Optional[int] = None


# Можно было унаследовать поля из NewsReadSchema, но для соответствия ответа сервера и образца тестового задания,
# создал новую схему, т.к. иначе поле 'comments' было не предпоследним (с примера), а последним.
class CardNewsReadSchema(BaseModel):
    id: int
    title: str
    date: str
    body: str
    deleted: bool
    comments: List[Comment]
    comments_count: Optional[int] = None


class ListNewsReadSchema(BaseModel):
    news: List[NewsReadSchema]
    news_count: Optional[int] = None
