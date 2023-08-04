from fastapi import FastAPI

from src.errors import global_error_handler
from src.api.endpoints.contact import router as contact_router


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(contact_router, prefix="/api/v1")

    application.add_exception_handler(Exception, global_error_handler)

    return application


app = get_application()
