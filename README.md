### SehatGpt Frontend : https://github.com/mAmanullah7/SehatGPT-Frontend

# SehatGPT 
Sehat GPT: Your AI nutritionist, Label Padhega India. 🤖🥗 Upload food images for instant nutrition insights and make informed dietary choices. Empowering you to read labels, understand nutrition.
```
├── app.py                
├── application/          
│   ├── imagecontroller.py
│   └── labelcontroller.py
├── static/             
│   ├── styles.css
│   └── upload/
│       └── images/     
├── templates/         
│   └── index.html
├── requirements.txt   
├── settings.py        
└── wsgi.py
```


# Create virtual environment
```
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

# Install dependencies
```
pip install -r requirements.txt
```


# Create upload directory
```
mkdir -p static/upload/images
```

### Running the Application

Development mode:
``` python app.py ```

Production mode:
``` gunicorn wsgi:app ```

The application will be available at ```http://localhost:5000```

# Image Labeling Application

## Features
- **Image Upload Functionality**: Easily upload images for processing.
- **Image Labeling System**: Add labels to uploaded images for organization and retrieval.
- **Static File Handling**: Efficiently manage static assets.
- **Responsive Web Interface**: Accessible and user-friendly design for all devices.

## Technical Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **File Storage**: Local filesystem
- **Development Server**: Flask built-in server
- **Production Server**: Gunicorn (recommended)

## Development
The application follows a modular structure:
- **`imagecontroller.py`**: Handles image upload and processing.
- **`labelcontroller.py`**: Manages image labeling functionality.
- **`static/styles.css`**: Contains application styling.
- **`templates/index.html`**: Main application template.

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a Pull Request.

## License
This project is licensed under the **MIT License**.

