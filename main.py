from fastapi import FastAPI

app = FastAPI()


@app.get('/memes/')
def hello():
    return 'Привет'

