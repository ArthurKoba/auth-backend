from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from loader import app
from db.models import Users
from db.debs import get_db
from models import RegisterModel

@app.get("/checkAvailabilityUsername/{username}")
async def check_availability_username(username: str):
    return {"is_availability": False}


@app.post("/register/")
async def register_user(register_data: RegisterModel):
    data = register_data.dict()
    data.update(password_hash=data.pop("password"))
    query = insert(Users).values(**data)
    db = get_db()
    try:
        await db.execute(query)
        await db.commit()
    except IntegrityError as e:
        return {"registered": False, "error": str(e)}
    return {"registered": True}
