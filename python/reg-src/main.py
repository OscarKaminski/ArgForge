import os
from openai import OpenAI
from google import genai
from brave import Brave
from colorama import Fore, Style
from colorama import init as colorama_init

colorama_init()

# Generate New Queries

def gen_query(config_client, config_key, config_model, config_query, config_arg_num):

    if config_client == "OpenAI":

        client = OpenAI(api_key = os.environ.get(config_key))

        response = client.responses.create(
            model = config_model,
            input = config_query + " Based on the previous search query, give me " + config_arg_num + " new search queries that could find webpages more relevant to the purpouse of the query in a new-query-new-line format."
        )

        print(response.output_text)

    elif config_client == "Google":

        client = genai.Client(api_key = config_key)

        response = client.models.generate_content(
            model = config_model,
            contents = config_query + " Based on the previous search query, give me " + config_arg_num + " new search queries that could find webpages more relevant to the purpouse of the query in a new-query-new-line format.",
        )

        print(response.text)

    else:
        print(f"{Fore.RED}ERROR: Invalid/Unsupported Client.{Style.RESET_ALL}")

# Search Generated Queries (WIP)

#def search_query(config_client, config_key, config_query, config_arg_num, config_rslt_num):

#    if config_client == "Brave":

#       brave = Brave(api_key = config_key)

#       try:
#           search_results = brave.search(q = config_query, count = config_rslt_num)
            
#           for result in search_results.web_results:
#               print(f"Title: {result.title}")
#               print(f"URL: {result.link}")
#               print(f"Description: {result.description}\n")
                
#       except Exception as e:
#           print(f"Error: {str(e)}")

#   else:
#        print(f"{Fore.RED}ERROR: Invalid/Unsupported Client.{Style.RESET_ALL}")
