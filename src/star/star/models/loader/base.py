from star import db
from star.models.dal.user import UserPrivateDAL
from star.models.dal.taxonomy import TaxonomyPrivateDAL
from star.models.dal.post import PostPrivateDAL
from star.models.core import taxonomy as taxonomy_model
from star import flask_bcrypt

def init_data():

    ###
    # RESET DB
    ############
    db.drop_all()
    db.create_all()

    ###
    # USER
    ############
    user = UserPrivateDAL.addUser(
            u"cychi1210@gmail.com", 
            flask_bcrypt.generate_password_hash(u"password"), 
            u"Chung-Yi", 
            u"Chi")
    role = UserPrivateDAL.addRole(u"admin")
    UserPrivateDAL.addRoleToUser(role, user)

    ###
    # TAXONOMY
    ############
    tax_tag = TaxonomyPrivateDAL.addTaxonomy(u'tag')
    tax_cat = TaxonomyPrivateDAL.addTaxonomy(u'category')

    ###
    # POST
    ############
    title = u"Post Title"
    post = PostPrivateDAL.addPost(
            user.id, 
            title, 
            u"Post excerpt", 
            u"Post content", 
            u"published", 
            u"allowed", 
            flask_bcrypt.generate_password_hash(u"password"), 
            u"-".join(title.split()))

    term_art = TaxonomyPrivateDAL.addTerm(u'Art')
    term_life = TaxonomyPrivateDAL.addTerm(u'life')
    TaxonomyPrivateDAL.addTermToTaxonomy(term_art, tax_tag)
    TaxonomyPrivateDAL.addTermToTaxonomy(term_life, tax_tag)
    TaxonomyPrivateDAL.addTermToTaxonomy(term_life, tax_cat)

    PostPrivateDAL.addTaxonomyTermToPost(
            post,
            TaxonomyPrivateDAL.getTaxonomyTermByTaxonomyIDAndTermID(
                tax_tag.id, term_art.id))
    PostPrivateDAL.addTaxonomyTermToPost(
            post,
            TaxonomyPrivateDAL.getTaxonomyTermByTaxonomyIDAndTermID(
                tax_tag.id, term_life.id))
    PostPrivateDAL.addTaxonomyTermToPost(
            post,
            TaxonomyPrivateDAL.getTaxonomyTermByTaxonomyIDAndTermID(
                tax_cat.id, term_life.id))

    ###
    # Work
    ############
    work = PostPrivateDAL.addWork(
            post.id, 
            u"Post Subtitle", 
            u"Post summary")

"""
def init_data():
    db.drop_all()
    db.create_all()

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

    #tax_tag = taxonomy_model.Taxonomy.query.filter_by(id=1).first()
    #db.session.delete(tax_tag)
    #db.session.commit()

    term_tag = taxonomy_model.Term.query.filter_by(id=1).first()
    db.session.delete(term_tag)
    db.session.commit()
"""
