from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request, Response

class Article :
    def __init__(self, body):
        self.body = body
        self.id = Article.id
        Article.id+=1

    def to_dict(self):
        return {
            'id': self.id, 
            'body': self.body
        }
    body = ''
    id = 0
app = Flask(__name__)

CORS(app)

articles = list()
articles.append(Article('ficel')) 
articles.append(Article('ryx'))

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

@app.post('/articles')
def insert_article():
    articles.append(
        Article(
            request.args['body']
        )
    )
    return Response("{}", status=200, mimetype='application/json')

@app.put('/articles')
def update_article():
    for article in articles:
        if article.id == int(request.args['id']):
            article.body = request.args['body']
            return Response("{}", status=200, mimetype='application/json')
    return Response("{}", status=404, mimetype='application/json')

@app.delete('/articles/<int:id>')
def delete_articel_by_id(id):
    for article in articles:
        if article.id == id:
            articles.remove(article)
            return Response("{}", status=200, mimetype='application/json')
    return Response("{}", status=404, mimetype='application/json')

