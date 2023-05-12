import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY


def extract_properties(text):
    # Initialize the output data
    output_data = {"properties": []}
    # Create prompt
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Extract the properties from the following text " +

             "Here is the  text" +
             str(text) + "the output should be a JSON-formatted string with the following format: " + str(output_data)
             },
        ]
    )
    # Get the properties from the response
    properties = response.choices[0].message.content
    # Parse the response and return the mapping
    output_data["properties"] = json.loads(properties)

    return output_data


