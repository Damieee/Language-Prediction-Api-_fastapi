from fastapi import APIRouter
from pydantic import BaseModel
from app.services import predict_language

router = APIRouter()

# Request body model
class SentenceInput(BaseModel):
    sentence: str

# Language prediction route
@router.post("/predict_language/")
async def get_language(input_data: SentenceInput):
    sentence = input_data.sentence
    predicted_language = predict_language(sentence)
    return {"sentence": sentence, "predicted_language": predicted_language}
