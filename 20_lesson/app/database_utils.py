from app.user_models import User, AccessToken
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Depends
from app.db import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def get_access_token_db(session: AsyncSession = Depends(get_async_session)):  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)