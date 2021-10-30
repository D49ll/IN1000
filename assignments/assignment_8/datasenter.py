from regneklynge import Regneklynge

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
		#Klyngenavn tilsvarer navn på fil minus ".txt"
		klyngeNavn,_ = filnavn.split('.')

		#Leser fra fil og lagrer alle linjer i en nøstet liste
		f = open(filnavn).read()
		linjer = f.splitlines()
	
		#Første linje fra fil tilsvarer alltid max antall noder pr rack
		maxNoderPrRack = int(linjer[0])

		#Oppretter Regneklynge objekt med node begrensninger
		self._regneklyger[klyngeNavn] = Regneklynge(maxNoderPrRack)

		#Legger til noder i racks tilhørende regneklyngen
		for i in range(1,len(linjer)):
			noder, minne, antPros = linjer[i].split(' ')
			for i in range(int(noder)):
				self._regneklyger[klyngeNavn].settInnNode((int(minne), int(antPros)))
		
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

datasenter = Datasenter()

datasenter.lesInnRegneklynge('abel.txt')






