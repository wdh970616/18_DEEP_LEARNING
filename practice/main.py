from fastapi import FastAPI
from routers import handwritting

app = FastAPI()


app.include_router(handwritting.router)
