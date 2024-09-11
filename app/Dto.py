from pydantic import BaseModel

# Request body model
class SentenceInput(BaseModel):
    sentence: str