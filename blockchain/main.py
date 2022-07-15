from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from blockchain.api.api_v1.api import api_router
from blockchain.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.project_name,
        debug=settings.debug,
        openapi_url="/api/v1/openapi.json",
        default_response_class=ORJSONResponse
    )
    application.include_router(api_router, prefix=settings.api_v1_str)
    return application


app = get_application()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
