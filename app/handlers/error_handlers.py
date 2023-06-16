from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.core.error import AppException, Kind


# httpErrorStatusCode maps an error Kind to an HTTP Status Code.
def http_error_status_code(k: Kind) -> int:
    match k:
        case Kind.Invalid | Kind.AlreadyExists | Kind.Validation | Kind.Request:
            return status.HTTP_400_BAD_REQUEST
        case Kind.Authentication:
            return status.HTTP_401_UNAUTHORIZED
        case Kind.Authorization:
            return status.HTTP_403_FORBIDDEN
        case Kind.NotFound:
            return status.HTTP_404_NOT_FOUND
        case Kind.Conflict:
            return status.HTTP_409_CONFLICT
        case Kind.BadGateway:
            return status.HTTP_502_BAD_GATEWAY
        case _:
            return status.HTTP_500_INTERNAL_SERVER_ERROR


async def app_error_handler(request: Request, exc: AppException):
    content = {
        "status": "error",
        "message": exc.message
    }
    if exc.details:
        content.update({"details": exc.details})

    logger.error("code: {}, location: {}, message: {}, trace: {}".format(exc.code, exc.location, exc.message,
                                                                         exc.stack_trace()))
    return JSONResponse(
        status_code=http_error_status_code(exc.kind),
        content=content
    )
