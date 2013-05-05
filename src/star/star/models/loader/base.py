from star import db
from star.models.core import taxonomy as taxonomy_model

def init_data():
    terms = [u"User Experience", u"Human-Computer Interaction", u"Heuristic Evaluation"]
    for term in terms:
        t = taxonomy_model.Term(name=term)
        t.slug = term.lower().replace(" ", "_")
        db.session.add(t)
        db.session.flush()
        db.session.commit()

    taxonomies = [u"tag", u"category"]
    for tax in taxonomies:
        t = taxonomy_model.Taxonomy(name=tax)
        db.session.add(t)
        db.session.flush()
        db.session.commit()

    term_ux = taxonomy_model.Term.query.filter_by(id=1).first()
    taxonomy_tag = taxonomy_model.Taxonomy.query.filter_by(id=1).first()
    tt = taxonomy_model.TaxonomyTerm(description=u"ux tag")
    tt.term_id = term_ux.id
    tt.taxonomy_id = taxonomy_tag.id
    db.session.add(tt)
    db.session.flush()
    db.session.commit()
    
    taxonomy_category = taxonomy_model.Taxonomy.query.filter_by(id=2).first()
    tt = taxonomy_model.TaxonomyTerm(description=u"ux category")
    tt.term_id = term_ux.id
    tt.taxonomy_id = taxonomy_category.id
    db.session.add(tt)
    db.session.flush()
    db.session.commit()