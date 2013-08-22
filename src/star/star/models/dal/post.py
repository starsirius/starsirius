from star import db
from star.models import db_add
from star.models.core import post as post_model
from slugify import slugify

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

    @staticmethod
    def getWorkByWorkID(work_id):
        """
        """
        ret_work = PostPrivateDAL.getWorkByWorkID(work_id)
        return ret_work

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

    @staticmethod
    def getWorkByWorkID(work_id):
        """
        """
        if not isinstance(work_id, int):
            raise TypeError("work_id must be an int")
        work_query = post_model.Work.query
        ret_work = work_query.get(work_id)
        return ret_work
                    
    @staticmethod
    def getWorks(offset=0, limit=9):
        """
        Get a list of works
        Arguments:
            [offset] - an int, the offset of the works [0]
            [limit] - an int, the limit of how many works to fetch, None to fetch ALL WORKS [9]
        Returns:
            ret_works - a list of Works objects, the works in the system
        """
        work_query = post_model.Work.query
        ret_works = work_query.order_by(db.desc(post_model.Work.id)).offset(offset).limit(limit).all()
        return ret_works

    ###
    # CREATE
    ############

    @staticmethod
    def createPost(author_id, title, excerpt, content, status, comment_status, password):
        """
        """
        post = post_model.Post()
        post.author_id = author_id
        post.title = title
        post.excerpt = excerpt
        post.content = content
        post.status = status
        post.comment_status = comment_status
        post.password = password
        post.slug = slugify(title)
        return post

    @staticmethod
    def addPost(author_id, title, excerpt, content, status, comment_status, password):
        """
        """
        post = PostPrivateDAL.createPost(author_id, title, excerpt, content, status, comment_status, password)
        return db_add(post)

    @staticmethod
    def createWork(post_id, subtitle, summary, cover_image_url=None, meta_data=None):
        work = post_model.Work()
        work.post_id = post_id
        work.subtitle = subtitle
        work.summary = summary
        work.cover_image_url = cover_image_url
        work.meta_data = meta_data
        return work

    @staticmethod
    def addWork(post_id, subtitle, summary, cover_image_url=None, meta_data=None):
        """
        """
        work = PostPrivateDAL.createWork(post_id, subtitle, summary, cover_image_url, meta_data)
        return db_add(work)

    @staticmethod
    def addTaxonomyTermToPost(post_id_or_obj, taxonomy_term):
        """
        Add a taxonomy_term to a post
        Arguments:
            post_id_or_obj - a Post or int, the Post or ID of the post
            taxonomy_term - a Taxonomy_Term object, the taxonomy_term you're adding to a post
        Returns:
            taxonomy_term - the taxonomy_term successfully added to the post
                                None if unsuccessful
        Notes:
            If DB commit fails, this will throw an exception
        """
        post = isinstance(post_id_or_obj, post_model.Post) and post_id_or_obj or PostPrivateDAL.getPostByPostID(post_id_or_obj)
        if not post:
            return None
        post.taxonomy_terms.append(taxonomy_term)
        db.session.flush()
        db.session.commit()
        return taxonomy_term

    ###
    # UPDATE
    ############

    ###
    # DELETE
    ############

