from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


async def global_error_handler(
    _: Request,
    exc: Exception
) -> JSONResponse:
    return JSONResponse(
        {"errors": "Internal Server Error"},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR
    )
