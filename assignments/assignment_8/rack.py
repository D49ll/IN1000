class Rack:
	'''
	Klasse for representasjon av racks i en regneklynge.
	'''

	def __init__(self, maxAntNoder):
		'''
		Oppretter et rack der det senere kan plasseres noder	
		'''
		self._noder = []
		self._maxNoder = maxAntNoder


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

	def _rackFult(self):
		if len(self._noder)==self._maxNoder:
			return True
		return False
