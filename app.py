from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    wap = "hello world"
    return render_template("index.html", wap=wap)


if __name__ == "__main__":
    app.run(debug=True)
