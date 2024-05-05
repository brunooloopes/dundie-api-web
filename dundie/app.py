from fastapi import FastAPI
from dundie.db import ActiveSession
from .routes import main_router


app = FastAPI(
    title="dundie",
    version="0.1.1",
    description="dundie is a rewards API",
)

app.include_router(main_router)
