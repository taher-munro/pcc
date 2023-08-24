

def do_calculation(prompt):
    os.environ["OPENAI_API_KEY"] = ""
    query = prompt
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index.query(query)