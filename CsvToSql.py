

import csv
import sys


# NOTE:
# All information will be in strings in the database. When retrieving info from
# the database a split on " ,, " (<space>,,<space>) needs to be performed.


# read the csv file.
reader = csv.reader(sys.stdin, dialect='excel')
count = 0
# loop over the rows in the csv file, but skip the first two.
# the first contains a hack to make it openable in excel and the second
# contains the headers.
# this is handled with a simple counter.
for row in reader:
	if count > 1:
		noun_string = ""
		adjective_string = ""
		verb_string = ""
		adverb_string = ""
		definition_string = ""

		row = map(str.strip, row)
		index = 0
		# loop over the entries in the csv file.
		# skip the first row as it contains information we do not want.
		for i in row:
			if index == 1:
				column_list = []
				if len(i) > 2:
					column_edited = row[1][3:]
					column_list = column_edited.split("', u'")
					column_list[-1] = column_list[-1][:-2]

					for i in column_list:
						definition_string = definition_string + i + " ,, "
					definition_string = definition_string[:-4]
			elif index > 1:
				if len(i) > 2:
					# remove unwanted characters from beginning of the string
					column_edited = i[3:]
					# split on "', u" --> unicode character
					column_list = column_edited.split("', u'")
					# remove unwanted characters from the end.
					column_list[-1] = column_list[-1][:-2]

					# loop over the items in the entry and add them to the
					# correct string.
					for i in column_list:
						if index == 2:
							noun_string = noun_string + i + " ,, "
						elif index == 3:
							adjective_string = adjective_string + i + " ,, "
						elif index == 4:
							verb_string = verb_string + i + " ,, "
						elif index == 5:
							adverb_string = adverb_string + i + " ,, "

			index = index + 1

		# remove ' ,, ' from end of string.
		noun_string = noun_string[:-4]
		adjective_string = adjective_string[:-4]
		verb_string = verb_string[:-4]
		adverb_string = adverb_string[:-4]

		# remove ' and " as these can mess with the data.
		noun_string = noun_string.replace("'", "")
		adjective_string = adjective_string.replace("'", "")
		verb_string = verb_string.replace("'", "")
		adverb_string = adverb_string.replace("'", "")
		definition_string = definition_string.replace("'", "")

		noun_string = noun_string.replace('"', "")
		adjective_string = adjective_string.replace('"', "")
		verb_string = verb_string.replace('"', "")
		adverb_string = adverb_string.replace('"', "")
		definition_string = definition_string.replace('"', "")

		# print "CORRECT?"
		# print noun_string
		# print ""
		# print adjective_string
		# print ""
		# print verb_string
		# print ""
		# print adverb_string
		# print ""
		# print definition_string

		# create the query itself.
		query = "INSERT INTO associations (word, definition, nouns, adverbs, verbs, adjectives)"
		query += " VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (row[0], definition_string, noun_string, adverb_string, verb_string, adjective_string)

		print query

	count = count + 1









