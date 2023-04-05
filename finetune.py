import os
os.environ["OPENAI_API_KEY"] = "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"

from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader


documents = SimpleDirectoryReader('sourcedata').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)

# save to disk
index.save_to_disk('indexdata/index.json')

