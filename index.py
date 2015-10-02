#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A web application that returns to the user the words associated with a 
searched word.

The program does one of two things, depending on its CGI parameters.

1. Returns the associated words in their vocabulary classes.

2. Allows user to search a new word from any page.

It's structured to separate out the front-end presentation (stored in
template.html) from the logical components of the application.

By Frederik Roenn Stensaeth and Sabastian Nyasha Mugazambi, 2015;
"""
# print 'Content-type: text/html\r\n\r\n'
# print '<html><head></head><body>'
# import cgitb
# cgitb.enable()

import sys
import cgi
from data_source import *

def main():
    """
    The main() method of the web application. Main is comprised of the logic
    that chooses what should happen next.
    Returns nothing.
    """
    parameters = getCgiParameters()

    # About page
    if 'about' in parameters:
        printPageWithNoReplacements('about.html')
    # Information page
    elif (('search_field' in parameters) 
        and (('NOUNS' in parameters) 
            or ('VERBS' in parameters) 
            or ('ALL' in parameters) 
            or ('ADJECTIVES' in parameters) 
            or ('ADVERBS' in parameters) 
            or ('DEFINITION' in parameters))):
        parameters['search_field'] = parameters['search_field']
        printInfoPage(parameters, 'templateHTML.html')
    # Categories and filter page
    elif 'search_field' in parameters:
        printCategoriesAndFilterPage(parameters['search_field'], 
                                     'categoriesTemplate.html')
    # Home page
    else:
        printPageWithNoReplacements('index.html')

def printPageWithNoReplacements(template_filename):
    """
    Prints the html file given without doing any replacement formats.
    """
    try:
        f = open(template_filename)
        template_text = f.read()
        f.close()
    except Exception, e:
        template_text = "Cannot read template file <tt>%s</tt>." % (
            template_filename)

    # And finally print it to standard output, which is the CGI way of
    # communicating content back to the web server.
    print 'Content-type: text/html\r\n\r\n',
    print template_text


def printInfoPage(parameters, template_filename):
    """
    Prints the html file given after having found the words that the user
    requested and filtered them according to the requrest of the user.
    """

    grey_out_box = ''
    keep_js = ''
    catkeep_js = ''
    # Reads in the necessary files: html template and javascript files.
    try:
        f = open(template_filename)
        template_text = f.read()
        f.close()
        f = open('grey_out_box.js')
        grey_out_box = f.read()
        f.close()

        f = open('keep.js')
        keep_js = f.read()
        f.close()
        f = open('catkeep.js')
        catkeep_js = f.read()
        f.close()
    except Exception, e:
        template_text = "Cannot read template file <tt>%s</tt>." % (
            template_filename)

    # This will be our dictionary of values to plug into the template file.
    # For each "{foo}" directive in the template, we'll need a key 
    # called "foo".
    replacements = {}
    replacements['search_field'] = parameters['search_field']
    replacements['grey_out_box'] = grey_out_box
    replacements['keep_js'] = keep_js
    replacements['catkeep_js'] = catkeep_js

    # Creates lists to store associative words in later.
    word_list_nouns = []
    word_list_verbs = []
    word_list_adjectives = []
    word_list_adverbs = []
    word_list_definition = []

    # Depending on what categories were in the paremeters we need to find
    # the words associated with the given word for each of those categories.
    # Only update the lists for the categories chosen.
    if ('NOUNS' in parameters):
        word_list_nouns = getAssociatedWords('Noun', 
                                                parameters['search_field'])
    if ('ADJECTIVES' in parameters):
        word_list_adjectives = getAssociatedWords('Adjective', 
                                                  parameters['search_field'])
    if ('VERBS' in parameters):
        word_list_verbs = getAssociatedWords('Verb', 
                                             parameters['search_field'])
    if ('ADVERBS' in parameters):
        word_list_adverbs = getAssociatedWords('Adverb', 
                                               parameters['search_field'])
    if ('DEFINITION' in parameters):
        word_list_definition = getAssociatedWords('Definition', 
                                                  parameters['search_field'])

    # If the length_field argument is found we call filterByLength() on all the
    # lists of associated words we have stored. Some of these lists might be
    # empty, but that does not matter, as they will remain empty when returned
    # from the function.
    if 'length_field' in parameters:
        word_list_nouns = filterByLength(parameters['length_field'], 
                                         word_list_nouns)
        word_list_verbs = filterByLength(parameters['length_field'], 
                                         word_list_verbs)
        word_list_adjectives = filterByLength(parameters['length_field'], 
                                              word_list_adjectives)
        word_list_adverbs = filterByLength(parameters['length_field'], 
                                           word_list_adverbs)
    # If the letters_field argument is found we call filterByCharacter() on all
    # the lists of associated words we have stored. Some of these lists might be
    # empty, but that does not matter, as they will remain empty when returned
    # from the function.
    elif 'letters_field' in parameters:
        word_list_nouns = filterByCharacters(parameters['letters_field'], 
                                             word_list_nouns)
        word_list_verbs = filterByCharacters(parameters['letters_field'], 
                                             word_list_verbs)
        word_list_adjectives = filterByCharacters(parameters['letters_field'], 
                                                  word_list_adjectives)
        word_list_adverbs = filterByCharacters(parameters['letters_field'], 
                                               word_list_adverbs)

    # Since the associated words are stored in lists, we make the lists into
    # strings where each word is separated by a space. This will make be handy
    # for putting the words into the html template later.
    noun_string = ' '.join(word_list_nouns)
    verb_string = ' '.join(word_list_verbs)
    adverb_string = ' '.join(word_list_adverbs)
    adjective_string = ' '.join(word_list_adjectives)

    # The definitions should be displayed on separate lines on the website,
    # so we add a paragraph tag to each one.
    for i in range(len(word_list_definition)):
        word_list_definition[i] = word_list_definition[i] + '<p></p>'
    definition_string = ' '.join(word_list_definition)

    # Creates the appropriate html code to be formatted into the template.
    # Each category needs to be checked individually, as we do not necessarily
    # know which ones were chosen by the user.
    if ('NOUNS' in parameters):
        noun_string = '<h1 class="div_heading">Nouns:</h1>' + noun_string
        noun_string = '<div id="dd1" class="dynamicDiv"><p>' + noun_string
        noun_string = noun_string + '</p></div>'
        replacements['Nouns'] = noun_string
    else:
        replacements['Nouns'] = noun_string

    if ('VERBS' in parameters):
        verb_string = '<h1 class="div_heading">Verbs:</h1>' + verb_string
        verb_string = '<div id="dd2" class="dynamicDiv"><p>' + verb_string
        verb_string = verb_string + '</p></div>'
        replacements['Verbs'] = verb_string
    else:
        replacements['Verbs'] = verb_string

    if ('ADVERBS' in parameters):
        adverb_string = '<h1 class="div_heading">Adverbs:</h1>' + adverb_string
        adverb_string = '<div id="dd3" class="dynamicDiv"><p>' + adverb_string
        adverb_string = adverb_string + '</p></div>'
        replacements['Adverbs'] = adverb_string
    else:
        replacements['Adverbs'] = adverb_string

    if ('ADJECTIVES' in parameters):
        adjective_string = '<h1 class="div_heading">Adjectives:</h1>' + \
                            adjective_string
        adjective_string = '<div id="dd4" class="dynamicDiv"><p>' + \
                            adjective_string + '</p></div>'
        replacements['Adjectives'] = adjective_string
    else:
        replacements['Adjectives'] = adjective_string

    if ('DEFINITION' in parameters):
        definition_string = '<h1 class="div_heading">Definitions:</h1>' + \
                            definition_string
        definition_string = '<div id="dd5" class="dynamicDiv"><p>' + \
                            definition_string + '</p></div>'
        replacements['Definition'] = definition_string
    else:
        replacements['Definition'] = definition_string
 
    outputText = template_text.format(**replacements)
    
    # And finally print it to standard output, which is the CGI way of
    # communicating content back to the web server.
    print 'Content-type: text/html\r\n\r\n',
    print outputText


def printCategoriesAndFilterPage(search_field, template_filename):
    """
    Prints out the html file given with correct replacements.
    Replacements include values (strings) and javascript code.
    """
    grey_out_box = ''
    keep_js = ''
    # Reads in the necessary files: html template and javascript files.
    try:
        f = open(template_filename)
        template_text = f.read()
        f.close()
        f = open('grey_out_box.js')
        grey_out_box = f.read()
        f.close()
        f = open('keep.js')
        keep_js = f.read()
        f.close()
    except Exception, e:
        template_text = "Cannot read template file <tt>%s</tt>." % (
            template_filename)

    # This will be our dictionary of values to plug into the template file.
    # For each "{foo}" directive in the template, we'll need a key 
    # called "foo".
    temp = indent(search_field, 1)
    replacements = {}
    replacements['search_field'] = temp
    replacements['grey_out_box'] = grey_out_box
    replacements['keep_js'] = keep_js
    
    # Now plug everything into the template...
    outputText = template_text.format(**replacements)

    # And finally print it to standard output, which is the CGI way of
    # communicating content back to the web server.
    print 'Content-type: text/html\r\n\r\n',
    print outputText


def getCgiParameters():
    """
    Returns a dictionary of sanitized, default-populated values for the CGI
    parameters that we care about.
    """
    form = cgi.FieldStorage()
    parameters = {}
    
    # At this point form holds all the parameters given in the url, so we
    # need to check whether the ones we want are in it and store it in the
    # dictionary parameters that will later be used to handle which site
    # is shown and with what content.
    if 'about' in form:
        parameters['about'] = 'About'

    if 'search_field' in form:
        # The 0 is sanitizeUserInputString is because this is a word, which
        # means that it cannot contain underscores.
        word_attempted = sanitizeUserInputString(
                            form['search_field'].value, 0).title()
        if len(word_attempted) == 0:
            parameters['about'] = 'About'
        else:
            parameters['search_field'] = word_attempted

    if 'NOUNS' in form:
        if form['NOUNS'].value == 'on':
            parameters['NOUNS'] = 'on'

    if 'VERBS' in form:
        if form['VERBS'].value == 'on':
            parameters['VERBS'] = 'on'

    if 'ADJECTIVES' in form:
        if form['ADJECTIVES'].value == 'on':
            parameters['ADJECTIVES'] = 'on'

    if 'ADVERBS' in form:
        if form['ADVERBS'].value == 'on':
            parameters['ADVERBS'] = 'on'

    if 'DEFINITION' in form:
        if form['DEFINITION'].value == 'on':
            parameters['DEFINITION'] = 'on'

    # ALL essentially means that every category should be turned on.
    if 'ALL' in form:
        if form['ALL'].value == 'on':
            parameters['NOUNS'] = 'on'
            parameters['VERBS'] = 'on'
            parameters['ADJECTIVES'] = 'on'
            parameters['ADVERBS'] = 'on'
            parameters['DEFINITION'] = 'on'

    # The 1 in sanitizeUserInputString is because this string is allowed to
    # contain underscores, as this is the symbol that represents unknown
    # characters to the user.
    if 'letters_field' in form:
        parameters['letters_field'] = sanitizeUserInputString(
                                        form['letters_field'].value, 1)

    if 'length_field' in form:
        parameters['length_field'] = sanitizeUserInputNumber(
                                        form['length_field'].value)

    return parameters


def sanitizeUserInputNumber(s):
    """
    Method takes a string as input and finds all the characters in the string
    that are integers. These integers are added to a new string and returned.
    """
    if s == None:
        return 0

    # Make sure that the input is a string, as this enables us to check each
    # character individually and see whether it is a legal one.
    s = str(s)
    s = s.strip()
    s_new = ''
    for ch in s:
        # not 0-9
        if (ord(ch) >= 48 and ord(ch) <= 57):
            s_new = s_new + ch
    # Default length is 0 if there are no legal characters.
    if s_new == '':
        s_new = 0
    else:
        s_new = int(s_new)
 
    return s_new


def sanitizeUserInputString(s, code):
    """
    Method takes a string as input and finds all the characters in the string
    that are a-z or A-Z. These characters are added to a new string and
    returned. If the code input value is set to the integer 1, underscores
    are added to the list of legal characters.
    """
    if s == None:
        return ""
    elif code == None:
        return s

    # Make sure that the input is a string as this enables us to check each
    # character individually within the 'legal' ranges for ASCII.
    s = str(s)
    s = s.strip()
    # if letters_field, only allow characters that fall within certain ranges.
    # legal characters are '_' (underscore) and a-z.
    s_new = ''
    for ch in s:
        # not a-z
        if (ord(ch) >= 97 and ord(ch) <= 122):
            s_new = s_new + ch
        elif (ord(ch) >= 65 and ord(ch) <= 90):
            s_new = s_new + ch
        elif code == 1:
            # not a valid character (letter or underscore)
            if ord(ch) == 95:
                s_new = s_new + ch
    s_new = s_new.lower()

    return s_new


def indent(s, k):
    """
    Returns an indented copy of the string, with 4*k spaces prepended to
    each line.
    """
    if type(s) != str:
        return ""
    elif type(k) != int:
        return s
    elif k < 1:
        return s

    return "\n".join([" "*(4*k) + line for line in s.splitlines()])


def getAssociatedWords(type_category, word):
    """
    Returns a list of asssociated words belonging to a category for a given 
    word.
    """
    list_of_words = []
    db = DataSource()

    if db.cursor == None:
        return ["Database error"]

    if word == "":
        return []

    # Calls the proper database interface function given the type specified.
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
        # This will in reality never happen due to the build of the script.
        # However, we cover it for safety reasons.
        return ["Invalid category"]

    return list_of_words


def filterByLength(size, word_list):
    """
    Takes a list of strings and filters the list by length of the string.
    Returns a new list with the strings of appropriate size.
    """
    if size == None:
        return word_list
    elif word_list == None:
        return []
    elif type(word_list) != list:
        return []
    elif type(size) != int:
        return word_list
    elif size < 0:
        return []

    if len(word_list) == 1:
        if word_list[0] == 'Database error':
            return word_list
        elif word_list[0] == 'Invalid category':
            return word_list


    word_list_reviewed = []
    for word in word_list:
        if len(word) == size:
            word_list_reviewed.append(word)
    return word_list_reviewed


def filterByCharacters(character_string, word_list):
    """
    Takes a list of strings and filters the list by positiojn of characters in
    the string. Returns a new list with the strings that had the characters in
    the appropriate positions.
    """
    if character_string == None:
        return word_list
    elif word_list == None:
        return []
    elif type(character_string) != str:
        return word_list
    elif type(word_list) != list:
        return []
    elif len(character_string) == 0:
        return []

    if len(word_list) == 1:
        if word_list[0] == 'Database error':
            return word_list
        elif word_list[0] == 'Invalid category':
            return word_list

    word_list_reviewed = []
    for word in word_list:
        # Only if the word is valid length (less than or equal to the 
        # characters specified) do we consider it at all.
        if len(character_string) == len(word.strip()):
            word_list_reviewed.append(word)

    # If the first character is not underscore, make it capital. Rest of string
    # remains the same.
    if character_string[0] != '_':
        character_string = character_string[0].title() + character_string[1:]

    # Word_list_reviewed now contains the correct words that needs to be
    # filtered by character positions.
    filtered__result_list = []
    for word in word_list_reviewed:
        checker = True
        # Loop over the character in character_list and check if they are
        # anything else than dashes. If they are not dashes, compare the
        # letter to the letter in the same position of the word.
        for i in range(len(character_string)):
            if character_string[i] != "_":
                if character_string[i] != word[i]:
                    checker = False
        if checker == True:
            filtered__result_list.append(word)

    return filtered__result_list



if __name__ == '__main__':
    main()









