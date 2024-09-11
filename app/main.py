from fastapi import FastAPI
from app.api.language_prediction import router as language_router

app = FastAPI()

@app.get('/')
async def index():
  return {'message': 'Hello world!'}

# Include the language prediction router
app.include_router(language_router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)
