<<<<<<< HEAD
from flask import Flask
from flask_cors import CORS
=======
from flask import Flask, jsonify
>>>>>>> 231193f1538202c91124429afc6d56e4915d15ee

class Article :
    def __init__(self, body, id):
        self.body = body
        self.id = id
    def to_dict(self):
        return {
            'id': self.id, 
            'body': self.body
        }
    body = ''
    id = 0
app = Flask(__name__)
<<<<<<< HEAD
CORS(app)
=======
articles = list()
articles.append(Article('ficel', 0)) 
articles.append(Article('ryx', 1))
>>>>>>> 231193f1538202c91124429afc6d56e4915d15ee

@app.route('/trump')
def hello():
    return 'Hello, World!'

@app.get('/articles')
def get_articles():
    return jsonify([article.to_dict() for article in articles])

@app.get('/articles/<int:id>')
def get_article_by_id(id):
    for article in articles:
        if article.id == id:
            return jsonify(article.to_dict())
