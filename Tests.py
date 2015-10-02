"""
Test file for all test methods

"""
from index import *
import test_data_source as test_db

"""Test for : getAssociatedWords(type_category, word):"""
#Testing the method that gets the list of words from the database. 
#Only tests the ability to return the lost of words not the words themselves
# Testing if the type_category if  1 --> Noun 
								#  2 --> Adjective
								#  3 --> Verb
								#  4 --> Adverb
								#  5 --> Definition  : In this case returns a list with strings

# GET-ASSOCIATED-WORDS
def testGetAssociatedWordsForNounShouldReturnListOfWords():
	returnedTest1 = test_db.getAssociatedWords('Noun','Food')

	if not (isinstance(returnedTest1,list)):
		print "Returned object for Noun not a list"

def testGetAssociatedWordsForAdjectiveShouldReturnListOfWords():	
	returnedTest2 = test_db.getAssociatedWords('Adjective','Food')

	if not (isinstance(returnedTest2,list)):
		print "Returned object for Adjective not a list"

def testGetAssociatedWordsForVerbShouldReturnListOfWords():
	returnedTest3 = test_db.getAssociatedWords('Verb','Food')

	if not (isinstance(returnedTest3,list)):
		print "Returned object for Verb not a list"

def testGetAssociatedWordsForAdverbShouldReturnListOfWords():
	returnedTest4 = test_db.getAssociatedWords('Adverb','Food')

	if not (isinstance(returnedTest4,list)):
		print "Returned object for Adverb not a list"

def testGetAssociatedWordsForDefinitionShouldReturnListOfWords():
	returnedTest5 = test_db.getAssociatedWords('Definition','Food')

	if not (isinstance(returnedTest5,list)):
		print "Returned object for Defination not a list of strings"

def testGetAssociatedWordsWithNumberInputShouldReturnEmptyList():
	#illegal : putting number as type_category
	returnedShouldFail = test_db.getAssociatedWords('3','Food')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for 'type_category = 3' not a list"

	if returnedShouldFail != ['Invalid category']:
		print "Returned  a none empty list for the input \
				'type_category = 3' instead of an empty list"

def testGetAssociatedWordsWithIllegalCharactersShouldReturnEmptyList():
	#illegal : putting illegal characters as type_category
	returnedShouldFail = test_db.getAssociatedWords('!@$#%&^%*()_~^','Food')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for 'type_category = illegal characters' not a list"

	if returnedShouldFail != ['Invalid category']:
		print "Returned a none empty list for the input \
				'type_category = illegal characters' instead of an empty list"

def testGetAssociatedWordsWithNoInputShouldReturnEmptyList():
	#illegal : putting nothing as type_category
	returnedShouldFail = test_db.getAssociatedWords('','Food')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for type_category = ''  not a list"

	if returnedShouldFail != ['Invalid category']:
		print "Returned a none empty list for the input \
				type_category = '' instead of an empty list"


def testGetAssociatedWordsWithSpaceShouldReturnEmptyList():
	#illegal : putting space as type_category
	returnedShouldFail = test_db.getAssociatedWords(' ','Food')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for type_category = ' ' not a list"

	if returnedShouldFail != ['Invalid category']:
		print "Returned a none empty list for the input \
				type_category = ' ' instead of an empty list"

def testGetAssociatedWordsWithoutBothInputsShouldReturnEmptyList():
	#illegal: testing for null input for both inputs
	returnedShouldFail = test_db.getAssociatedWords('','')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for type_category = ' ' not a list"

	if returnedShouldFail != []:
		print "Returned a none empty list for the input \
				type_category = ' ' instead of an empty list"

def testGetAssociatedWordsWithWordAsNumberShouldReturnEmptyList():
	#illegal: testing for word = <number>
	returnedShouldFail = test_db.getAssociatedWords('Noun','3')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for 'word = 3' not a list"

	if returnedShouldFail != ['']:
		print "Returned a none empty list for the input \
				'word = 3' instead of an empty list"

