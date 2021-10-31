from regneklynge import Regneklynge

class Datasenter:
	'''
	Klasse for representasjon av et datasenter
	'''
	def __init__(self):
		'''
		Initierer en tom ordliste til fremtidige regnklynger
		'''
		self._klynger = dict()

	def lesInnRegneklynge(self, filnavn):
		'''
		Leser inn data om en regneklynge fra fil og legger den til i ordboken
			@param filnavn filene der dataene for regneklyngen ligger
		'''
		#Klyngenavn tilsvarer navn på fil minus ".txt"
		navn,_ = filnavn.split('.')

		#Leser fra fil og lagrer alle linjer i en nøstet liste
		f = open(filnavn).read()
		linjer = f.splitlines()
	
		#Første linje = max antall noder pr rack
		maxNoderPrRack = int(linjer[0])

		#Oppretter Regneklynge objekt med node begrensninger
		self._klynger[navn] = Regneklynge(maxNoderPrRack)

		#Legger til noder i racks
		for i in range(1,len(linjer)):
			noder, minne, antPros = linjer[i].split(' ')
			for _ in range(int(noder)):
				self._klynger[navn].settInnNode((int(minne), int(antPros)))
		
	def skrivUtAlleRegneklynger(self): 
		'''
		Skriver ut informasjon om alle regneklyngene i datasenteret
		'''
		for klynge in self._klynger:
			self.skrivUtRegneklynge(klynge)			


	def skrivUtRegneklynge(self, navn):
		'''
		Skriver ut informasjon om en spesifikk regeklynge
			@param navn navnet på regnekyngen
		'''
		#Test variabler
		paakrevdMinne = [32,64,128]
		antNoder = []
		
		#Sjekker minne i alle noder mot aktuelt minnekrav
		for minne in paakrevdMinne:
			antNoder.append(self._klynger[navn].noderMedNokMinne(minne))
		
		#Resultat til terminal
		print()
		print(f'Informasjon om regneklyngen \'{navn}\':')
		for i in range(len(antNoder)):
			print(f'Noder med minst {paakrevdMinne[i]} GB: {antNoder[i]}')
		print(f'Antall prosessorer: {self._klynger[navn].antProsessorer()}')
		print(f'Antall rack: {self._klynger[navn].antRacks()}')




		







