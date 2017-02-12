#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from Schedule import *

class HillClimbing:
	def __init__(self):
		self.__current = []
		self.__neighbor = []

	def algorithm(self, Schedule, CSP, value):
		# Cari jadwal awal
		Schedule.inisialisasi(CSP)
		self.__current = deepcopy(Schedule.getSolutionState())
		CSP.setListOfJadwal(self.__current)
		CSP.hitungConflict2()
		tempcurrent = CSP.getJumlahConflict2() # tempcurrent adalah jumlah conflict awal
		i = 0
		while (i <= value):
			# Cari jadwal neighbor
			Schedule.inisialisasi(CSP)
			self.__neighbor = deepcopy(Schedule.getSolutionState())
			CSP.setListOfJadwal(self.__neighbor)
			CSP.hitungConflict2()
			tempneighbor = CSP.getJumlahConflict2() # tempneighbor adalah jumlah conflict neighbor
			if (tempneighbor < tempcurrent): # conflict neighbor lebih sedikit daripada conflict current (neighbor solusi lebih baik)
				# set current menjadi neighbor
				self.__current = deepcopy(CSP.getListOfJadwal())
				CSP.setListOfJadwal(self.__current)
				tempcurrent = tempneighbor
			else: # conflict current lebih sedikit daripada conflict neighbor (current solusi lebih baik)
				CSP.setListOfJadwal(self.__current)
			i += 1
			CSP.hitungConflict2()

#GETTER
	def getListOfCurrent(self):
		return self.__current

	def getListOfNeighbor(self):
		return self.__neighbor
