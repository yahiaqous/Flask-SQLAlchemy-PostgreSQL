import os
from flask import request

# App Initialization
from . import create_app # from __init__ file
app = create_app(os.getenv("CONFIG_MODE")) 

from .src.accounts.controllers import list_all_accounts_controller, create_account_controller, retrieve_account_controller, update_account_controller, delete_account_controller

# ----------------------------------------------- #

# Routes:
# Hello World!
@app.route('/')
def hello():
    return "Hello World!"

# Accounts:
@app.route("/accounts", methods=['GET', 'POST'])
def list_create_accounts():
    if request.method == 'GET': return list_all_accounts_controller()
    if request.method == 'POST': return create_account_controller()
    else: return 'Method is Not Allowed'

@app.route("/accounts/<account_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_accounts(account_id):
    if request.method == 'GET': return retrieve_account_controller(account_id)
    if request.method == 'PUT': return update_account_controller(account_id)
    if request.method == 'DELETE': return delete_account_controller(account_id)
    else: return 'Method is Not Allowed'
    
# ----------------------------------------------- #

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()