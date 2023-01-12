from loader import app
from models import AuthModel


@app.post("/getToken/")
async def get_token(auth: AuthModel):
    return {"message": "test"}
