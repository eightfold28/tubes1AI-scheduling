#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

import copy

class Ruangan:
#STATIC
    __count = 0

#CTOR CCTOR DTOR
    def __init__ (self, nama_ruangan, jam_mulai, jam_selesai, list_of_hari):
        self.__nama_ruangan = nama_ruangan
        self.__jam_mulai = jam_mulai
        self.__jam_selesai = jam_selesai
        self.__list_of_available_hari = [False,False,False,False,False]
        for hari in list_of_hari:
            self.__list_of_available_hari[hari-1] = True;
        Ruangan.__count += 1
        #print ('CTOR Ruangan', self.__nama_ruangan)

    def copy(self):
        Ruangan.__count += 1
        #print ('CCTOR Ruangan', self.__nama_ruangan)
        return copy.deepcopy(self)

    def __del__ (self):
        #print ('DTOR Ruangan', self.__nama_ruangan)
        Ruangan.__count -= 1

#GETTER
    def getNamaRuangan(self):
        return self.__nama_ruangan

    def getJamMulai(self):
        return self.__jam_mulai

    def getJamSelesai(self):
        return self.__jam_selesai

    def getListOfAvailableHari(self):
        return self.__list_of_available_hari

    def getCount():
        return Ruangan.__count

#METHOD
    def __str__(self):
        return """{}
Jam Mulai               : {}
Jam Selesai             : {}
List hari yang tersedia : {}""".format (self.getNamaRuangan(),
self.getJamMulai(), self.getJamSelesai(), self.getListOfAvailableHari())

    def isHariAvailable(self, n):
        if n < 0 or n > 4:
            return False
        else:
            return self.__list_of_available_hari[n]
