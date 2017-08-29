from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/acessar", methods=["GET","POST"])
def acessar():
	if request.method == "POST":
		print(request.form['usuario'])
		print(request.form['senha'])
	else:
		pass
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)