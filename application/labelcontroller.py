import google.generativeai as genai
from dotenv import load_dotenv

import os


# Configure Google Generative AI
# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



# Set up the model
generation_config = {
    "temperature": 2.0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="assume you are a health specialist, having knowledge about all kinds of foods their ingredients (not their measurements) and it's calorific values with daily intakes values and a warning if its higher then the recommended daily dose. Also make sure the response is only a json which can be used as a api call response.",
)

chat_session = model.start_chat(
   history=[
     {
       "role": "user",
       "parts": [
         "A coca cola",
       ],
     },
     {
       "role": "model",
       "parts": [
         """{
  "product": "Coca-Cola (Can)",
  "serving_size": "355 ml (12 oz)",
  "nutritional_breakdown": {
    "calories": "140 kcal",
    "protein": "0g",
    "carbohydrates": {
      "total": "39g",
      "sugars": "39g"
    },
    "fats": {
      "total": "0g",
      "saturated_fats": "0g",
      "trans_fats": "0g"
    },
    "fiber": "0g",
    "sodium": "45mg",
    "cholesterol": "0mg",
    "caffeine": "34mg"
  },
  "key_nutrients": {
    "sugars": "High sugar content (39g per can)",
    "sodium": "Contains a moderate amount of sodium",
    "caffeine": "Provides 34mg of caffeine"
  },
  "daily_intake_considerations": {
    "calories": "140 kcal per can, contributing to overall daily caloric intake",
    "sugars": "39g of sugars is above the recommended daily intake limit for added sugars (~25g for women, ~36g for men according to AHA)",
    "sodium": "45mg, contributing to the daily recommended limit (less than 2300mg)"
  },
  "warnings": {
    "high_sugar_content": "Excessive consumption may contribute to weight gain, increase risk of diabetes, and other metabolic issues",
    "empty_calories": "Provides no essential nutrients, only calories from sugar"
  }
}. \n""",
       ],
     },
   ]
 )
def generate_response(content):
    
    response = chat_session.send_message(content)
    
    return response.text.strip()
