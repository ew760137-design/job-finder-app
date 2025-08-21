from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Finder API is running!"}
