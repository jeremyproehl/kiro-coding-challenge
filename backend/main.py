from fastapi import FastAPI

app = FastAPI(title="Kiro Coding Challenge API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Kiro Coding Challenge API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
