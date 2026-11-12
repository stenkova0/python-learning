from fastapi import FastAPI

app = FastAPI()

@app.get("/bonjour/{nom}")
def bonjour(nom: str):
    return {"message": f"Bonjour {nom} !"}