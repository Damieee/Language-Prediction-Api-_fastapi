from fastapi import FastAPI
from app.api.language_prediction import router as language_router
from app.services import load_model

app = FastAPI()

# Load the models once the application starts
@app.on_event("startup")
async def startup_event():
    load_model()

# Include the language prediction router
app.include_router(language_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
