from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import STATIC_DIR
from app.routes import router

app = FastAPI(title="Quiz Cidadania Italiana")

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
app.include_router(router)