def testGetAssociatedWordsWithWordAsNothingShouldReturnEmptyList():
	#illegal: testing for word = ''
	returnedShouldFail = test_db.getAssociatedWords('Noun','')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for word = '' not a list"

	if returnedShouldFail != []:
		print "Returned a none empty list for the input \
				word = '' instead of an empty list"

def testGetAssociatedWordsWithWordAsIllegalCharactersShouldReturnEmptyList():
	#illegal: testing for word = <illegal characters>
	returnedShouldFail = test_db.getAssociatedWords('Noun','~!@#$%^&*()_+')

	if not (isinstance(returnedShouldFail,list)):
		print "Returned object for word = <illegal characters> not a list"

	if returnedShouldFail != ['']:
		print "Returned a none empty list for the input \
				word = <illegal characters> instead of an empty list"


# INDENT
def testIndentWithNoneStringShouldReturnReturnEmptyList():
	# indent(None, 0)
	result = indent(None, 0)

	if result != "":
		print "indent(None, 0) failed."

def testindentWithNoneValueShouldReturnSameString():
	# indent(xxx, None)
	result = indent('a', None)

	if result != 'a':
		print "indent('a', None) failed."

def testIndentWithNegativeValueShouldReturnSameString():
	# indent(xxx, -1)
	result = indent('a', -1)

	if result != 'a':
		print "indent('a', -1) failed."

def testIndentWithZeroValueShouldReturnSameString():
	# indent(xxx, 0)
	result = indent('a', 0)

	if result != 'a':
		print "indent('a', 0) failed."

def testIndentWithOneValueShouldReturnSameStringWithOneIndent():
	# indent(xxx, 1)
	result = indent('a', 1)

	if result != '    a':
		print "indent('a', 1) failed."

def testIndentWithNonStringShouldReturnSameValueButAsString():
	# indent([], 0)
	result = indent(['a'], 0)

	if result != "":
		print "indent(['a'], 0) failed."


# SANITIZE-USER-INPUT-STRING
def testSanitizeUserInputStringWithNoneStringShouldReturnEmptyString():
	# sanitizeUserInputString(None, code)
	result = sanitizeUserInputString(None, 1)

	if result != "":
		print "sanitizeUserInputString(None, 1) failed."

def testSanitizeUserInputStringWithNoneValueShouldReturnSameString():
	# sanitizeUserInputString(string, None)
	result = sanitizeUserInputString('a', None)

	if result != 'a':
		print "sanitizeUserInputString('a', None) failed."

def testSanitizeUserInputStringWithEmptyStringShouldReturnEmptyString():
	# sanitizeUserInputString("", code)
	result = sanitizeUserInputString("", 1)

	if result != "":
		print "sanitizeUserInputString("", 1) failed."

def testSanitizeUserInputStringWithNonStringAndCode0ShouldReturnEmptyString():
	# sanitizeUserInputString([], code)
	result = sanitizeUserInputString([], 0)

	if result != "":
		print "sanitizeUserInputString([], 0) failed."

def testSanitizeUserInputStringWithNonStringAndCode1ShouldReturnEmptyString():
	# sanitizeUserInputString([], code)
	result = sanitizeUserInputString([], 1)

	if result != "":
		print "sanitizeUserInputString([], 1) failed."

def testSanitizeUserInputStringWithStringAndCode1ShouldReturnOnlyCharactersAndUnderscores():
	# sanitizeUserInputString(xxxx, code)
	result = sanitizeUserInputString('abc_123', 1)

	if result != 'abc_':
		print "sanitizeUserInputString('abc_123', 1) failed."

def testSanitizeUserInputStringWithStringAndCode0ShouldReturnOnlyCharacters():
	# sanitizeUserInputString(xxxx, code)
	result = sanitizeUserInputString('abc_123', 0)

	if result != 'abc':
		print "sanitizeUserInputString('abc_123', 0) failed."


# SANITIZE-USER-INPUT-NUMBER
def testSanitizeUserInputNumberWithNoneShouldReturn0():
	# sanitizeUserInputNumber(None)
	result = sanitizeUserInputNumber(None)

	if result != 0:
		print "sanitizeUserInputNumber(None) failed."

