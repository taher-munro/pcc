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

if __name__ == '__main__':
    app.run()
