#python3 -m venv my_venv
#source my_venv/bin/activate
#chainlit run CHATGPT_clone.py -w

import chainlit as cl
#from openai import OpenAI
import openai

with open('API_Key.txt','r') as api:
    apikey= api.readline().split('APIKey=')[1].strip()

openai.api_key= apikey
#client = OpenAI(api_key= )

@cl.on_message
async def main(message: str):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": "You are a helpful assistant"},
        {"role": "user", "content": str(message.content)}
    ],
    #messages=[
    #  {
    #    "role": "assistant",
    #    "content": [
    #      {
    #        "type": "text",
    #        "text": "You are a helpful assistant"
    #      }
    #    ]
    #  },
    #  {
    #    "role": "user",
    #    "content": [
    #      {
    #        "type": "text",
    #        "text": str(message)
    #      }
    #    ]
    #  },
    #],
    temperature=1
    )
    await cl.Message(content= f"{response.choices[0].message.content}").send()
"""
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": [
          {
            "type": "text",
            "text": "You are a career guidence coach with expertise in computer science"
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Are programming jobs going to go extinct. Give me carrer advice on how to build a carrer in computer science domain"
          }
        ]
      },
      #{
      #  "role": "assistant",
      #  "content": [
      #    {
      #      "type": "text",
      #      "text": "Creating an AI chat application is a great project! Here's a simple example script in Python using the NLTK library to build a basic chatbot. \n\nFirst, you need to install the NLTK library by running the following command in your terminal:\n\n```bash\npip install nltk\n```\n\nNext, here's an example script:\n\n```python\nimport nltk\nnltk.download('punkt')\nfrom nltk.chat.util import Chat, reflections\n\npairs = [\n    [\n        r\"my name is (.*)\",\n        [\"Hello %1, how are you today?\",]\n    ],\n    [\n        r\"what is your name?\",\n        [\"My name is Chatbot and I'm here to help you.\",]\n    ],\n    [\n        r\"how are you?\",\n        [\"I'm doing good. How about you?\",]\n    ],\n    [\n        r\"sorry (.*)\",\n        [\"No problem, don't apologize.\",]\n    ],\n    [\n        r\"quit\",\n        [\"Goodbye, take care. See you soon!\"]\n    ],\n]\n\ndef chatbot():\n    print(\"Hi, I'm your chatbot. How can I assist you today?\")\n    chat = Chat(pairs, reflections)\n    chat.converse()\n\nif __name__ == \"__main__\":\n   "
      #    }
      #  ]
      #}
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    #int(response)
"""
    