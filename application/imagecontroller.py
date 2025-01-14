import os
import mimetypes
from flask import Blueprint, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv


# Configure Google Generative AI
# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Define your image controller blueprint
image_bp = Blueprint('image', __name__)

UPLOAD_FOLDER = 'static/uploads'  # Ensure this directory exists for uploads

def upload_to_gemini(file_name, file_bytes, mime_type=None):
    """Uploads the given file to Gemini."""
    file_path = f'/tmp/{file_name}'
    with open(file_path, 'wb') as f:
        f.write(file_bytes)
    uploaded_file = genai.upload_file(file_path, mime_type=mime_type)
    return uploaded_file

# The model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@image_bp.route('/upload', methods=['POST'])
def handle_upload():
    files = request.files.getlist('image')
    if not files:
        return jsonify({"error": "No files uploaded."}), 400

    responses = []
    image_urls = []  # To store the URLs of uploaded images

    for file in files:
        mime_type, _ = mimetypes.guess_type(file.filename)
        mime_type = mime_type or 'application/octet-stream'
        file_bytes = file.read()

        # Save the uploaded file to the static uploads folder
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(image_path, 'wb') as f:
            f.write(file_bytes)

        # Upload the file to Gemini
        uploaded_file = upload_to_gemini(file.filename, file_bytes, mime_type=mime_type)

        # Generate content using the model
        response = model.generate_content([
            "input: You are a health specialist with expertise in nutritional values and food analysis. Analyze the food items visible in the image linked below and generate a structured JSON output with information about the dish, ingredients, calorie values, and dietary recommendations. If you are unable to analyze the image directly, please provide a sample JSON response similar to the format below:",
            "output: \"dish_name\": \"Roasted Potatoes with Mushrooms\",          \"ingredients\": [            {{              \"name\": \"Potatoes\",              \"type\": \"Vegetable\",              \"calories_per_100g\": 77,              \"calories_in_dish\": 231,              \"daily_intake_percentage\": 12,              \"warning\": \"None\"            }},            {{              \"name\": \"Mushrooms\",              \"type\": \"Fungi\",              \"calories_per_100g\": 38,              \"calories_in_dish\": 76,              \"daily_intake_percentage\": 4,              \"warning\": \"None\"            }},            {{              \"name\": \"Olive Oil\",              \"type\": \"Fat\",              \"calories_per_100g\": 884,              \"calories_in_dish\": 177,              \"daily_intake_percentage\": 9,              \"warning\": \"High calorie density.\"            }},            {{              \"name\": \"Salt\",              \"type\": \"Seasoning\",              \"sodium_per_100g\": 38758,              \"sodium_in_dish\": 775,              \"daily_intake_percentage\": 32,              \"warning\": \"High sodium content. Use sparingly.\"            }}          ],          \"total_calories_in_dish\": 497,          \"warnings\": [            {{              \"ingredient\": \"Olive Oil\",              \"message\": \"High in calories; limit usage to avoid exceeding fat intake.\"            }},            {{              \"ingredient\": \"Salt\",              \"message\": \"High sodium levels can contribute to hypertension; use less if possible.\"",
            "input: ",
            uploaded_file,
            "whats the ingredients",
            "output: ",
        ])

        responses.append(response.text)
        image_urls.append(f"/static/uploads/{file.filename}")  # Add the uploaded image URL

    # Return the responses and image URLs
    return jsonify({"responses": responses, "imageUrls": image_urls})

# Ensure the uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
