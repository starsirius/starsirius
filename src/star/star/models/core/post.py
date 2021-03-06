from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import func
from star import db, app
from star.models import now
from star.models.core.user import User
from star.models.core.comment import Comment
from star.models.core.taxonomy import TaxonomyTerm

post_taxonomy_term = db.Table('post_taxonomy_term',
    db.Column('id', db.Integer, db.Sequence('post_taxonomy_term_seq_id', optional=True), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id', deferrable=True, ondelete="CASCADE")),
    #db.Column('taxonomy_term_id', db.Integer, db.ForeignKey('taxonomy_term.id', deferrable=True, ondelete="CASCADE")),
    db.Column('term_id', db.Integer, nullable=False), 
    db.Column('taxonomy_id', db.Integer, nullable=False), 
    db.ForeignKeyConstraint(['term_id', 'taxonomy_id'], ['taxonomy_term.term_id', 'taxonomy_term.taxonomy_id'] ), 
    db.Column('created', db.DateTime, nullable=False, default=now), 
    extend_existing=True)

class Post(db.Model):
    __tablename__ = 'post'
    id =                db.Column(db.Integer, db.Sequence('post_seq_id', optional=True), primary_key=True)
    author_id =         db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    author =            db.relationship('User', uselist=False, passive_deletes=True)
    title =             db.Column(db.Unicode(250), nullable=False)
    excerpt =           db.Column(db.Unicode(5000), nullable=False)
    content =           db.Column(db.Unicode(10000), nullable=False)
    status =            db.Column(db.Unicode(20), nullable=False, default=u"publish")
    comment_status =    db.Column(db.Unicode(20), nullable=False, default=u"open")
    password =          db.Column(db.UnicodeText, nullable=False) # This is a bcrypt hash
    slug =              db.Column(db.Unicode(250), nullable=False)
    comments =          db.relationship('Comment', backref='post', lazy='dynamic')
    taxonomy_terms =    db.relationship('TaxonomyTerm', secondary=post_taxonomy_term, backref=db.backref('posts'))
    created =           db.Column(db.DateTime, nullable=False, default=now)
    published =         db.Column(db.DateTime, nullable=False, default=now)
    last_updated =      db.Column(db.DateTime, nullable=False, default=now, onupdate=now)

class Work(db.Model):
    __tablename__ = 'work'
    id =                db.Column(db.Integer, db.Sequence('work_seq_id', optional=True), primary_key=True)
    post_id =           db.Column(db.Integer, db.ForeignKey('post.id', deferrable=True, ondelete='CASCADE'), unique=True, nullable=False) # with unique=True, a post can only have one work
    post =              db.relationship('Post', uselist=False, primaryjoin=Post.id==post_id, backref=db.backref('work', uselist=False))
    subtitle =          db.Column(db.Unicode(250), nullable=False)
    summary =           db.Column(db.Unicode(5000), nullable=False)
    cover_image_url =   db.Column(db.Unicode(149), nullable=False, default=u"http://www.gravatar.com/avatar/HASH?d=identicon")
    meta_data =         db.Column(db.UnicodeText, nullable=True)
    created =           db.Column(db.DateTime, nullable=False, default=now)
    published =         db.Column(db.DateTime, nullable=False, default=now)
    last_updated =      db.Column(db.DateTime, nullable=False, default=now, onupdate=now)
