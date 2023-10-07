import openai
import json

# Get API KEY
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
api_key = config_data.get("api_key")


# Inititate openAi
openai.api_key = api_key

# Get recommendation form ChatGPT 3.5
def get_Reccomendation(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002", 
        prompt= ("Give me a similar item like " + prompt),
        max_tokens=10,
        n=3,
        stop=None,
    )
    return response.choices[0].text.strip()

def main():
    print("In Main")


if __name__ == "__main__":
    main()