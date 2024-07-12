from fastapi import FastAPI

from router import router_memes

app = FastAPI(
    title="Memes"
)

app.include_router(router_memes)