def testSanitizeUserInputNumberWithEmptyStringShouldReturn0():
	# sanitizeUserInputNumber("")
	result = sanitizeUserInputNumber("")

	if result != 0:
		print "sanitizeUserInputNumber("") failed."

def testSanitizeUserInputNumberWithNonStringShouldReturn0():
	# sanitizeUserInputNumber(['a'])
	result = sanitizeUserInputNumber(['a'])

	if result != 0:
		print "sanitizeUserInputNumber(['a']) failed."

def testSanitizeUserInputNumberWithStringShouldReturn123():
	# sanitizeUserInputNumber('abc123def')
	result = sanitizeUserInputNumber('abc123def')

	if result != 123:
		print "sanitizeUserInputNumber('abc123def') failed."

def testSanitizeUserInputNumberWithNonStringShouldReturn123():
	# sanitizeUserInputNumber(123)
	result = sanitizeUserInputNumber(123)

	if result != 123:
		print "sanitizeUserInputNumber(123) failed."


# FILTER-BY-LENGTH
def testFilterByLengthWithNoneSizeShouldReturnSameList():
	# filterByLength(None, word_list)
	result = filterByLength(None, ['a'])

	if result != ['a']:
		print "filterByLength(None, ['a'] failed."

def testFilterByLengthWithNoneListShouldReturnEmptyList():
	# filterByLength(size, None)
	result = filterByLength(1, None)

	if result != []:
		print "filterByLength(1, None) failed."

def testFilterByLengthWithNonListShouldReturnEmptyList():
	# filterByLength(size, 'abc')
	result = filterByLength(1, 'abc')

	if result != []:
		print "filterByLength(1, 'abc') failed."

def testFilterByLengthWithNonIntSizeShouldReturnSameList():
	# filterByLength('abc', word_list)
	result = filterByLength('abc', ['a'])

	if result != ['a']:
		print "filterByLength('abc', ['a']) failed."

def testFilterByLengthWithEmptyListShouldReturnEmptyList():
	# filterByLength(size, [])
	result = filterByLength(1, [])

	if result != []:
		print "filterByLength(1, []) failed."

def testFilterByLengthWithNegativeSizeShouldReturnEmptyList():
	# filterByLength(-1, word_list)
	result = filterByLength(-1, ['a'])

	if result != []:
		print "filterByLength(-1, ['a']) failed."

def testFilterByLengthWith0SizeShouldReturnEmptyList():
	# filterByLength(0, word_list)
	result = filterByLength(0, ['a'])

	if result != []:
		print "filterByLength(0, ['a']) failed."

def testFilterByLengthWithPositiveSizeShouldReturnListOfLength2():
	# filterByLength(2, ['aa', 'bb', 'c', 'ddd'])
	result = filterByLength(2, ['aa', 'bb', 'c', 'ddd'])

	if len(result) != 2:
		print "filterByLength(2, ['aa', 'bb', 'c', 'ddd']) failed."


# FILTER-BY-CHARACTERS
def testFilterByCharactersWithNoneStringShouldReturnSameList():
	# filterByCharacters(None, word_list)
	result = filterByCharacters(None, ['a'])

	if result != ['a']:
		print "filterByCharacters(None, ['a']) failed."

def testFilterByCharactersWithNoneListShouldReturnEmptyList():
	# filterByCharacters(chracter_string, None)
	result = filterByCharacters('a', None)

	if result != []:
		print "filterByCharacters('a', None) failed."

def testFilterByCharactersWithNonListShouldReturnEmptyList():
	# filterByCharacters(chracter_string, 'abc')
	result = filterByCharacters('a', 'abc')

	if result != []:
		print "filterByCharacters('a', 'abc')"

def testFilterByCharactersWithNonStringShouldReturnSameList():
	# filterByCharacters(0, word_list)
	result = filterByCharacters(0, ['a'])

	if result != ['a']:
		print "filterByCharacters(0, ['a']) failed."

