from star import db
from star.models import now, db_add, db_remove
from star.models.core import user as user_model

"""
This is the user data access layer.
It abstracts interactions with the data or model,
allowing business rules and interaction to feel more
natural, as well as mitigated possible human error
when performing data related operations.
"""


class UserPublicDAL(object):
    """
    The User Public Data Access Layer and ORM helper functions.
    Here you'll find functions for common operations on the model
    and common operations to fetch objects from within the model.
    These methods are safe to publish to a public API (with RESTful access and interaction).
    """

    ###
    # READ
    ############

    @staticmethod
    def getUserByUserID(user_id):
        """
        Fetch a star user mapper object given a user_id.
        Arguments:
            user_id - an int, the user_id number of the desired starUser Object
        Returns:
            ret_user - a starUser object, the user mapper object paired to the user_id
                        will return None if not found
        Raises:
            TypeError - if user_id is not an int
        """
        ret_user = UserPrivateDAL.getUserByUserID(user_id)
        return ret_user


class UserPrivateDAL(object):
    """
    The User Private Data Access Layer and ORM helper functions.
    Here you'll find functions for common operations on the model and common
    operations to fetch objects from within the model.
    These methods will not be published out of the system.
    """

    ###
    # CREATE
    ############
    @staticmethod
    def createUserPassword(user_id, hashed_password):
        """
        Create a password for a given user_id
        Arguments:
            user_id - an int, the user's ID of the user who's password you want to set
            hashed_password - a unicode string, the password hash string, hashed with bcrypt
        Returns:
           user_pw - a UserPasswd object
        Notes:
            This does not check to see if user_id is a valid ID;
            A constraint exception will be thrown if it isn't (when the object is added to a DB session)
        """
        user_pw = user_model.UserPasswd()
        user_pw.user_id = user_id
        user_pw.password = hashed_password
        return user_pw

    @staticmethod
    def createUserCredentials(user_email):
        """
        Create and add a user's credentials (email) to the DB.
        Arguments:
            user_email - a unicode string, the email address of the user you wish to add
        Returns:
            usercred - a UserCredentials object,
                        None on failure
        Notes:
            There is no additional busines logic.
            A controller/call should check the following independenly:
                - is the email address valid?
                - does the email address already exist?
        """
        usercred = user_model.UserCredentials()
        usercred.email = user_email
        return usercred

    @staticmethod
    def createUser(usercred_id, first_name, last_name, image_url=None):
        """
        Create a User object
        Arguments:
            usercred_id - an int, the User's UserCredential ID (related to their email)
            first_name - a unicode string, the User's first name
            last_name - a unicode string, the User's last name
            [image_url] - a unicode string, the URL of the user's image picture (Usually a CDN URL) [None]
        Returns:
            user - a User object
        Notes:
            This does not check to see if usercred_id is a valid ID;
            A constraint exception will be thrown if it isn't (when the object is added to a DB session)
        See also:
            addUser - top-level call for creating and adding users to the DB (for use in controllers)
        """
        user = user_model.User()
        user.usercred_id = usercred_id
        user.first_name = first_name
        user.last_name = last_name
        user.display_name = first_name + " " + last_name[0] # for example: `Chung-Yi C`
        if image_url:
            user.image_url = image_url
        return user

    @staticmethod
    def addUser(email, hashed_password, first_name, last_name, image_url=None):
        """
        Create and add a User to the DB.  Also creates Email/Credential pairs.
        Arguments:
            email - a unicode string, the email address of the user you wish to add
            hashed_password - a unicode string, the password hash string, hashed with bcrypt
            first_name - a unicode string, the user's first name
            last_name - a unicode string, the user's last name
            [image_url] - a unicode string, the URL of the user's image picture (Usually a CDN URL) [None]
        Returns:
            user - a User, the newly created User
                    None on failure
        Notes:
            There is no additional business logic.
            A controller/call should check the following independenly:
                - is the email address valid?
                - does the email address already exist?
        """
        # Create the credentials
        usercred = UserPrivateDAL.createUserCredentials(email)
        db_add(usercred, commit=False)
        # Create the user, hooking the credentials in
        user = UserPrivateDAL.createUser(usercred.id, first_name, last_name, image_url)
        db_add(user, commit=False)
        # Tie the user to a password now
        user_passwd = UserPrivateDAL.createUserPassword(user.id, hashed_password)
        db_add(user_passwd, commit=False)
        db.session.commit()
        return user

    @staticmethod
    def createRole(role_name):
        """
        Create a new role - for authorization/permission
        Arguments:
            role_name - a string, the name of the Role you want to create (eg: admin, author, user)
        Returns:
            role - a Role object
        """
        role = user_model.Role()
        role.role_name = role_name
        return role

    @staticmethod
    def addRole(role_name):
        """
        Create a new role and add it to the DB for use System wide.
        These roles should also be replicated in the __init__ role dictionary.
        Arguments:
            role_name - a string, the name of the Role you want to create (eg: admin, author, user)
        Returns:
            role - a Role object, the freshly created and persisted role
        Notes:
            There is no additional business logic/sanity check to see if the role exists
            If it does, a unique constraint exception will be thrown
        """
        role = UserPrivateDAL.createRole(role_name)
        return db_add(role)

    @staticmethod
    def addRoleToUser(role, user):
        """
        Add a Role to a User
        Arguments:
            role - a Role object, the role you want to adorn the `user` with
            user - a User object, the user accepting a new role
        Returns:
            user - the User with the new role added.  (see: user.roles)
        """
        if role not in user.roles:
            user.roles.append(role)
            db.session.flush()
            db.session.commit()
        return user


    ###
    # READ
    ############

    @staticmethod
    def getUserByUserID(user_id):
        """
        Fetch a user mapper object given a user_id.
        Arguments:
            user_id - an int, the user_id number of the desired User Object
        Returns:
            ret_user - a User object, the user mapper object paired to the user_id
                        will return None if not found
        Raises:
            TypeError - if user_id is not an int
        """
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an int")
        user_query = user_model.User.query
        ret_user = user_query.get(user_id)
        return ret_user

    @staticmethod
    def getUserByUserCredID(usercred_id):
        """
        Fetch a user mapper object given a usercred_id.
        Arguments:
            usercred_id - an int, the user_id number of the desired User Object
        Returns:
            ret_user - a User object, the user mapper object paired to the usercred_id
                        will return None if not found
        Raises:
            TypeError - if usercred_id is not an int
        """
        if not isinstance(usercred_id, int):
            raise TypeError("usercred_id must be an int")
        user_query = user_model.User.query
        ret_user = user_query.filter(user_model.User.usercred_id==usercred_id).first()
        return ret_user

    @staticmethod
    def getUserByEmail(user_email):
        """
        Fetch a user mapper object given a user's email
        Arguments:
            user_email - a unicode string, the email of the desired User Object
        Returns:
            ret_user - a User object, the usermapper object paired to the email
                        will return None if not found
        """
        usercred_query = db.session.query(user_model.UserCredentials.id)
        user_cred_id = usercred_query.filter(user_model.UserCredentials.email==user_email).first()
        if user_cred_id:
            user_cred_id = user_cred_id[0]
            ret_user = UserPrivateDAL.getUserByUserCredID(user_cred_id)
            return ret_user
        return None

    @staticmethod
    def getRoleByRoleID(role_id):
        """
        Fetch a role mapper object given a role_id.
        Arguments:
            role_id - an int, the role_id number of the desired Role Object
        Returns:
            ret_role - a Role object, the role mapper object paired to the role_id 
                        will return None if not found
        Raises:
            TypeError - if role_id is not an int
        """
        if not isinstance(role_id, int):
            raise TypeError("role_id must be an int")
        role_query = user_model.Role.query
        ret_role = role_query.get(role_id)
        return ret_role

    @staticmethod
    def getRoleByRoleName(role_name):
        """
        Fetch a role mapper object given a role's name
        Arguments:
            role_name - a unicode string, the name of the desired Role Object
        Returns:
            ret_role - a Role object, the role mapper object paired to the role name
                        will return None if not found
        """
        role_query = user_model.Role.query
        ret_role = role_query.filter(user_model.Role.role_name==role_name).first()
        return ret_role
