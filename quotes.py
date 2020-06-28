from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Abhi77#@@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gwzmlucxivtagn:16274c611686d4e5e3cb86fbf18d95a2338e04eaee5037bcdb98a274997473c3@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d5r5sse57p17c0'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result= Favquotes.query.all()
	return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
	return render_template('quotes.html')


@app.route('/process', methods = ['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata=Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()
	return redirect(url_for('index'))