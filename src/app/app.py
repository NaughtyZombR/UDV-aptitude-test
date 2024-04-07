from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    """Асинхронный контекстный менеджер для выполнения кода до и после запуска приложения."""

    # Включаем маршрутизатор в приложение
    fastapi_app.include_router(router)

    yield  # Возвращаем работу приложению
    # тут можно выполнить код после завершения приложения


# Создание экземпляра FastAPI
app = FastAPI(title="NewsForumAPI", version="0.0.1", lifespan=lifespan)
