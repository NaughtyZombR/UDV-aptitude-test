from fastapi import APIRouter, HTTPException, status

from app.modules.news.schemas.news import CardNewsReadSchema, ListNewsReadSchema
from app.services.news import NewsService

router = APIRouter()


@router.get("/", response_model=ListNewsReadSchema)
async def get_all_news() -> ListNewsReadSchema:
    """Маршрут для получения списка всех новостей"""

    all_news: ListNewsReadSchema = NewsService.get_all_news()
    return all_news


@router.get(
    "/news/{news_id}",
    response_model=CardNewsReadSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Новость не существует или была удалена",
            "content": {
                "application/json": {
                    "examples": {
                        status.HTTP_404_NOT_FOUND: {
                            "summary": "News not found",
                            "value": {"detail": "News not found"},
                        },
                    }
                }
            },
        }
    },
)
async def get_news(news_id: int) -> CardNewsReadSchema:
    """Маршрут для получения конкретной новости по ее ID"""

    news: CardNewsReadSchema | None = NewsService.get_news_by_id(news_id)

    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="News not found"
        )

    return news
