from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Bandofind API is running!"
    }
