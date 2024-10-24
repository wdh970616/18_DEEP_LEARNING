from pydantic import BaseModel
from fastapi import UploadFile


class HandwrittingRequest(BaseModel):
    handwritting: UploadFile
