import os
from openai import OpenAI
from google import genai

# Make sure all input values in the query() function are string values, although config_arg_num should be an integer inputed as a string.

def gen_query(config_client, config_key, config_model, config_query, config_arg_num):

    if config_client == "OpenAI":

        client = OpenAI(api_key = os.environ.get(config_key))

        response = client.responses.create(
            model = config_model,
            input = config_query + " Based on the previous search query, give me " + config_arg_num + " new search queries that could find webpages more relevant to the purpouse of the query in a new-query-new-line format."
        )

        print(response.output_text)

    if config_client == "Google":

        client = genai.Client(api_key = config_key)

        response = client.models.generate_content(
            model = config_model,
            contents = config_query + " Based on the previous search query, give me " + config_arg_num + " new search queries that could find webpages more relevant to the purpouse of the query in a new-query-new-line format.",
        )

        print(response.text)

def search_query():
    pass
