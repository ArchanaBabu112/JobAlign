from fastapi import FastAPI, File, UploadFile
from openai import OpenAI
from dotenv import load_dotenv
import openai
import os 

load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")
openai.organization=os.getenv("OPENAI_ORG")
app=FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/talk" )
async def post_audio(file: UploadFile):
    audio_file= open(file.filename, "rb")
    transcript = openai.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)
    print(transcript)
    

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}