import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY


def map_csv_to_firebase(rawtext, firebase_schema):
    
    output = {'firebase_key': 'corresponding column name, or NA if no mapping found'}

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Please take the rawtext and extract the headers and the first row of values from the raw text and map the headers to the Firebase schema and return the corresponding mapping in JSON format. If there is no mapping for a header, please set the value to NA." +

             "Here is the raw text" + str(rawtext) +

             "And here is the Firebase schema:"+str(firebase_schema) +

             "Please return the mapping in this format:"+str(output)
             },
        ]
    )
    mapping = response.choices[0].message.content

    # Parse the response and return the mapping
    output_data = json.loads(mapping)
    # print(output_data)
    return output_data
