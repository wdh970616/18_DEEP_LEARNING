from fastapi import FastAPI
from practice.routers import handwriting

app = FastAPI()


app.include_router(handwriting.router)
