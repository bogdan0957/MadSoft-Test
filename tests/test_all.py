import pytest
from http import HTTPStatus

from httpx import AsyncClient

from scr.main import app


@pytest.mark.anyio
async def test_memes():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/memes")
    assert response.status_code == HTTPStatus.OK


@pytest.mark.anyio
async def test_get_mem():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/memes/6")
    assert response.status_code == HTTPStatus.OK


@pytest.mark.anyio
async def test_post_mem():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/memes", json={
            "id": 52,
            "meme": "test",
            "description": "test",
        })
    assert response.status_code == HTTPStatus.OK


@pytest.mark.anyio
async def test_delete_mem():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/memes/52/")
    assert response.status_code == HTTPStatus.OK
