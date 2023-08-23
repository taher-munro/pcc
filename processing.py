import os

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

def do_calculation(prompt):
    os.environ["OPENAI_API_KEY"] = " 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"
    query = prompt
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index.query(query)