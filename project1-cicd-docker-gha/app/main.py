from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "service": "devops-portfolio-app", "version":"1.0.0"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}