def testFilterByCharactersWithEmptyListShouldReturnEmptyList():
	# filterByCharacters(chracter_string, [])
	result = filterByCharacters('a', [])

	if result != []:
		print "filterByCharacters('a', []) failed."

def testFilterByCharactersWithEmptyStringShouldReturnEmptyList():
	# filterByCharacters("", word_list)
	result = filterByCharacters("", ['a'])

	if result != []:
		print "filterByCharacters('', ['a']) failed."

def testFilterByCharactersWithUnderscoreStringShouldReturnListOfLength1():
	# filterByCharacters("_", ['a', 'bb'])
	result = filterByCharacters("_", ['a', 'bb'])

	if len(result) != 1:
		print "filterByCharacters('_', ['a', 'bb']) failed."


# TEST-DATA-SOURCE
def testGetAdjectivesListForWordWithNoneShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getAdjectivesListForWord('None')

	if result != ['']:
		print "getAdjectivesListForWord('None') failed."

def testGetAdjectivesListForWordWithNumberShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getAdjectivesListForWord('1')

	if result != ['']:
		print "getAdjectivesListForWord('1') failed."

def testGetAdjectivesListForWordWithWordShouldReturnNonEmptyList():
	db = test_db.DataSourceTest()

	result = db.getAdjectivesListForWord('food')

	if len(result) == 0:
		print "getAdjectivesListForWord('food') failed."
#---
def testGetVerbsListForWordWithNoneShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getVerbsListForWord('None')

	if result != ['']:
		print "getVerbsListForWord('None') failed."

def testGetVerbsListForWordWithNumberShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getVerbsListForWord('1')

	if result != ['']:
		print "getVerbsListForWord('1') failed."

def testGetVerbsListForWordWithWordShouldReturnNonEmptyList():
	db = test_db.DataSourceTest()

	result = db.getVerbsListForWord('food')

	if len(result) == 0:
		print "getVerbsListForWord('food') failed."
#---
def testGetAdverbsListForWordWithNoneShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getAdverbsListForWord('None')

	if result != ['']:
		print "getAdverbsListForWord('None') failed."

def testGetAdverbsListForWordWithNumberShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getAdverbsListForWord('1')

	if result != ['']:
		print "getAdverbsListForWord('1') failed."

def testGetAdverbsListForWordWithWordShouldReturnNonEmptyList():
	db = test_db.DataSourceTest()

	result = db.getAdverbsListForWord('food')

	if len(result) == 0:
		print "getAdverbsListForWord('food') failed."
#---
def testGetNounsListForWordWithNoneShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getNounsListForWord('None')

	if result != ['']:
		print "getNounsListForWord('None') failed."

def testGetNounsListForWordWithNumberShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getNounsListForWord('1')

	if result != ['']:
		print "getNounsListForWord('1') failed."

def testGetNounsListForWordWithWordShouldReturnNonEmptyList():
	db = test_db.DataSourceTest()

	result = db.getNounsListForWord('food')

	if len(result) == 0:
		print "getNounsListForWord('food') failed."
#---
def testGetDefinitionsListForWordWithNoneShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getDefinitionsListForWord('None')

	if result != ['']:
		print "getDefinitionsListForWord('None') failed."

def testGetDefinitionsListForWordWithNumberShouldReturnEmptyList():
	db = test_db.DataSourceTest()

	result = db.getDefinitionsListForWord('1')
	if result != ['']:
		print "getDefinitionsListForWord('1') failed."

def testGetDefinitionsListForWordWithWordShouldReturnNonEmptyList():
	db = test_db.DataSourceTest()

	result = db.getDefinitionsListForWord('food')

	if len(result) == 0:
		print "getDefinitionsListForWord('food') failed."


