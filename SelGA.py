#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from CSP import *
import copy
from random import randint

class SelGA:
#KONSTRUKTOR
	def __init__ (self):
		self.__nama_matkul = ""
		self.__ruangan = ""
		self.__hari = 0
		self.__jam_mulai = 0
		self.__durasi = 0
		self.__jam_selesai = 0
		self.__idconflict = -1 #tidak berkonflik

	def isiSel (self, Jadwal, daftar_ruangan):
		found = False

		while (found == False):
			#PENCARIAN VALUE NAMA MATA KULIAH
			matkul = Jadwal.getNamaKegiatan()
			self.setNamaMatkul(matkul)

			#PENCARIAN NILAI DURASI
			durasi = Jadwal.getDurasi()
			self.setDurasi(durasi)

			#PENCARIAN VALUE RUANGAN UNTUK MATA KULIAH
			r_ruangan = randint(0,len(Jadwal.getDomainOfRuangan())-1)
			ruang = Jadwal.getDomainOfRuangan()[r_ruangan]
			self.setRuangan(ruang)

			#PENCARIAN RUANGAN DARI JADWAL KE DAFTAR RUANGAN
			for item in range(len(daftar_ruangan)):
				if daftar_ruangan[item].getNamaRuangan() == ruang:
					idxRuangan = item
					break

			#PENCARIAN VALUE HARI UNTUK MATA KULIAH
			hari1 = Jadwal.getDomainOfHari()
			hari2 = [] #hari dari ruangan
			for i in range (5):
				if daftar_ruangan[idxRuangan].getListOfAvailableHari()[i] == True:
					hari2.append(i)

			#NILAI INTERSECT HARI PADA JADWAL MATA KULIAH DAN HARI PADA RUANGAN
			hari = []
			hari = list(set(hari1) & set(hari2))
			if (len(hari) == 0):
				continue
			r_hari = randint(0,len(hari)-1)
			self.setHari(hari[r_hari])

			#PENCARIAN VALUE JAM MULAI UNTUK MATA KULIAH
			mulai1 = Jadwal.getDomainOfJamMulai()
			mulai2 = []
			jamBukaRuangan = daftar_ruangan[idxRuangan].getJamSelesai() - daftar_ruangan[idxRuangan].getJamMulai()
			for i in range (jamBukaRuangan):
				cond1 = ((i + daftar_ruangan[idxRuangan].getJamMulai() + self.__durasi) <= daftar_ruangan[idxRuangan].getJamSelesai())
				cond2 = ((i + daftar_ruangan[idxRuangan].getJamMulai() + self.__durasi) <= Jadwal.getDomainOfJamSelesai()[len(Jadwal.getDomainOfJamSelesai()) -1])
				if ((cond1 == True) and (cond2 == True)):
					mulai2.append(i + daftar_ruangan[idxRuangan].getJamMulai())

			#NILAI INTERSECT WAKTU MULAI PADA JADWAL MATA KULIAH DAN WAKTU MULAI PADA RUANGAN
			mulai = list(set(mulai1) & set(mulai2))
			if (len(mulai) == 0):
				continue
			r_mulai = randint(0,len(mulai)-1)
			self.setJamMulai(mulai[r_mulai])

			#PENCARIAN VALUE JAM SELESAI UNTUK MATA KULIAH
			selesai = self.__jam_mulai + self.__durasi
			self.setJumSelesai(selesai)

			found = True

#GETTER
	def getNamaMatkul(self):
		return self.__nama_matkul

	def getRuangan(self):
		return self.__ruangan

	def getHari(self):
		return self.__hari

	def getJamMulai(self):
		return self.__jam_mulai

	def getJamSelesai(self):
		return self.__jam_selesai

	def getDurasi(self):
		return self.__durasi

	def getIdConflict(self):
		return self.__idconflict

#SETTER
	def setNamaMatkul(self, matkul):
		self.__nama_matkul = matkul

	def setRuangan(self, ruang):
		self.__ruangan = ruang

	def setHari(self, hari):
		self.__hari = hari

	def setJamMulai(self, mulai):
		self.__jam_mulai = mulai

	def setJumSelesai(self, selesai):
		self.__jam_selesai = selesai

	def setDurasi(self, durasi):
		self.__durasi = durasi

	def setIdConflict(self, conf):
		self.__idconflict = conf

#METHOD
	def printSel(self):
		print("[{0}, {1}, {2}, {3}, {4}, {5}]".format(self.getNamaMatkul(), self.getRuangan(), self.getHari(), self.getDurasi(), self.getJamMulai(), self.getJamSelesai()))
