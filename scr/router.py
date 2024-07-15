from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import memes
from database import get_async_session
from schemas import MemesCreate, MemesUpdate

router_memes = APIRouter(
    prefix="/memes",
    tags=["Memes"]
)


@router_memes.get("/")
async def get_memes(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(memes)
    except Exception:
        raise HTTPException(status_code=500, detail='Нет мемов!')
    else:
        result = await session.execute(query)
        return result.mappings().all()


@router_memes.post("/")
async def add_memes(new_memes: MemesCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(memes).values(**new_memes.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': '200'}


@router_memes.get("/{id}")
async def get_mem(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(memes).where(memes.c.id == id)
    if query is None:
        raise HTTPException(status_code=404, detail='Не найден мем')
    result = await session.execute(query)
    return result.mappings().all()


@router_memes.put("/{id}")
async def edit_mem(id: int, update_memes: MemesUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(memes).where(memes.c.id == id).values(**update_memes.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": '200'}


@router_memes.delete("/{id}")
async def delete_mem(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(memes).where(memes.c.id == id)
    if stmt is None:
        raise HTTPException(status_code=404, detail="Не найден мем!")
    await session.execute(stmt)
    await session.commit()
    return {"status": '204 No Content'}
