from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Item, Customer, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

@app.route('/items')
def items():
    items_dict = [item.to_dict() for item in Item.query.all()]
    response = make_response(items_dict, 200)
    return response

@app.route('/customers')
def customers():
    customers_dict = [customer.to_dict() for customer in Customer.query.all()]
    response = make_response(customers_dict, 200)
    return response

@app.route('/reviews')
def reviews():
    reviews_dict = [review.to_dict() for review in Review.query.all()]
    response = make_response(reviews_dict, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
