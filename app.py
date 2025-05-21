from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/web/inscricao", methods=["GET", "POST"])
def inscricao_web():
        data = request.form
        return jsonify(data)
     

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
