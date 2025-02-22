from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML API is running..."}

# Run the API: uvicorn app:app --reload
