# import os
# from flask import Flask, jsonify, request, render_template, send_from_directory
# from application.labelcontroller import generate_response
# from flask_cors import CORS

# app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route("/api/generate", methods=["POST"])
# def generate_api():
#     if request.method == "POST":
#         try:
#             req_body = request.get_json()
#             content = req_body.get("contents")
#             response = generate_response(content)
#             response = response.replace("```json","")
#             response = response.replace("```","")
#             response = jsonify(response)

#             response.headers.add("Access-Control-Allow-Origin", "*")

#             return response

#         except Exception as e:
#             return jsonify({ "error": str(e) })

# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory('static', path)


# if __name__ == "__main__":
#     app.run(port=int(os.environ.get('PORT', 5000)), debug=True)


# Testfing the application

import os
from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
from application.labelcontroller import generate_response
from application.imagecontroller import image_bp

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/generate", methods=["POST"])
def generate_api():
    if request.method == "POST":
        try:
            req_body = request.get_json()
            content = req_body.get("contents")
            response = generate_response(content)
            response = response.replace("```json", "").replace("```", "")
            return jsonify(response)
        except Exception as e:
            return jsonify({"error": str(e)})

# Register the image controller blueprint
app.register_blueprint(image_bp)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 5000)), debug=True)
