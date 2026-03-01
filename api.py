from fastapi import FastAPI

app = FastAPI() 
@app.get("/prompt")
def read_root():
    return {"message": "Hello World"}   