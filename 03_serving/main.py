from fastapi import FastAPI
from routers import translation


app = FastAPI()


app.include_router(translation.router)

# import uvicorn

# if __name__ == "__main__":
# uvicorn.run(app, port=8000)

# uvicorn main:app --reload --port="포트번호"
