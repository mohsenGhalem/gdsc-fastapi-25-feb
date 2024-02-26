
from fastapi import FastAPI
import uvicorn

from services import auth_service
from services import user_service


app = FastAPI()

app.include_router(auth_service.router)

app.include_router(user_service.router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")