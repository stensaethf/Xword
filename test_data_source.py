#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''DataSource - the interface class with the methods for accessing
our database.

By Sabastian Mugazambi and Fredrik Roenn Stensaeth; 2015'''

# NOTE:
# All information will be in strings in the database. When retrieving info from
# the database a split on " ,, " (<space>,,<space>) needs to be performed.

# [word, definition, nouns, adverbs, verbs, adjectives]

import psycopg2

class DataSourceTest:
    def __init__(self):
        """
        Constructor for the DataSource database interface class. Nothing
        will be set up here, besides the connection to the database.
        """

        USERNAME = 'mugazambis'
        DB_NAME = 'mugazambis'
        PASSWORD = 'tiger474desktop' # just for testing purposes.

        # Might need to un-nest this try-except.
        try:
            db_connection = psycopg2.connect(user=USERNAME, database=DB_NAME, password=PASSWORD)
            self.cursor = db_connection.cursor()
        except:
            self.cursor = None
    
    def getAdjectivesListForWord(self, word):
        """
        Returns a list of the Adjectives associated with the word.
        The adjectives are strings.
        """
        if self.cursor == None:
            return []

        self.cursor.execute("SELECT * FROM associations WHERE word = %s;", (word,))

        adjectives_raw = ""
        for i in self.cursor:
            adjectives_raw = i[5]

        adjectives_list = adjectives_raw.split(" ,, ")

        return adjectives_list
    
    def getVerbsListForWord(self, word):
        """
        Returns a list of the Verbs associated with the word.
        The verbs are strings.
        """
        if self.cursor == None:
            return []

        self.cursor.execute("SELECT * FROM associations WHERE word = %s;", (word,)) # d

        verbs_raw = ""
        for i in self.cursor:
            verbs_raw = i[4]

        verbs_list = verbs_raw.split(" ,, ")
        
        return verbs_list
        
    def getAdverbsListForWord(self, word):
        """
        Returns a list of the Adverbs associated with the word.
        The adverbs are strings.
        """
        if self.cursor == None:
            return []

        self.cursor.execute("SELECT * FROM associations WHERE word = %s;", (word,)) # d
 
        adverbs_raw = ""
        for i in self.cursor:
            adverbs_raw = i[3]

        adverbs_list = adverbs_raw.split(" ,, ")
        
        return adverbs_list
        
    def getNounsListForWord(self, word):
        """
        Returns a list of the Nouns associated with the word. 
        The nouns are strings.
        """
        if self.cursor == None:
            return []

        command = "SELECT * FROM associations WHERE word = \'" + word + "\'"
        self.cursor.execute(command) # d

        nouns_raw = ""
        for i in self.cursor:
            nouns_raw = i[2]

        nouns_list = nouns_raw.split(" ,, ")
        
        return nouns_list
            
    def getDefinitionsListForWord(self, word):
        """
        Returns a list of the definitions of the word (there can be multiple
        definitions). The definitions are strings.
        """
        if self.cursor == None:
            return []

        self.cursor.execute("SELECT * FROM associations WHERE word = %s;", (word,)) # d

        definitions_raw = ""
        for i in self.cursor:
            definitions_raw = i[1]

        definitions_list = definitions_raw.split(" ,, ")
        
        return definitions_list
    

def getAssociatedWords(type_category, word):
    """
    Returns a list of asssociated words belonging to a category for a given 
    word.
    """
    list_of_words = []
    db = DataSourceTest()

    if db.cursor == None:
        return ["Database error"]

    if word == "":
        return []

    if type_category == "Noun":
        list_of_words = db.getNounsListForWord(word)
    elif type_category == "Adjective":
        list_of_words = db.getAdjectivesListForWord(word)
    elif type_category == "Verb":
        list_of_words = db.getVerbsListForWord(word)
    elif type_category == "Adverb":
        list_of_words = db.getAdverbsListForWord(word)
    elif type_category == "Definition":
        list_of_words = db.getDefinitionsListForWord(word)
    else:
        # this will in reality never happen due to the build of the script.
        # however, we cover it for safety reasons.
        return ["Invalid category"]

    return list_of_words



