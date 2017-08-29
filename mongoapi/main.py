import json

from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

biblioteca = MongoClient().biblioteca
livros = biblioteca.livros

@app.route("/livros/todos")
def listar_todos():
	l = list(livros.find({}, {"_id":0}))
	return json.dumps(l)

@app.route("/livros/add/<string:titulo>/<string:autor>")
def add_livro(titulo,autor):
	l = {}
	l['titulo'] = titulo
	l['autor'] = autor
	livros.insert_one(l)
	return redirect("/livros/todos")

@app.route("/livros/deletar/todos")
def delete_todo():
	livros.delete_many({})
	return redirect("/livros/todos")

@app.route("/livros/del/<string:titulo>")
def deletar_livro(titulo):
	livros.delete_many({"titulo": titulo})
	return redirect("/livros/todos")

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)