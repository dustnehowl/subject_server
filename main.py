from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.post("/upload")
async def upload_file(student_id: str = Form(...), file: UploadFile = File(...)):
    try:
        base_url = f'./submit/{student_id}/'
        file_name = base_url + str(file.filename)

        if not os.path.exists(base_url):
            os.makedirs(base_url)

        print(file_name)
        with open(file_name, "wb") as f:
            f.write(file.file.read())
        
        # 여기에서 student_id와 파일 정보를 활용하여 원하는 처리를 수행할 수 있습니다.

        return JSONResponse(content={"message": "파일 업로드 성공"})
    except Exception as e:
        return JSONResponse(content={"error": "파일 업로드 실패"}, status_code=500)


