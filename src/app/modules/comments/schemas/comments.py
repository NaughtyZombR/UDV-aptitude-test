from pydantic import BaseModel


# Модель данных для комментария
class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: str
    comment: str
