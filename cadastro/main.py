from flask import Flask, render_template, redirect, session, request
from pymongo import MongoClient

flaskbanco = MongoClient().flaskbanco
usuarios = flaskbanco.usuarios

app = Flask(__name__)
app.secret_key = "hdhdhd"

@app.route("/")
def index():
	if 'username' in session:
		return "Pagina"
	else:
		return redirect("/login")

@app.route("/login",  methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		u = usuarios.find_one({"usuario": request.form['usuario'], "senha": request.form['senha']})
		if u:
			session['username'] = request.form['usuario']
			return redirect("/")
		return redirect("/login")

@app.route("/logout")
def logout():
	session.pop('username', None)
	return redirect("/login")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	if request.method == "GET":
		return render_template("cadastro.html")
	else:
		u = {}
		u['usuario'] = request.form['usuario']
		u['email'] = request.form['email']
		u['senha'] = request.form['senha']
		usuarios.insert_one(u)
		session['username'] = request.form['usuario']
		return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)