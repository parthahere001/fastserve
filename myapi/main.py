from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def getItems():
    return ['Item1', 'Item2', 'Item3']