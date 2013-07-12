from star import db
from star.model.core import post as post_model

"""
This is the user data access layer.
It abstracts interactions with the data or model,
allowing business rules and interaction to feel more
natural, as well as mitigated possible human error
when performing data related operations.
"""

class PostPublicDAL(object):
    """
    The Post Public Data Access Layer and ORM helper functions.
    Here you'll find functions for common operations on the model
    and common operations to fetch objects from within the model.
    These methods are safe to publish to a public API (with RESTful access and interaction).
    """

    ###
    # READ
    ############

    @staticmethod
    def getPostByPostID(post_id):
        """
        Fetch a post mapper object given a post_id.
        Arguments:
            post_id - an int, the post_id number of the desired Post Object
        Returns:
            ret_post - a Post object, the post mapper object paired to the post_id
                        will return None if not found
        Raises:
            TypeError - if post_id is not an int
        """
        ret_post = PostPrivateDAL.getPostByPostID(post_id)
        return ret_post

    ###
    # CREATE
    ############

    ###
    # UPDATE
    ############

    ###
    # DELETE
    ############

class PostPrivateDAL(object):
    """
    The Post Private Data Access Layer and ORM helper functions.
    Here you'll find functions for common operations on the model and common
    operations to fetch objects from within the model.
    These methods will not be published out of the system.
    """

    ###
    # READ
    ############

    @staticmethod
    def getPostByPostID(post_id):
        """
        Fetch a post mapper object given a post_id.
        Arguments:
            post_id - an int, the post_id number of the desired Post Object
        Returns:
            ret_post - a Post object, the post mapper object paired to the post_id
                        will return None if not found
        Raises:
            TypeError - if post_id is not an int
        """
        if not isinstance(post_id, int):
            raise TypeError("post_id must be an int")
        post_query = post_model.Post.query
        ret_post = post_query.get(post_id)
        return ret_post

    ###
    # CREATE
    ############

    ###
    # UPDATE
    ############

    ###
    # DELETE
    ############

