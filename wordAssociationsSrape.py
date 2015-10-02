


import requests
from bs4 import BeautifulSoup
import csv
import sys
import os
import time
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://wordassociations.net/search?hl=en&l=%s&start=%s"

csv_list = []
csv_list.append(["Word", "Definition", "Nouns", "Adjectives", "Verbs", "Adverbs"])

word_dictionary = {}
word_and_link_dict = {}

for n in range(7, 14, 1):
    letter = chr(n + 97)

    for num in range(0, 5500, 100):
        time.sleep(0.1)

        r = requests.get(url % (letter, num))
        soup = BeautifulSoup(r.content)

        if (soup.find(attrs={"id":"discoErrorNotice"}) != None): continue

        dictSectionOfWords = soup.find(attrs={"class":"dict"})
        if (dictSectionOfWords != None):
            for li in dictSectionOfWords.findAll('li'):
                if li != None:
                    if li.get_text() != "":
                        if li.a != None:
                            if li.a.get("href") != None:
                                print li
                                word_and_link_dict[li.get_text()] = li.a.get("href")

words_list = [] 
for i in word_and_link_dict:
    words_list.append([i, word_and_link_dict[i]])
filename = "words scrape and link"
myfile = open(filename + ".csv", "wb")
wr = csv.writer(myfile, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
wr.writerows(words_list)
myfile.close()

print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "A new beginning!!!!!!!!"
print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "############################################"
print "############################################"


#word_url = "http://wordassociations.net%s&start=%s"
word_url = "http://wordassociations.net/search?hl=en&w=%s&start=%s"

sorted_word_and_link_keys = sorted(word_and_link_dict.keys())
for word in sorted_word_and_link_keys:
    noun_list = []
    adjective_list = []
    verb_list = []
    adverb_list = []
    definition_list = []
    definition_dictionary = {}

    print word

    for num in range(0, 1000, 100):
        time.sleep(0.1)

        r = requests.get(word_url % (word, num))
        soup = BeautifulSoup(r.content)

        content = soup.find(attrs={"class":"n-content"})

        if content != None:
            if content != "":
                # content_left = content.find(attrs={"class":"n-content-left"})
                # content_right = content.find(attrs={"class":"n-content-right"})

                nouns_content = content.find(attrs={"class":"section NOUN-SECTION"})
                adjectives_content = content.find(attrs={"class":"section ADJECTIVE-SECTION"})
                verb_content = content.find(attrs={"class":"section VERB-SECTION"})
                adverb_content = content.find(attrs={"class":"section ADVERB-SECTION"})
                definition_content = content.find(attrs={"class":"dictionary-content"})

                # print nouns_content
                # print adjectives_content
                # print verb_content
                # print adverb_content
                # print definition_content

                # print "############################################"
                # print "NOUNS!"
                # print "############################################"

                if nouns_content != None:
                    if nouns_content != "":
                        for li in nouns_content.findAll('li'):
                            if li != None:
                                noun_associated = li.get_text()
                                if noun_associated != "":
                                    # print noun_associated
                                    noun_list.append(noun_associated)

                # print "############################################"
                # print "ADJECTIVES!"
                # print "############################################"

                if adjectives_content != None:
                    if adjectives_content != "":
                        for li in adjectives_content.findAll('li'):
                            if li != None:
                                adjective_associated = li.get_text()
                                if adjective_associated != "":
                                    # print adjective_associated
                                    adjective_list.append(adjective_associated)

                # print "############################################"
                # print "VERBS!"
                # print "############################################"

                if verb_content != None:
                    if verb_content != "":
                        for li in verb_content.findAll('li'):
                            if li != None:
                                verb_associated = li.get_text()
                                if verb_associated != "":
                                    # print verb_associated
                                    verb_list.append(verb_associated)

                # print "############################################"
                # print "ADVERBS!"
                # print "############################################"

                if adverb_content != None:
                    if adverb_content != "":
                        for li in adverb_content.findAll('li'):
                            if li != None:
                                adverb_associated = li.get_text()
                                if adverb_associated != "":
                                    # print adverb_associated
                                    adverb_list.append(adverb_associated)

                # print "############################################"
                # print "DEFINITIONS!"
                # print "############################################"

                if definition_content != None:
                    if definition_content != "":
                        for article in definition_content.find_all(attrs={"class":"dictionary-article"}):
                            if article != None:
                                definition = article.get_text()
                                if definition != None:
                                    if definition != "":
                                        if definition not in definition_dictionary:
                                            # print definition
                                            definition_list.append(definition)
                                            definition_dictionary[definition] = 1
    # print noun_list
    # print adjective_list
    # print verb_list
    # print adverb_list
    # print definition_list

    # ["Word", "Definition", "Nouns", "Adjectives", "Verbs", "Adverbs"]
    #word_dictionary[word] = [word, definition_list, noun_list, adjective_list, verb_list, adverb_list]
    csv_list.append([word, definition_list, noun_list, adjective_list, verb_list, adverb_list])

if len(csv_list) != 1:
    filename = "TEST word associations scrape"
    myfile = open(filename + "-unfinished.csv", "wb")
    wr = csv.writer(myfile, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
    wr.writerows(csv_list)
    myfile.close()

    open(filename + ".csv", "w").write("sep=,\n" + open(filename + "-unfinished.csv").read())
    os.remove(filename + "-unfinished.csv")
else:
    print "Failed to collect any information."

print "Done!"


