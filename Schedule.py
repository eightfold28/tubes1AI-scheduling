#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from random import randint
from CSP import *
from copy import deepcopy

class Schedule:
	def __init__(self):
		self.__jadwalbaru = []

#METHOD
	def inisialisasi(self, CSP):
	# generate solusi random, dimana solusi yang diterima adalah state jadwal sudah memenuhi constraint jadwal dan ruangan
		self.__jadwalbaru = deepcopy(CSP.getListOfJadwal())
		CSP.setListOfJadwal(self.__jadwalbaru)
		CSP.hitungConflict1()
		temp = CSP.getJumlahConflict1() #nilai konflik terhadap diri sendiri, yakni ruangan tersedia utk jadwal
		new = True #penanda untuk masuk ke while minimal 1x
		while (temp > 0 or new):
			for item in self.__jadwalbaru:
				r_ruangan = randint(0, len(item.getDomainOfRuangan())-1)
				item.setRuangan(r_ruangan)
				r_jamMulai = randint(0, len(item.getDomainOfJamMulai())-1)
				item.setJamMulai(r_jamMulai)
				r_jamSelesai = item.getJamMulai() + item.getDurasi()
				item.setJamSelesaiSpecial(r_jamSelesai)
				r_hari = randint(0, len(item.getDomainOfHari())-1)
				item.setHari(r_hari)
			CSP.setListOfJadwal(self.__jadwalbaru)
			CSP.hitungConflict1()
			temp = CSP.getJumlahConflict1()
			new = False

#GETTER
	def getSolutionState(self):
		return self.__jadwalbaru		
