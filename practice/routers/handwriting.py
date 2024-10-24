from fastapi import APIRouter, UploadFile, File
from service.handwriting import handwriting_to_text

router = APIRouter()


@router.post("/handwriting")
async def generate_text(handwriting: UploadFile = File(...)):

    result = await handwriting_to_text(handwriting)

    return {"Generated Text": result}
