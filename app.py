import os
import openai
import pandas

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from flask import Flask, request, render_template
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage
from langchain.callbacks.base import BaseCallbackHandler
import requests

app = Flask(__name__, template_folder='templates')

chat_history = []



def do_calculation(prompt):
    query = prompt
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])
    chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo",  temperature=0),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )
    result = chain({"question": query, "chat_history": chat_history})
    chat_history.append((query, result['answer']))
    newr = result['answer'].replace("\n", '<br>')
    return newr


@app.route("/", methods=["GET", "POST"])
def adder_page():
    request.headers.get('grok-skip-browser-warning', '1234')
    errors = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        if prompt is not None :
            result = do_calculation(prompt)
            return result

    return render_template('demo.html')

if __name__ == "__main__":
    app.run()
