# Python-RESTful-LLM
Example code for the implementation of RESTful API using Python along with LLM API integration.

## 🛠 Technologies Used

- **Backend:** FastAPI, Pydantic
- **Frontend:** HTML, CSS, JavaScript
- **AI API:** OpenAI
- **Environment Management:** python-dotenv
- **Server:** Uvicorn

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/5ukui/Python-RESTful-LLM.git
cd your-repo
```

### 2. Create a Python Virtual Environment
```
python -m venv venv
```

### 3. Activate the Python Virtual Environment
Windows:
```
venv\Scripts\activate.bat
```
Linux:
```
source venv/bin/activate
```

### 4. Install Requirements
```
pip install -r requirements.txt
```

### 5. Create .env file and add your OpenAI API Key
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 6. Run the App
```
uvicorn main:app --reload
```

## 📁 Project Structure
```
.
├── main.py               # FastAPI backend code
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── templates/
│   └── index.html        # HTML front-end
├── static/
│   └── logo.png          # Static assets (e.g. images)

```

## 📡 API Endpoint
POST /chat/
```
{
  "message": "Hello AI!"
}
```
Response:
```
{
  "response": "Hi! How can I help you today?"
}
```

