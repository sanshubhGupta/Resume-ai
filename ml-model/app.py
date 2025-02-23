#FastAPI endpoint for resume parsing

from fastapi import FastAPI, UploadFile, File
import shutil
import os
from resume_parser import extract_text_from_pdf, extract_details

app = FastAPI()

UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/parse-resume/")
async def parse_resume(file: UploadFile = File(...)):
    """api to parse resume and extract details"""
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    #save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #extract text and parse details
    resume_text = extract_text_from_pdf(file_path)
    details = extract_details(resume_text)

    return {"filename": file.filename, "parsed_data" : details}
