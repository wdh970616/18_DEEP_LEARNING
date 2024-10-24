from fastapi import APIRouter, UploadFile

# from models.handwritting import HandwrittingRequest
from service.handwritting import handwritting_to_text

router = APIRouter()


@router.post("/handwritting")
async def generate_text(handwritting: UploadFile):

    result = handwritting_to_text(handwritting)

    return {"Generated Text": result}
