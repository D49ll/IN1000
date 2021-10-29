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