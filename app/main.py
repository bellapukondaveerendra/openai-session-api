from fastapi import FastAPI
from app.routes import router
# Initialize FastAPI app
app = FastAPI()
app.include_router(router)