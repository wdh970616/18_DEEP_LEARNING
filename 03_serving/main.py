from fastapi import FastAPI
from routers import translation

app = FastAPI()


app.include_router(translation.router)
