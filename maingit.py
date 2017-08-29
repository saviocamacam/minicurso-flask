from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/perfil/<string:username>")
def profile(username):
	token = "?access_token=84f891bd9791a7bb6645ab90b8ade08dac8531da"
	url = "https://api.github.com/users/" + username + token
	r = requests.get(url)
	
	if r.status_code == 200:
		url_repos = r.json()['repos_url'] + token
		repos = requests.get(url_repos).json()
		return render_template("profile.html", usuario=r.json(), repos=repos)
	else:
		return abort(404)

if __name__ == "__main__":
	app.run(debug=True)