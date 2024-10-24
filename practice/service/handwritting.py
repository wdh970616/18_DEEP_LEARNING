from transformers import AutoModelForVision2Seq, TrOCRProcessor
from PIL import Image
import io

# 모델 load
model = AutoModelForVision2Seq.from_pretrained("microsoft/trocr-base-handwritten")
# 프로세서 load
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")


async def handwritting_to_text(handwritting: object) -> str:

    # UploadFile에서 이미지를 PIL.Image로 변환
    contents = await handwritting.read()  # 비동기적으로 파일 내용을 읽습니다.
    handwritting_image = Image.open(
        io.BytesIO(contents)
    )  # BytesIO를 사용하여 Image 객체로 변환

    # 손글씨 이미지 전처리
    encoded_handwritting = processor(
        handwritting_image, return_tensors="pt"
    ).pixel_values

    # 추론
    generated_tokens = model.generate(encoded_handwritting)

    # 후처리
    generated_text = processor.batch_decode(generated_tokens, skip_special_tokens=True)

    return generated_text[0]
