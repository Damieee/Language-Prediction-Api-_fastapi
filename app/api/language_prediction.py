from fastapi import APIRouter
from app.services import predict_language
from app.Dto import SentenceInput
router = APIRouter()

# Language prediction route
@router.post("/predict_language/")
async def get_language(input_data: SentenceInput):
    sentence = input_data.sentence
    predicted_language = predict_language(sentence)
    return {"sentence": sentence, "predicted_language": predicted_language}
