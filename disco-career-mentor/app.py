from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an instance of the Flask application
app = Flask(__name__)

# Access your Adzuna API keys
#ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
#ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

ADZUNA_APP_ID="645920c5"
ADZUNA_APP_KEY="d40d7c4a26537a4c9e345ac8f09d6d6e"

print("ADZUNA_APP_ID:", ADZUNA_APP_ID)
print("ADZUNA_APP_KEY:", ADZUNA_APP_KEY)

# Define a route for job search
@app.route('/jobs/<job_role>')
def get_jobs(job_role):
    # Use the environment variables to construct the URL
    url = f"http://api.adzuna.com/v1/api/jobs/us/search/1?app_id={ADZUNA_APP_ID}&app_key={ADZUNA_APP_KEY}&results_per_page=5&what={job_role}"
    response = requests.get(url)

    # Print status code and response text for debugging
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data", "details": response.text}), response.status_code

# Define a home route
@app.route('/')
def home():
    return jsonify(message="Welcome to Disco Career Mentor!")

# Start the server
if __name__ == "__main__":
    app.run(debug=True)
