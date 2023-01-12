from loader import app
from models import RegisterModel


@app.get("/checkAvailabilityUsername/{username}")
async def check_availability_username(username: str):
    return {"is_availability": False}


@app.post("/register/")
async def register_user(register_data: RegisterModel):
    return {"is_availability": False}
