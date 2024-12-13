__all__ = ("router",)

from aiogram import Router

from .base_routers import router as base_router

router = Router(name=__name__)

router.include_routers(
    base_router,
   )