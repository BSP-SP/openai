import os
os.environ['OPENAI_API_KEY']="your_api"

from gpt_index import GPTSimpleVectorIndex




# load from disk
index = GPTSimpleVectorIndex.load_from_disk('indexdata/index.json')

statement = "start"

while statement != 'exit':
    statement = input('What is your question? > ')
    print(" Your question is - " + statement)
    print("Answer: ")
    print(index.query(statement))