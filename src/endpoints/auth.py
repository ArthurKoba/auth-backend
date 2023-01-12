from app import app


@app.post("/getToken/")
async def get_token():
    return {"message": "test"}
