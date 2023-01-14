from typing import Optional
from sqlalchemy import select

from loader import app
from db.models import Users
from db.debs import get_db


@app.get("/getUsers")
async def get_users(user_id: Optional[int] = None):
    query = select(Users)
    db = get_db()
    raw_users = (await db.execute(query)).all()
    users = []

    for raw_user in raw_users:
        user_obj = raw_user[0]
        user = {
            "username": user_obj.username,
            "nickname": user_obj.nickname,
        }
        users.append(user)
    return {"users": users}
