import sys

from fastapi import FastAPI

import verifcation_code_recog

# uvicorn main:app --host 0.0.0.0 --port 8080 --reload
# http://127.0.0.1:8000/docs

app = FastAPI()
sys.setrecursionlimit(10000)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/picture/base64/")
async def verifByBase64(base64Encode: str):
    return verifcation_code_recog.verifcationCodeByB64(base64Encode)

@app.get("/picture/url")
async def verifByUrl(picUrl: str):
    return verifcation_code_recog.verifcationCodeByUrl(picUrl)
