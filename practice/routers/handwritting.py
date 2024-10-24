from fastapi import APIRouter, UploadFile, File
from service.handwritting import handwritting_to_text

router = APIRouter()


@router.post("/handwritting")
async def generate_text(handwritting: UploadFile = File(...)):

    result = await handwritting_to_text(handwritting)

    return {"Generated Text": result}
