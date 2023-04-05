import os
os.environ["OPENAI_API_KEY"] = "your_api"

from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader


documents = SimpleDirectoryReader('sourcedata').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)

# save to disk
index.save_to_disk('indexdata/index.json')

