# -*- coding: utf-8 -*-
import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker

print(u"SQLAlchemy version : " + sqla.__version__)

db = sqla.create_engine('sqlite:///CreativeCherry.db', echo=True)

print(u"DB utilisée : " + str(db.url))

def get_session():
    Session = sessionmaker(db)
    session = Session()
    return session

def safe_add(session, data):
    error = None
    out = None
    if not data:
        error = u"Missing data to add"
        return error
    
    try:
        session.add(data)
        session.commit()
        out = u"Commit OK"
    except IntegrityError as e:
        print(u"IntegrityError")
        error = str(e.orig)
        
    return out, error

def safe_model_instance_creator(model, params):
    out = None
    error = None
    
    try:
        out = model(**params)
    except AssertionError as e:
        print(u"AssertionError")
        error = e
        
    return out, error
