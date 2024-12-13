__all__ = ("router",)

from aiogram import Router

from .network_parameters_router import router as network_router
from .base_router import router as base_router

router = Router(name=__name__)

router.include_routers(
network_router,
    base_router,
   )