from rack import Rack

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
		self._racks = [[Rack()]]
        self._rackIndeks = 0

	def settInnNode(self, node):
		'''
		Plasserer en node inn i et rack med ledig plass, eller i et nytt rack.
			@param node referanse til noden som skal settes inn i datastrukturen		
		'''
		pass

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