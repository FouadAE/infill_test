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
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Extract the properties from the following text " +

             "Here is the  text" +
             str(text) + "the output should be a JSON-formatted string with the following format: " + str(output_data)
             },
        ],
        temperature=0.9,
    )
    # response = openai.ChatCompletion.create(
    #     engine="gpt-4",
    #     prompt="Extract the properties from the following text " +
    #          "Here is the  text" +
    #        str(text) + "the output should be a JSON-formatted string with the following format: " + str(output_data)
    #           ,
    #       # You can specify a stopping condition if needed
    #     temperature=0.2,  # Adjust the temperature to control the randomness of the output
        
        
    # )
    # Get the properties from the response
    #properties = response.choices[0]
    # Parse the response and return the mapping
    #output_data = json.loads(properties)

    #return properties
    response = response.choices[0].message.content
    output_data = json.loads(response)
    print(response)
    return output_data

