from fastapi import FastAPI, Depends
from db import set_db

app = FastAPI(
    dependencies=[
        Depends(set_db)
    ]
)
