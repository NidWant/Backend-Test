from enum import Enum
from typing import Optional
import traceback


class Kind(Enum):
    Other = 0  # Unclassified error. This value is not printed in the error message.
    AlreadyExists = 1  # Item already exists.
    BadGateway = 2  # Bad gateway
    Conflict = 3  # item status in conflict
    Database = 4  # Error from database.
    Internal = 6  # Internal error or inconsistency.
    Invalid = 7  # Invalid operation for this type of item.
    NotFound = 8  # Item not found.
    Request = 9  # Invalid Request
    Response = 10  # Invalid Response
    ResponseStatusCode = 11  # Invalid Response status code.
    Validation = 15  # Input validation error.
    Authorization = 16  # Unauthorized user
    Authentication = 17  # Unauthenticated user


class AppException(Exception):
    def __init__(
            self,
            kind: Kind,
            location: str,
            message: str,
            code: str,
            details: dict = None,
            param: Optional[str] = None,
            err: Optional[Exception] = None,
    ):
        self.kind = kind
        self.location = location
        self.param = param
        self.message = message
        self.code = code
        self.details = details
        self.err = err

    def __str__(self):
        return f"{self.kind}: {self.message}"

    def stack_trace(self) -> str:
        if self.err:
            return "".join(traceback.format_exception(self.err))
        return "".join(traceback.format_exception(self))
