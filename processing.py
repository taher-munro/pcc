import os
import openai

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

def do_calculation(prompt):
    os.environ["OPENAI_API_KEY"] = "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"
    query = prompt
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index.query(query)
