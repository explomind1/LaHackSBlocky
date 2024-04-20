
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import os
import google.generativeai as genai

# Set up the environment variable for the API key
os.environ['GOOGLE_API_KEY'] = "..."
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create an instance of GenerativeModel
model = genai.GenerativeModel('gemini-pro')

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def post_message(request: Request, message: str = Form(...)):
    # Assuming generate_text or a similar method exists
    try:
        response = model.generate_text(prompt=message)
        response_data = response['choices'][0]['text'].strip()  # Adjust based on actual response format
    except AttributeError as e:
        response_data = f"Error: {str(e)}"
    return templates.TemplateResponse("index.html", {"request": request, "response_data": response_data})
