from flask import Flask, session, redirect


@app.route("/")
def index():
	if 'username' in session:
		
