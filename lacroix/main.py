#UTF-8

from flask import Flask, session, redirect, request, render_template
from pymongo import MongoClient

banco = MongoClient().banco
escolas = banco.escolas
alunos = banco.alunos
adm_users = banco.adm_users

app = Flask(__name__)
app.secret_key = "lacroixefoda"

@app.route("/")
def index():
	if "username" in session:
		lista_escolas = list(escolas.find({},{"_id": 0}))
		return render_template("escolas.html", lista_escolas = lista_escolas)
	else:
		return redirect("/login")
	

@app.route("/")
def index_2():
	return "Lacroix eh vida"

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		u = adm_users.find_one({"usuario": request.form['usuario'], "senha": request.form['senha']})
		if u:
			session['username'] = request.form['usuario']
			lista_escolas = list(escolas.find({},{"_id": 0}))
			return render_template("escolas.html", lista_escolas = lista_escolas)

@app.route("/logout")
def logout():
	session.pop('username', None)
	return redirect("/login")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	if request.method == "GET":
		return render_template("cadastro_adm.html")
	else:
		u = {}
		u['usuario'] = request.form['usuario']
		u['email'] = request.form['email']
		u['senha'] = request.form['senha']
		adm_users.insert_one(u)
		session['username'] = request.form['usuario']
		return redirect("/")

@app.route("/escola/new", methods=["GET", "POST"])
def new_escola():
	if request.method == "GET":
		return render_template("cadastro_escola.html")
	else:
		escola = {}
		escola['nome'] = request.form['nome']
		escola['cidade'] = request.form['cidade']
		escola['gestor'] = request.form['gestor']
		escolas.insert_one(escola)
		lista_escolas = list(escolas.find({},{"_id": 0}))
		return render_template("escolas.html", lista_escolas = lista_escolas)

@app.route("/aluno/new", methods=["GET","POST"])
def new_aluno():
	if request.method == "GET":
		lista_escolas = list(escolas.find({}, {"_id": 0}))
		return render_template("cadastro_aluno.html", escolas = lista_escolas)
	
	else:
		aluno = {}
		aluno['nome'] = request.form['nome']
		aluno['idade'] = request.form['idade']
		aluno['escola'] = request.form['escola']
		alunos.insert_one(aluno)
		lista_alunos = list(alunos.find({}, {"_id": 0}))
		return render_template("alunos.html", lista_alunos = lista_alunos)

if __name__ == "__main__":
	app.run(debug=True)