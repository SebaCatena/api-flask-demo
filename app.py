from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    return render_template('posts.html', posts=posts[:5])

if __name__ == '__main__':
    app.run(debug=True)