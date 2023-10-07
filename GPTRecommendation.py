import openai
import json

# Get API KEY
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
api_key = config_data.get("api_key")

# Inititate openAi
openai.api_key = api_key

# Get recommendation form ChatGPT 3.5
def get_Recommendation(prompt):
    prompt1 = "Give me 3 shopping recommendation that pairs well with a " + prompt + " without explanation or the word a seperated by commas so I can split using python code"
    response = openai.Completion.create(
        engine="text-davinci-002", 
        prompt=prompt1,
        max_tokens=100,
        n=3,
        stop=None,
    )
    return response.choices[0].text.strip()

def main():
    print("In Main")

if __name__ == "__main__":
    main()
