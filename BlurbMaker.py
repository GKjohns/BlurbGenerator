import random


#todo
#    Use the markov maker in verse to tell if a corpus is
#    "in the style" of another corpus.

#	write in class that compares the percentage of "first, second"
#	combinations that actually are in the corpus. Test it on books
#	by the same author

#	try setting a threshold frequentist style.




class MarkovMaker:

	def __init__(self, text):
		
		self.raw_text = text
		self.doubles_database = self.loadDoubles()
		self.triples_database = self.loadTriples()

		self.double_count = 0 #number of times doubles were used
		self.triple_count = 0 #number of times triples were used

	def loadDoubles(self):
		
		#Loads doubles

		words = []
		for word in self.raw_text.split():
			words.append(word.strip().translate(None, '"').lower())

		pairs = {}
		for i in xrange(len(words) - 1):
			first, second = words[i], words[i+1]
			key = (first)
			if key in pairs:
				pairs[key].append(second)
			else:
				pairs[key] = [second]

		return pairs

	def loadTriples(self):

		#Loads triples

		words = []
		for word in self.raw_text.split():
			words.append(word.strip().translate(None, '"').lower())
		triples = {}

		for i in xrange(len(words) - 2):
			first, second, third = words[i], words[i+1], words[i+2]
			key = (first, second)

			if key in triples:
				triples[key].append(third)
			else:
				triples[key] = [third]

		return triples

	def generateChain(self, length = 100):

		#TODO
		#   eventually make it so the user can enter a seed word
		#   (obviously sonvert it to lower)

		seed = random.choice(self.triples_database.keys())		
		string = seed[0] + ' ' + seed[1]

		for i in xrange(length - 2):
			string += ' '
			string += random.choice(self.triples_database[(string.split()[-2], string.split()[-1])])
		string += '.'

		print '\n', self.capitalize(string), '\n'

	def capitalize(self, text):
	 	
		words = text.split()

		# If the previous word has a period at the
		# end, capitalize the current word
		for i in xrange(1,len(words)):
			if words[i-1][-1] == '.' or words[i-1][-1] == '!' or words[i-1][-1] == '?':
				words[i] = words[i][0].upper() + words[i][1:]

		string = ''

		for word in words:
			string += word
			string += ' '

		return string[0].upper() + string[1:]


if __name__ == '__main__':
	
	number_of_words = 100
	corpus = open('dorian_gray.txt', 'rb').read()

	my_maker = MarkovMaker(corpus)
	my_maker.generateChain(number_of_words)
