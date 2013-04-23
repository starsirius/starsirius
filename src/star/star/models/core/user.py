from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import func
from star import db, app
from star.models import now

user_role = db.Table('user_role',
    db.Column('id', db.Integer, db.Sequence('user_role_seq_id', optional=True), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', deferrable=True, ondelete="CASCADE")),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id', deferrable=True, ondelete="CASCADE")),
    db.Column('created', db.DateTime, nullable=False, default=now),
    extend_existing=True)

class UserCredentials(db.Model):
    __tablename__ = 'usercred'
    id =            db.Column(db.Integer, db.Sequence('usercred_seq_id', optional=True), primary_key=True)
    _email =        db.Column('email', db.Unicode(100), nullable=False, index=True, unique=True)
    created =       db.Column(db.DateTime, nullable=False, default=now)
    last_updated =  db.Column(db.DateTime, nullable=False, default=now, onupdate=now)

    @hybrid_property
    def email(self):
        return self._email.lower()

    @email.setter
    def email(self, email):
        self._email = email.lower()

    @email.expression
    def email(cls):
        return func.lower(cls._email)

class UserPasswd(db.Model):
    __tablename__ = 'userpasswd'
    id =            db.Column(db.Integer, db.Sequence('userpasswd_seq_id', optional=True), primary_key=True)
    user_id =       db.Column(db.Integer, db.ForeignKey('user.id', deferrable=True, ondelete='CASCADE'), unique=True, nullable=False)
    password =      db.Column(db.UnicodeText, nullable=False) # This is a bcrypt hash
    created =       db.Column(db.DateTime, nullable=False, default=now)
    last_updated =  db.Column(db.DateTime, nullable=False, default=now, onupdate=now)

class User(db.Model):
    __tablename__ = 'user'
    id =                db.Column(db.Integer, db.Sequence('user_seq_id', optional=True), primary_key=True)
    usercred_id =       db.Column(db.Integer, db.ForeignKey('usercred.id', deferrable=True, ondelete='CASCADE'), unique=True, nullable=False)
    email =             db.relationship('UserCredentials', uselist=False, primaryjoin=UserCredentials.id==usercred_id)
    first_name =        db.Column(db.Unicode(149), nullable=False)
    last_name =         db.Column(db.Unicode(149), nullable=False)
    display_name =      db.Column(db.Unicode(149), nullable=False)
    phone_number =      db.Column(db.Unicode(40), nullable=True)
    image_url =         db.Column(db.Unicode(149), nullable=False, default=u"http://www.gravatar.com/avatar/HASH?d=identicon")
    roles =             db.relationship('Role', secondary=user_role, backref=db.backref('users', lazy='dynamic'))
    last_login =        db.Column(db.DateTime, nullable=False, default=now)
    created =           db.Column(db.DateTime, nullable=False, default=now)
    last_updated =      db.Column(db.DateTime, nullable=False, default=now, onupdate=now)

    @hybrid_property
    def full_name(self):
        return self.first_name.title() + ' ' + self.last_name.title()

class Role(db.Model):
    __tablename__ = 'role'
    id =         db.Column(db.Integer, db.Sequence('role_seq_id', optional=True), primary_key=True)
    role_name =  db.Column(db.Unicode(149), nullable=False, unique=True)
    created =    db.Column(db.DateTime, nullable=False, default=now)

