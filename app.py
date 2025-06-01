from flask import Flask, render_template, request, abort
import requests

app = Flask(__name__)

@app.route('/')
def home():
    search = request.args.get('search', '')  # Captura texto del input de búsqueda
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    if search:
        # Filtra posts que contienen la palabra buscada (sin importar mayúsculas/minúsculas)
        posts = [post for post in posts if search.lower() in post['title'].lower()]

    return render_template('posts.html', posts=posts[:5], search=search)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    if response.status_code == 404:
        abort(404)
    post = response.json()
    return render_template('post_detail.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)