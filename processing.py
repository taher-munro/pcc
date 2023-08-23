import os
import openai

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

def do_calculation(prompt):
    query = prompt
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index.query(query)
