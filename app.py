import os
from flask import request

# App Initialization
from . import create_app # from __init__ file
app = create_app(os.getenv("CONFIG_MODE")) 

from .src.items.controllers import list_all_items_controller, create_item_controller, retrieve_item_controller, update_item_controller, delete_item_controller

# ----------------------------------------------- #

# Hello World!
@app.route('/')
def hello():
    return "Hello World!"

# Applications Routes
from .src.accounts import urls

# Items:
@app.route("/items", methods=['GET', 'POST'])
def list_create_items():
    if request.method == 'GET': return list_all_items_controller()
    if request.method == 'POST': return create_item_controller()
    else: return 'Method is Not Allowed'
    
@app.route("/items/<item_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_items(item_id):
    if request.method == 'GET': return retrieve_item_controller(item_id)
    if request.method == 'PUT': return update_item_controller(item_id)
    if request.method == 'DELETE': return delete_item_controller(item_id)
    else: return 'Method is Not Allowed'
    
# ----------------------------------------------- #

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()