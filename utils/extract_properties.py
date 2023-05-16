import openai
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY

import json
def extract_properties(text):
    # Initialize the output data
    output_data = {"properties": []}
    #start time
    start_time = time.time()
    # Create prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        messages=[
            {"role": "user", "content": "Extract the properties from the following text: '" +
             str(text) + "'. Please respond with a JSON-formatted string with the following format: " + json.dumps(output_data)
             },
        ],
    )
    response_content = response.choices[0].message.content
    #end time
    end_time = time.time()
    #print time
    print("Time taken to extract properties: " + str(end_time - start_time))
    try:
        # Attempt to load the response content as JSON
        output_data = json.loads(response_content)
    except json.JSONDecodeError:
        # If the response isn't valid JSON, return a default value or handle the error
        print("Invalid JSON received:", response_content)
        return None

    return output_data
