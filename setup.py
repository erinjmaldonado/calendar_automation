import os
from dotenv import load_dotenv
from canvasapi import Canvas
load_dotenv()

# Make an API call and store the response.
API_URL = "https://canvas.csun.edu"
API_KEY = os.environ.get('API_KEY')


# Initialize a new Canvas object
def get_canvas():
    canvas = Canvas(API_URL, API_KEY)
    return canvas
