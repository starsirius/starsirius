from star import db
from star.models import db_add
from star.model.core import taxonomy as taxonomy_model

"""
This is the user data access layer.
It abstracts interactions with the data or model,
allowing business rules and interaction to feel more
natural, as well as mitigated possible human error
when performing data related operations.
"""

class TaxonomyPublicDAL(object):
    """
    The Taxonomy Public Data Access Layer and ORM helper functions.
    Here you'll find functions for common operations on the model
    and common operations to fetch objects from within the model.
    These methods are safe to publish to a public API (with RESTful access and interaction).
    """

    ###
    # READ
    ############

    ###
    # CREATE
    ############

    ###
    # UPDATE
    ############

    ###
    # DELETE
    ############

class TaxonomyPrivateDAL(object):
    """
    The Taxonomy Private Data Access Layer and ORM helper functions.
    Here you'll find functions for common operations on the model and common
    operations to fetch objects from within the model.
    These methods will not be published out of the system.
    """

    ###
    # READ
    ############

    @staticmethod
    def getTermByTermID(term_id):
        """
        Fetch a term mapper object given a term_id.
        Arguments:
            term_id - an int, the term_id number of the desired Term Object
        Returns:
            ret_term - a Term object, the term mapper object paired to the term_id 
                        will return None if not found
        Raises:
            TypeError - if term_id is not an int
        """
        if not isinstance(term_id, int):
            raise TypeError("term_id must be an int")
        term_query = term_model.Term.query
        ret_term = term_query.get(term_id)
        return ret_term

    @staticmethod
    def getTaxonomyByTaxonomyID(taxonomy_id):
        """
        Fetch a taxonomy mapper object given a taxonomy_id.
        Arguments:
            taxonomy_id - an int, the taxonomy_id number of the desired Taxonomy Object
        Returns:
            ret_taxonomy - a Taxonomy object, the taxonomy mapper object paired to the taxonomy_id 
                        will return None if not found
        Raises:
            TypeError - if taxonomy_id is not an int
        """
        if not isinstance(taxonomy_id, int):
            raise TypeError("taxonomy_id must be an int")
        taxonomy_query = taxonomy_model.Taxonomy.query
        ret_taxonomy = taxonomy_query.get(taxonomy_id)
        return ret_taxonomy

    @staticmethod
    def getTaxonomyTermByTaxonomyIDAndTermID(taxonomy_id, term_id):
        """
        Fetch a taxonomy_term mapper object given a taxonomy_id and term_id.
        Arguments:
            taxonomy_id - an int, the taxonomy_id number of the desired Taxonomy Object
            term_id - an int, the term_id number of the desired Term Object
        Returns:
            ret_taxonomy_term - a TaxonomyTerm object, the taxonomy_term mapper object paired to the taxonomy_id and term_id
                        will return None if not found
        Raises:
            TypeError - if taxonomy_id or term_id is not an int
        """
        if not isinstance(taxonomy_id, int):
            raise TypeError("taxonomy_id must be an int")
        if not isinstance(term_id, int):
            raise TypeError("term_id must be an int")
        taxonomy_term_query = taxonomy_model.TaxonomyTerm.query
        ret_taxonomy_term = taxonomy_term_query.get((term_id, taxonomy_id))
        return ret_taxonomy_term

    ###
    # CREATE
    ############

    @staticmethod
    def createTerm(name):
        """
        """
        term = taxonomy_model.Term()
        term.name = name
        term.slug = "-".join(name.split())
        return term

    @staticmethod
    def addTerm(name):
        """
        """
        term = TaxonomyPrivateDAL.createTerm(name)
        return db_add(term)

    ###
    # UPDATE
    ############

    ###
    # DELETE
    ############
