# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# model the class after the table from our database
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('emails_schema').query_db(query)
        # Create an empty list to append our instances of table
        emails = []
        # Iterate over the db results and create instances of table with cls.
        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());'
        return connectToMySQL('emails_schema').query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['email']) == 0:
            flash("Please enter an email address!")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Please enter a valid email address!")
            is_valid = False
        return is_valid
