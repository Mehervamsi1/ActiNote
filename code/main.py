from groq import Groq
import os
from dotenv import load_dotenv 


load_dotenv()

def chat_with_groq(client, prompt, model, response_format):
    completion = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": prompt,
        }]
    )
    return completion.choices[0].message.content

groq_key= os.getenv('grok_api')
client = Groq(api_key=groq_key)
model = "llama3-8b-8192"


#####################Above######################################

prompt = input(str("What's on your mind: "))
full_prompt=prompt
llm_response = chat_with_groq(client, full_prompt, model,{"type": "json_object"})
print(llm_response)