def main():
	testindentWithNoneValueShouldReturnSameString()
	testIndentWithNegativeValueShouldReturnSameString()
	testIndentWithZeroValueShouldReturnSameString()
	testIndentWithOneValueShouldReturnSameStringWithOneIndent()
	testIndentWithNonStringShouldReturnSameValueButAsString()
	testSanitizeUserInputStringWithNoneValueShouldReturnSameString()
	testSanitizeUserInputStringWithEmptyStringShouldReturnEmptyString()
	testSanitizeUserInputStringWithNonStringAndCode0ShouldReturnEmptyString()
	testSanitizeUserInputStringWithNonStringAndCode1ShouldReturnEmptyString()
	testSanitizeUserInputStringWithStringAndCode1ShouldReturnOnlyCharactersAndUnderscores()
	testSanitizeUserInputStringWithStringAndCode0ShouldReturnOnlyCharacters()
	testSanitizeUserInputNumberWithEmptyStringShouldReturn0()
	testSanitizeUserInputNumberWithNonStringShouldReturn0()
	testSanitizeUserInputNumberWithStringShouldReturn123()
	testSanitizeUserInputNumberWithNonStringShouldReturn123()
	testFilterByLengthWithNoneSizeShouldReturnSameList()
	testFilterByLengthWithNonListShouldReturnEmptyList()
	testFilterByLengthWithNonIntSizeShouldReturnSameList()
	testFilterByLengthWithEmptyListShouldReturnEmptyList()
	testFilterByLengthWithNegativeSizeShouldReturnEmptyList()
	testFilterByLengthWith0SizeShouldReturnEmptyList()
	testFilterByLengthWithPositiveSizeShouldReturnListOfLength2()
	testFilterByCharactersWithNoneStringShouldReturnSameList()
	testFilterByCharactersWithNonListShouldReturnEmptyList()
	testFilterByCharactersWithNonStringShouldReturnSameList()
	testFilterByCharactersWithEmptyListShouldReturnEmptyList()
	testFilterByCharactersWithEmptyStringShouldReturnEmptyList()
	testFilterByCharactersWithUnderscoreStringShouldReturnListOfLength1()
	testGetAssociatedWordsForNounShouldReturnListOfWords()
	testGetAssociatedWordsForAdjectiveShouldReturnListOfWords()
	testGetAssociatedWordsForVerbShouldReturnListOfWords()
	testGetAssociatedWordsForAdverbShouldReturnListOfWords()
	testGetAssociatedWordsForDefinitionShouldReturnListOfWords()
	testGetAssociatedWordsWithNumberInputShouldReturnEmptyList()
	testGetAssociatedWordsWithIllegalCharactersShouldReturnEmptyList()
	testGetAssociatedWordsWithNoInputShouldReturnEmptyList()
	testGetAssociatedWordsWithSpaceShouldReturnEmptyList()
	testGetAssociatedWordsWithoutBothInputsShouldReturnEmptyList()
	testGetAssociatedWordsWithWordAsNumberShouldReturnEmptyList()
	testGetAssociatedWordsWithWordAsNothingShouldReturnEmptyList()
	testGetAssociatedWordsWithWordAsIllegalCharactersShouldReturnEmptyList()
	testGetAdjectivesListForWordWithNoneShouldReturnEmptyList()
	testGetAdjectivesListForWordWithNumberShouldReturnEmptyList()
	testGetAdjectivesListForWordWithWordShouldReturnNonEmptyList()
	testGetVerbsListForWordWithNoneShouldReturnEmptyList()
	testGetVerbsListForWordWithNumberShouldReturnEmptyList()
	testGetVerbsListForWordWithWordShouldReturnNonEmptyList()
	testGetAdverbsListForWordWithNoneShouldReturnEmptyList()
	testGetAdverbsListForWordWithNumberShouldReturnEmptyList()
	testGetAdverbsListForWordWithWordShouldReturnNonEmptyList()
	testGetNounsListForWordWithNoneShouldReturnEmptyList()
	testGetNounsListForWordWithNumberShouldReturnEmptyList()
	testGetNounsListForWordWithWordShouldReturnNonEmptyList()
	testGetDefinitionsListForWordWithNoneShouldReturnEmptyList()
	testGetDefinitionsListForWordWithNumberShouldReturnEmptyList()
	testGetDefinitionsListForWordWithWordShouldReturnNonEmptyList()


if __name__ == '__main__':
    main()
		








	
