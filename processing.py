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
