from sqlalchemy import inspect
from datetime import datetime
from flask_validator import ValidateString, ValidateNumber, ValidateURL
from sqlalchemy.orm import validates

from .. import db  # from __init__.py

# ----------------------------------------------- #

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Item(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation 
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update
    
# Input by User Fields:
    name         = db.Column(db.String(50), nullable=False)
    price        = db.Column(db.Float(precision=2), nullable=False, default=0.00)
    description  = db.Column(db.Text())
    image_link   = db.Column(db.String(1000), nullable=False)

# Relations: SQLAlchemy Basic Relationship Patterns => https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    account    = db.relationship("Account", back_populates="items")
    account_id = db.Column(db.String(100), db.ForeignKey("account.id"))


# Validations => https://flask-validator.readthedocs.io/en/latest/index.html
    @classmethod
    def __declare_last__(cls):
        ValidateString(Item.name, False, True, "The name type must be string")
        ValidateNumber(Item.price, True, "The price type must be number")
        ValidateURL(Item.image_link, True, True, "The image link is not valid")

# Set an empty string to null for name field => https://stackoverflow.com/a/57294872
    @validates('name')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '': return None
        else: return value
    
    
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self): 
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.email
