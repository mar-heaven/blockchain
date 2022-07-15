from fastapi import APIRouter

from blockchain.api.api_v1.endpoints import (
    chain
)

api_router = APIRouter()
api_router.include_router(chain.router, tags=["chain"])