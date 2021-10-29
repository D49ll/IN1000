from regneklynge import Regneklynge
from node import Node

class Datasenter:
	'''
	Klasse for representasjon av et datasenter
	'''
	def __init__(self):
		self._regneklyger = dict()

	def lesInnRegneklynge(self, filnavn):
		'''
		Leser inn data om en regneklynge fra fil og legger den til i ordboken
			@param filnavn filene der dataene for regneklyngen ligger
		'''
		klyngeNavn,_ = filnavn.split('.')

		f = open(filnavn).read()
		linjer = f.splitlines()
	
		maxNoderPrRack = int(linjer[0])

		for i in range(1,len(linjer)):
			noder, minne, antPros = linjer[i].split(' ')
			noder = int(noder)
			minne = int(minne)
			antPros = int(antPros)
			self._regneklyger[klyngeNavn] = Regneklynge(maxNoderPrRack)

			for _ in range(noder):
				self._regneklyger[klyngeNavn].settInnNode(Node(minne, antPros))

	def skrivUtAlleRegneklynger(self): 
		'''
		Skriver ut informasjon om alle regneklyngene
		'''

	def skrivUtRegneklynge(self, navn):
		'''
		Skriver ut informasjon om en spesifikk regeklynge
			@param navn navnet på regnekyngen
		'''
		pass

test = Datasenter()

test.lesInnRegneklynge('abel.txt')



print(test)





