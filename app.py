import os

import requests
from flask import Flask, abort, render_template, request

app = Flask(__name__)

API_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 5  # segundos


@app.route("/")
def home():
    search = request.args.get("search", "").strip()[:100]
    error = None
    posts = []

    try:
        response = requests.get(f"{API_URL}/posts", timeout=TIMEOUT)
        response.raise_for_status()
        posts = response.json()
    except requests.RequestException:
        error = "No pudimos obtener las publicaciones. Intentá de nuevo en unos segundos."

    if search:
        posts = [post for post in posts if search.lower() in post.get("title", "").lower()]

    return render_template("posts.html", posts=posts[:5], search=search, error=error)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    try:
        response = requests.get(f"{API_URL}/posts/{post_id}", timeout=TIMEOUT)
    except requests.RequestException:
        abort(503)

    if response.status_code == 404:
        abort(404)

    try:
        response.raise_for_status()
    except requests.HTTPError:
        abort(502)

    return render_template("post_detail.html", post=response.json())


if __name__ == "__main__":
    # El modo debug se habilita solo de forma explícita: FLASK_DEBUG=1.
    # Nunca lo actives en producción: el depurador de Werkzeug permite ejecutar código.
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
