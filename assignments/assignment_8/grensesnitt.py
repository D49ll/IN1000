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
			self._regneklyger[klyngeNavn] = Regneklynge(maxNoderPrRack)

			for _ in noder:
				self._regneklyger[klyngeNavn].settInnNode(Node(minne, antPros))




	def skrivUtAlleRegneklynger(self): 
		'''
		Skriver ut informasjon om alle regneklyngene
		'''
		pass

	def skrivUtRegneklynge(self, navn):
		'''
		Skriver ut informasjon om en spesifikk regeklynge
			@param navn navnet på regnekyngen
		'''
		pass


class Regneklynge:
	'''
	Klasse for representasjon av regneklynge i et datasenter.
	'''

	def __init__(self, noderPerRack):
		'''
		Oppretter en regneklynge og setter maks antall det er plass til i et rack
			@param noderPerRack max antall noder per rack
		'''
		self._noderPerRack = noderPerRack
		self._racks = [[]]
		self._rackIndeks = 0
		self._nodeIndeks = 0


	def settInnNode(self, node):
		'''
		Plasserer en node inn i et rack med ledig plass, eller i et nytt rack.
			@param node referanse til noden som skal settes inn i datastrukturen		
		'''

		if self._nodeIndeks > self._noderPerRack:
			self._rackIndeks += 1
			self._nodeIndeks = 0

		self._racks[self._rackIndeks].append(Rack)
		self._nodeIndeks += 1



	def antProsessorer(self):
		'''
		Beregner totalt antall prosessorer i hele regneklyngen
			@return totalt antall prosessorer		
		'''
		pass


	def noderMedNokMinne(self, paakrevdMinne):
		'''
		Beregner antall noder i regneklyngen med minne over angitt grense
			@param paakrevdMinne hvor mye minne skal noder som telles med ha
			@return antall noder med tilstrekkelig minne		
		'''
		pass


	def antRacks(self):
		'''
		Henter antall racks i regneklyngen
			@return antall racks		
		'''
		pass



class Rack:
	'''
	Klasse for representasjon av racks i en regneklynge.
	'''

	def __init__(self,navn):
		'''
		Oppretter et rack der det senere kan plasseres noder	
		'''
		self._navn = navn
		self._noder = []


	def settInn(self, node):
		'''
		Plasserer en ny node inn i racket
			@param node noden som skal plasseres inn		
		'''
		self._noder.append(node)


	def getAntNoder(self):
		'''
		Henter antall noder i racket
			@return antall noder
		'''
		return len(self._noder)


	def antProsessorer(self):
		'''
		Beregner sammenlagt antall prosessorer i nodene i et rack
			@return antall prosessorer		
		'''
		antPros = 0
		for node in self._noder:
			antPros += node.antProsessorer()
		return antPros

	def noderMedNokMinne(self, paakrevdMinne):
		'''
		Beregner antall noder i racket med minne over gitt grense
			@param paakrevdMinne antall GB minne som kreves
			@return antall noder med tilstrekkelig minne
		'''
		antNoder = 0
		for node in self._noder:
			if node.nokMinne(paakrevdMinne):
				antNoder += 1
		return antNoder

class Node:
	'''
	Klasse for representasjon av noder i en regneklynge
	'''
	def __init__(self, minne, antPros):
		'''
		Oppretter en node med gitt minne-storrelse og antall prosessorer
			@param minne GB minne i den nye noden
			@param antPros antall prosessorer i den nye noden
		'''

		self._minne = minne
		self._antPros = antPros

	def antProsessorer(self):
		'''
		Henter antall prosessorer i noden
			@return antall prosessorer i noden
		'''

		return self._antPros

	
	def nokMinne(self, paakrevdMinne):
		'''
		Sjekker om noden har tilstrekkelig minne for et program
			@param paakrevdMinne GB minne som kreves for programmet
			@return True hvis noden har minst så mye minne
		'''

		if paakrevdMinne <= self._minne:
			return True
		return False