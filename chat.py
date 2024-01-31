# #PDF
# # ! pip install langchain
# # ! pip install pypdf 

# import openai
# from langchain_community.document_loaders import PyPDFLoader

# openai.api_key  = 'OPENAI_API_KEY'

# loader = PyPDFLoader("Development policy.pdf")
# pages = loader.load()

# print(len(pages))

# page = pages[0]
# print(page.page_content[0:500])
# page.metadata


# # Example: reuse your existing OpenAI setup
# from openai import OpenAI

# # Point to the local server
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# completion = client.chat.completions.create(
#   model="local-model", # this field is currently unused
#   messages=[
#     {"role": "system", "content": "Always answer in rhymes."},
#     {"role": "user", "content": "Introduce yourself."}
#   ],
#   temperature=0.7,
# )

# print(completion.choices[0].message)


import openai
from langchain_community.document_loaders import PyPDFLoader

# Replace OPENAI_API_KEY with your Mistral API key
openai.api_key = "YOUR_MISTRAL_API_KEY"

loader = PyPDFLoader("Development policy.pdf")
pages = loader.load()

print(len(pages))

page = pages[0]
print(page.page_content[0:500])
page.metadata


# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to your Mistral server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="YOUR_MISTRAL_API_KEY")

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
