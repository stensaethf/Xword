#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''DataSource - the interface class with the methods for accessing
our database.

By Sabastian Mugazambi and Fredrik Roenn Stensaeth; 2015'''

import psycopg2
import os.path

class DataSource:
    """
    The DataSource class functions as an interface for accessing the database.
    Methods:
    - getAdjectivesListForWord(word)
    - getVerbsListForWord(word)
    - getAdverbsListForWord(word)
    - getNounsListForWord(word)
    -getDefinitionsListForWord(word)
    """

    def __init__(self):
        """
        Constructor for the DataSource database interface class. Nothing
        will be set up here, besides the connection to the database.
        """

        USERNAME = 'mugazambis'
        DB_NAME = 'mugazambis'

        # self.cursor = None

        # Step 1: Read your password from the secure file.
        try:
            f = open(os.path.join('/cs257', USERNAME))
            PASSWORD = f.read().strip()
            f.close()
            # PASSWORD = 'tiger474desktop'
        except:
            self.cursor = None

        # Might need to un-nest this try-except.
        try:
            db_connection = psycopg2.connect(user=USERNAME, 
                                             database=DB_NAME, 
                                             password=PASSWORD)
            self.cursor = db_connection.cursor()
            # Might need to un-nest this try-except.
            # try:
            #     self.cursor = db_connection.cursor()
            # except:
            #     self.cursor = 1
        except:
            self.cursor = None
    
    def getAdjectivesListForWord(self, word):
        """
        Returns a list of the Adjectives associated with the word.
        The adjectives are strings.
        """
        if self.cursor == None:
            return []

        self.cursor.execute(
            "SELECT * FROM associations WHERE word = %s;", (word,))

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

        self.cursor.execute(
            "SELECT * FROM associations WHERE word = %s;", (word,))

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

        self.cursor.execute(
            "SELECT * FROM associations WHERE word = %s;", (word,))
 
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
        self.cursor.execute(command)

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

        self.cursor.execute(
            "SELECT * FROM associations WHERE word = %s;", (word,))

        definitions_raw = ""
        for i in self.cursor:
            definitions_raw = i[1]

        definitions_list = definitions_raw.split(" ,, ")
        
        return definitions_list
        








