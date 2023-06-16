from fastapi import FastAPI
from app.api.routes import router as api_router
from app.handlers.error_handlers import AppException, app_error_handler

app = FastAPI()

app.add_exception_handler(AppException, app_error_handler)

app.include_router(api_router)
