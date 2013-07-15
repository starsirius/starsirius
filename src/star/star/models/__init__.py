from star import db
import datetime

now = datetime.datetime.now

def db_add(obj, commit=True):
    db.session.add(obj)
    db.session.flush()
    if commit:
        db.session.commit()
    return obj

def db_remove(obj, commit=True):
    db.session.delete(obj)
    db.session.flush()
    if commit:
        db.session.commit()
    return True
