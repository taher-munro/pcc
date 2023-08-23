from flask import Flask, request, render_template
from processing import do_calculation

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        if prompt is not None :
            result = do_calculation(prompt)
            return render_template('screen.html',result=result)

    return render_template('screen.html')

if __name__ == "__main__":
    app.run()
