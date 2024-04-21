
# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates
# import os
# import google.generativeai as genai

# # Set up the environment variable for the API key
# os.environ['GOOGLE_API_KEY'] = "..."
# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# # Create an instance of GenerativeModel
# model = genai.GenerativeModel('gemini-pro')

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def get_chat(request: Request):
#     return templates.TemplateResponse("index_EXAMPLE.html", {"request": request})

# @app.post("/")
# async def post_message(request: Request, message: str = Form(...)):
#     # Assuming generate_text or a similar method exists
#     try:
#         response = model.generate_text(prompt=message)
#         response_data = response['choices'][0]['text'].strip()  # Adjust based on actual response format
#     except AttributeError as e:
#         response_data = f"Error: {str(e)}"
#     return templates.TemplateResponse("index.html", {"request": request, "response_data": response_data})






#####


# from fastapi import FastAPI, Form
# import os
# import google.generativeai as genai

# # Set up the environment variable for the API key
# os.environ['GOOGLE_API_KEY'] = "..."
# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# # Create an instance of GenerativeModel
# model = genai.GenerativeModel(model_name="gemini-pro")

# app = FastAPI()

# @app.get("/")
# async def get_chat():
#     with open('index.html', 'r', encoding='utf-8') as file:
#         return file.read()

# @app.post("/chat/")
# async def chat(message: str = Form(...)):
#     prompt_parts = [
#     "You are involved in a project involving matching Data Seekers to Data Providers (Categories: Writers, Graphic Designers, Musicians, Videographers, Dataset Engineers) for custom, unique datasets. The Data Seeker enters some information about what they are seeking, and then they get a list of Data Providers that are a good fit. From here, the Data Seeker can choose to speak with an AI Agent that acts on behalf of the chosen Data Provider to gather necessary information and then create an Ethereum smart contract for the order of the dataset. You will take on the role of this AI Agent. You will first summarize what the Data Seeker stated that he wants.  You will then tell the Data Seeker any constraints or specific specializations that the Data Provider defined. Next, you will ask the Data Seeker to input a longer description of the type of data they need, which will help the Data Provider fulfill the order to the exact needs of the Data Seeker. You will then tell the Data Seeker what the unit of data is for this provider (ie. video, song, row of data), as well as the cost per unit. Here, you will also note any discounts that the Data Provider defined. Then, you will ask for how many units of data the Data Seeker needs, or if they would like to choose one of the discounts options. If they choose a number, you will simply calculate:",
#     "Data Seeker (User): Hello.",
#     "AI Agent (You): Hello, I am Alex’s Agent. I see that you’re interested in Writing services entailing 'Middle East', 'Gaza', 'Food Supplies', and 'Terrorism'. Is this correct? Please say Yes or No.",
#     "Data Seeker (User): I choose Discount 1: 500 images for 0.1 ETH.",
#     "AI Agent (You): Excellent. Let’s confirm these details, and then I will create the smart contract to fulfill your order. You are interested in Graphic services entailing 'Steampunk', 'Armageddon', and 'Nihilism'. Specifically, you want 500 images for 0.1 ETH. Your order will cost 0.1 ETH. Does this sound right? Please say Yes or No.",
#     "Data Seeker (User): Yes",
#     "AI Agent (You): ",
#     ]
#     # Assume generate_content is the correct method to call; replace with the actual method
#     response = model.generate_content(prompt_parts)
#     return {"message": response.text}


from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import os
import google.generativeai as genai

# Set up the environment variable for the API key
os.environ['GOOGLE_API_KEY'] = "..."
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create an instance of GenerativeModel
model = genai.GenerativeModel(model_name="gemini-pro")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat/")
async def chat(request: Request, message: str = Form(...)):
    prompt_parts = [
        "You are involved in a project involving matching Data Seekers to Data Providers (Categories: Writers, Graphic Designers, Musicians, Videographers, Dataset Engineers) for custom, unique datasets. The Data Seeker enters some information about what they are seeking, and then they get a list of Data Providers that are a good fit. From here, the Data Seeker can choose to speak with an AI Agent that acts on behalf of the chosen Data Provider to gather necessary information and then create an Ethereum smart contract for the order of the dataset. You will take on the role of this AI Agent. You will first summarize what the Data Seeker stated that he wants. You will then tell the Data Seeker any constraints or specific specializations that the Data Provider defined. Next, you will ask the Data Seeker to input a longer description of the type of data they need, which will help the Data Provider fulfill the order to the exact needs of the Data Seeker. You will then tell the Data Seeker what the unit of data is for this provider (ie. video, song, row of data), as well as the cost per unit. Here, you will also note any discounts that the Data Provider defined. Then, you will ask for how many units of data the Data Seeker needs, or if they would like to choose one of the discounts options. If they choose a number, you will simply calculate:",
        f"Data Seeker (User): {message}",
        "AI Agent (You): ",
    ]
    # Assume generate_content is the correct method to call; replace with the actual method
    response = model.generate_content(prompt_parts)
    return {"message": response.text}

