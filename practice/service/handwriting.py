from transformers import AutoModelForVision2Seq, AutoProcessor
from fastapi import UploadFile
from PIL import Image
import io

# 모델 load
model = AutoModelForVision2Seq.from_pretrained("microsoft/trocr-base-handwritten")
# 프로세서 load
processor = AutoProcessor.from_pretrained("microsoft/trocr-base-handwritten")


async def handwriting_to_text(handwriting: UploadFile):

    # UploadFile에서 이미지를 PIL.Image로 변환
    contents = await handwriting.read()

    try:
        # 이미지를 PIL로 열기 및 RGB로 변환
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        print(f"이미지 처리 오류: {e}")
        raise ValueError("이미지를 처리하는 중 문제가 발생했습니다.")

    # 손글씨 이미지 전처리
    encoded_handwriting = processor(images=image, return_tensors="pt")

    # 추론
    generated_tokens = model.generate(encoded_handwriting["pixel_values"])

    # 후처리
    generated_text = processor.batch_decode(generated_tokens, skip_special_tokens=True)[
        0
    ]

    return generated_text
