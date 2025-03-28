from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000)