from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/sobre")
def sobre():
	return render_template("sobre.html")

@app.route("/usuario/<string:usuario>")
def usuarios(usuario):
	return "Usuario %s" % usuario



if __name__ == "__main__":
	app.run(debug=True)