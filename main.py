import os
from typing import Union
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



class PromptInput(BaseModel):
    message: str
    
@app.post("/chat/")
async def chat_with_openai(prompt: PromptInput):
    try:
        response = client.responses.create(
            model="gpt-4.1", # <-----  Change the model according to your API key
            input=prompt.message
        )

        ai_reply = response.choices[0].message.content.strip()
        print(ai_reply)
        return {"response": ai_reply}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}