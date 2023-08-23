from flask import Flask, request
from processing import do_calculation

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        if prompt is not None :
            result = do_calculation(prompt)
            return '''
                <html>
                    <body>
                       
                         <form method="post" action=".">
                    <p><textarea name="prompt" rows="10" cols="50" ></textarea></p>
                    <p><input type="submit" value="Submit" /></p>
                </form>
                 <p>Answer: {result}</p>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter Prompt:</p>
                <form method="post" action=".">
                    <p><textarea name="prompt" rows="10" cols="50" ></textarea></p>
                    <p><input type="submit" value="Submit" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

# @app.route("/", methods=["GET", "POST"])
# def index():
#    os.environ["OPENAI_API_KEY"] = " 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"
#    query = input('Prompt:')
#    loader = DirectoryLoader("data/")
#    index = VectorstoreIndexCreator().from_loaders([loader])
#    return index.query(query)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082, debug=True)
