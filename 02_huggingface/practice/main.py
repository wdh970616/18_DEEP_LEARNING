from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import base64
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="images"), name="images")


# 데이터 모델 정의
class ImageData(BaseModel):
    image: str


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", encoding="utf-8") as f:
        return f.read()


@app.post("/recognize")
async def recognize_text(image_data: ImageData):
    image = image_data.image
    if not image:
        raise HTTPException(status_code=422, detail="Image data is required.")

    # Base64 이미지 데이터에서 'data:image/png;base64,' 부분 제거
    image_data = image.split(",")[1]
    with open("images/drawn_image.png", "wb") as f:
        f.write(base64.b64decode(image_data))

    response = query("images/drawn_image.png")
    return {"text": response.get("text", "인식된 텍스트가 없습니다.")}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
