import os
import openai

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from flask import Flask, request, render_template
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

app = Flask(__name__, template_folder='templates')



chat_history = []

def do_calculation(prompt):
    query = prompt
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])
    chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )
    result = chain({"question": query, "chat_history": chat_history})
    return result['answer']

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        if prompt is not None :
            result = do_calculation(prompt)
            return render_template('demo.html',result=result)

    return render_template('demo.html')

if __name__ == "__main__":
    app.run()
