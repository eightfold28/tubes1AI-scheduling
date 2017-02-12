#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

import copy

class Jadwal:
#STATIC
    __count = 0

#CTOR CCTOR DTOR
    def __init__ (self, nama_kegiatan, domain_of_ruangan, jam_mulai, jam_selesai, durasi, domain_of_hari):
        self.__nama_kegiatan = nama_kegiatan

        self.__domain_of_ruangan = domain_of_ruangan
        self.__ruangan = self.__domain_of_ruangan[0]
        self.__is_ruangan_conflicted = False

        self.__domain_of_hari = domain_of_hari
        for index in range(len(self.__domain_of_hari)):
            self.__domain_of_hari[index] -= 1
        self.__hari = self.__domain_of_hari[0]
        self.__is_hari_conflicted = False

        self.__durasi = durasi

        self.__domain_of_jam_mulai = []
        self.__domain_of_jam_selesai = []

        temp_jam_mulai = jam_mulai
        temp_jam_selesai = jam_mulai + self.__durasi

        while (temp_jam_mulai + self.__durasi <= jam_selesai):
            self.__domain_of_jam_mulai.append(temp_jam_mulai)
            temp_jam_mulai += 1

        while (temp_jam_selesai <= jam_selesai):
            self.__domain_of_jam_selesai.append(temp_jam_selesai)
            temp_jam_selesai += 1

        self.__jam_mulai = self.__domain_of_jam_mulai[0]
        self.__jam_selesai = self.__domain_of_jam_selesai[0]
        self.__is_jam_mulai_conflicted = False
        self.__is_jam_selesai_conflicted = False
        Jadwal.__count += 1

    def copy(self):
        Jadwal.__count += 1
        return copy.deepcopy(self)

    def __del__ (self):
        Jadwal.__count -= 1

#GETTER
    def getNamaKegiatan(self):
        return self.__nama_kegiatan

    def getNamaRuangan(self):
        return self.__ruangan

    def getDomainOfRuangan(self):
        return self.__domain_of_ruangan

    def getJamMulai(self):
        return self.__jam_mulai

    def getDomainOfJamMulai(self):
        return self.__domain_of_jam_mulai

    def getJamSelesai(self):
        return self.__jam_selesai

    def getDomainOfJamSelesai(self):
        return self.__domain_of_jam_selesai

    def getDurasi(self):
        return self.__durasi

    def getHari(self):
        return self.__hari

    def getDomainOfHari(self):
        return self.__domain_of_hari

    def isRuanganConflicted(self):
        return self.__is_ruangan_conflicted

    def isJamMulaiConflicted(self):
        return self.__is_jam_mulai_conflicted

    def isJamSelesaiConflicted(self):
        return self.__is_jam_selesai_conflicted

    def isHariConflicted(self):
        return self.__is_hari_conflicted

#SETTER
    def setNamaKegiatan(self, nama_kegiatan):
        self.__nama_kegiatan = nama_kegiatan

    def setRuangan(self, index):
        self.__ruangan = self.__domain_of_ruangan[index]

    def setRuanganSpecial(self, nama_ruangan):
        self.__ruangan = nama_ruangan

    def setJamMulai(self, index):
        self.__jam_mulai = self.__domain_of_jam_mulai[index]

    def setJamMulaiSpecial(self, jam_mulai):
        self.__jam_mulai = jam_mulai

    def setJamSelesai(self, index):
        self.__jam_selesai = self.__domain_of_jam_selesai[index]

    def setJamSelesaiSpecial(self, jam_selesai):
        self.__jam_selesai = jam_selesai

    def setHari(self, index):
        self.__hari = self.__domain_of_hari[index]

    def setHariSpecial(self, hari):
        self.__hari = hari

    def setRuanganConflictStatus(self, value):
        self.__is_ruangan_conflicted = value

    def setJamMulaiConflictStatus(self, value):
        self.__is_jam_mulai_conflicted = value

    def setJamSelesaiConflictStatus(self, value):
        self.__is_jam_selesai_conflicted = value

    def setHariConflictStatus(self, value):
        self.__is_hari_conflicted = value

    def setDurasi(self, value):
        self.__durasi = value

#METHOD
    def __str__ (self):
        return """{}
Ruangan             : {}
  Domain Ruangan    : {}
Jam Mulai           : {}
  Domain Jam Mulai  : {}
Jam Selesai         : {}
  Domain Jam Selesai: {}
Durasi              : {}
Hari                : {}
  Domain Hari       : {}""".format (self.getNamaKegiatan(),
self.getNamaRuangan(), self.getDomainOfRuangan(),
self.getJamMulai(), self.getDomainOfJamMulai(),
self.getJamSelesai(), self.getDomainOfJamSelesai(),
self.getDurasi(),
self.getHari(), self.getDomainOfHari())
