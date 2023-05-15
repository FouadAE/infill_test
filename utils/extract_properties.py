import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY

import json

def extract_properties(text):
    # Initialize the output data
    output_data = {"properties": []}

    # Create prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Extract the properties from the following text: '" +

             str(text) + "'. Please respond with a JSON-formatted string with the following format: " + json.dumps(output_data)
             },
        ],
        temperature=0.2,
    )
    response = response.choices[0].message.content

    try:
        # Attempt to load the response as JSON
        output_data = json.loads(response)
    except json.JSONDecodeError:
        # If the response isn't valid JSON, return a default value or handle the error
        print("Invalid JSON received:", response)
        return None

    print(response)
    return output_data