#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from __future__ import division
from math import exp
import random
from Schedule import *
from copy import deepcopy


class SimulatedAnnealing:
	def __init__(self, T, Tmin, alpha):
		self.__SolutionResult = []
		self.__newSolution = []
		self.__T = T
		self.__Tmin = Tmin
		self.__alpha = alpha

	#Nilai probabilitas yang masih diperbolehkan
	def acceptance_probability(self, cOld, cNew, T):
		return exp((cOld-cNew)/T)

	#Algoritma utama simulated annealing
	def inisialisasi(self, schedule, CSP):
		self.__SolutionResult = deepcopy(schedule.getSolutionState())
		CSP.setListOfJadwal(self.__SolutionResult)
		CSP.hitungConflict2()
		costAwal = CSP.getJumlahConflict2()
		#inputan standar
		#T = 1 #suhu awal
		#Tmin = 0.00001
		#alpha = 0.9
		T = self.__T
		Tmin = self.__Tmin
		alpha = self.__alpha
		# Iterasi selama suhu masih panas atau jumlah konflik tidak 0
		while (T > Tmin and costAwal > 0):
			#coba modifikasi solusi sebelumnya
			schedule.inisialisasi(CSP)
			self.__newSolution = schedule.getSolutionState()
			CSP.setListOfJadwal(self.__newSolution)
			CSP.hitungConflict2()
			costBaru = CSP.getJumlahConflict2()
			if (costBaru < costAwal):
				self.__SolutionResult = deepcopy(self.__newSolution)
				costAwal = costBaru
			else:
				ap = self.acceptance_probability(costAwal, costBaru, T)
				rand = random.uniform(0,0.2)
				if (ap > rand):
					self.__SolutionResult = deepcopy(self.__newSolution)
					costAwal = costBaru
					CSP.hitungConflict2()
					x = CSP.getJumlahConflict2()
				else:
					CSP.setListOfJadwal(self.__SolutionResult)
					CSP.hitungConflict2()
					x = CSP.getJumlahConflict2()
			T = T*alpha
		CSP.setListOfJadwal(self.__SolutionResult)
		CSP.hitungConflict2()

	def HitungEfisiensi(self, CSP):
		return (((len(CSP.getListOfJadwal())) - CSP.getJumlahConflict2()) / (len(CSP.getListOfJadwal())))

		#GETTER
	def getResult(self):
		return self.__SolutionResult
