from star import db
from star.models import now
from star.models.core.user import User

class Comment(db.Model):
    __tablename__ = 'comment'
    id =            db.Column(db.Integer, db.Sequence('comment_seq_id', optional=True), primary_key=True)
    post_id =       db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    author_name =   db.Column(db.Unicode(100), nullable=False)
    author_email =  db.Column(db.Unicode(100), nullable=False)
    author_url =    db.Column(db.Unicode(200), nullable=False)
    author_ip =     db.Column(db.Unicode(100), nullable=False)
    content =       db.Column(db.Unicode(10000), nullable=False)
    approved =      db.Column(db.Boolean, nullable=False, default=True)
    karma =         db.Column(db.Integer, nullable=False, default=0)
    agent =         db.Column(db.Unicode(255), nullable=False)
    type =          db.Column(db.Unicode(20), nullable=False)
    parent_id =     db.Column(db.Integer, db.ForeignKey('comment.id', deferrable=True, ondelete='CASCADE'))
    children =      db.relationship('Comment', backref=db.backref('parent', remote_side=[id], passive_deletes=True))
    user_id =       db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user =          db.relationship('User', backref=db.backref('comments', passive_deletes=True))
    created =       db.Column(db.DateTime, nullable=False, default=now)
