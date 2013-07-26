from star import db
from star.models import now

class Term(db.Model):
    """
    The basic information about a single term. It's not meaningful without context. 
    """
    __tablename__ = 'term'
    id =            db.Column(db.Integer, db.Sequence('term_seq_id', optional=True), primary_key=True)
    name =          db.Column(db.Unicode(149), nullable=False, unique=True)
    slug =          db.Column(db.Unicode(149), nullable=False, unique=True)
    created =       db.Column(db.DateTime, nullable=False, default=now)

class TaxonomyTerm(db.Model):
    """
    A term is not a category or tag on its own. It must be given context via the taxonomy.
    """
    __tablename__ = 'taxonomy_term'
    term_id =       db.Column(db.Integer, db.ForeignKey('term.id', ondelete='CASCADE'), primary_key=True)
    taxonomy_id =   db.Column(db.Integer, db.ForeignKey('taxonomy.id', ondelete='CASCADE'), primary_key=True)
    term =          db.relationship('Term', backref=db.backref("taxonomy_term", passive_deletes=True))
    description =   db.Column(db.Unicode(10000), nullable=False)
    parent =        db.Column(db.Integer, nullable=False, default=0)
    created =       db.Column(db.DateTime, nullable=False, default=now)

class Taxonomy(db.Model):
    """
    A taxonomy is a way to group posts together, e.g. "tag" and "category".
    """
    __tablename__ = 'taxonomy'
    id =        db.Column(db.Integer, db.Sequence('taxonomy_seq_id', optional=True), primary_key=True)
    name =      db.Column(db.Unicode(149), nullable=False, unique=True)
    terms =     db.relationship('TaxonomyTerm', backref="taxonomy", passive_deletes=True)
    created =   db.Column(db.DateTime, nullable=False, default=now)
