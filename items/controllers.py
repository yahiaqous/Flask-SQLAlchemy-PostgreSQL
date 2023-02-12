from flask import request, jsonify
import uuid

from .. import db
from .models import Item

# ----------------------------------------------- #

# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
  
def list_all_items_controller():
    items = Item.query.all()
    response = []
    for item in items: response.append(item.toDict()) 
    return jsonify(response)

def create_item_controller():
    request_form = request.form.to_dict()
    
    id = str(uuid.uuid4())
    new_item = Item( 
                    id           = id,
                    name         = request_form['name'],
                    price        = float(request_form['price']),
                    description  = request_form['description'],
                    image_link   = request_form['image_link'],
                    account_id   = request_form['account_id'],
                    )
    db.session.add(new_item)
    db.session.commit()
    
    response = Item.query.get(id).toDict()
    return jsonify(response)

def retrieve_item_controller(item_id):
    response = Item.query.get(item_id).toDict()
    return jsonify(response)

def update_item_controller(item_id):
    request_form = request.form.to_dict()
    item = Item.query.get(item_id)
    
    item.name        = request_form['name']
    item.price       = float(request_form['price'])
    item.description = request_form['description']
    item.image_link  = request_form['image_link']
    item.account_id  = request_form['account_id']
    db.session.commit()
    
    response = Item.query.get(item_id).toDict()
    return jsonify(response)
    
def delete_item_controller(item_id):
    Item.query.filter_by(id=item_id).delete()
    db.session.commit()
    
    return ('Item with Id "{}" deleted successfully!').format(item_id)
