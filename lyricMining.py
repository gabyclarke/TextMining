""" CODE FOR SOFTDES MINI PROJECT 3: TEXT MINING
	SPRING 2016

	MINING SONG LYRICS FOR AN ARTIST

	@author: Gaby Clarke

"""

import string
from pattern.web import *
import unicodedata

def getArtistPages(artist):
	""" takes an artist and generates all artist pages populated with songs 

		artist: formatted artist name
		generates: artist pages '___#.txt'
	"""

	i = 0
	while True:
		i += 1
		url = 'https://www.musixmatch.com/artist/{}/{}'.format(artist, i)
		artistPage = URL(url).download()
		content = plaintext(artistPage)

		f = open('{}{}.txt'.format(artist, i), 'w')
		f.write(content.encode("UTF-8"))
		f.close()

		if '* 15' not in content:
			break


def cleanUpArtistPage(fileName):
	""" takes an artist page and returns the unformatted song list from that page
		
		fileName: '___.txt'
		returns: unformatted song list
	"""

	f = open(fileName, 'r+')
	content = f.read()

	i = content.find('* 01')
	j = content.rfind('Load more')
	print content[i:j]
	return content[i:j]


def cleanUpLyrics(s):
	""" takes an unformatted string and returns a list of lowercase words without
		punctuation

		string: a string
		returns: a formatted list of words in the string
	"""

	string = string.lower()

	for char in string.punctuation:
		if char != "'":
			string = string.replace(char, '')

	wordList = string.split()
	return wordList


def histogram(wordList):
	""" takes a list of words and returns a dictionary with each word as a key to the number
		of times the word appears in the list

		wordList: a list of words
		returns: dictionary (word and frequency)
	"""

	d = dict()
	for word in wordList:
		d[word] = d.get(word, 0) + 1
	return d



if __name__ == "__main__":
	import doctest
	# doctest.testmod()

	# getArtistPages('Broken-Bells')
	cleanUpArtistPage('Broken-Bells1.txt')
