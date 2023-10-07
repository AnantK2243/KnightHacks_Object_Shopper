# import openai
import json

# Get API KEY
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
api_key = config_data.get("api_key")

print(f"{api_key}")

# Inititate openAi
# openai.api_key = api_key


"""
# Get recommendation form ChatGPT 3.5
def get_Reccomendation(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002", 
        prompt=prompt,
        max_tokens=50,  # Adjust as needed
        n=1,  # Number of completions to generate
        stop=None,  # Stop generation at specified tokens (e.g., ['\n'])
    )
    return response.choices[0].text.strip()
"""