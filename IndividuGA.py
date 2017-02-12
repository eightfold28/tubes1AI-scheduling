#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from SelGA import *

class IndividuGA:
#KONSTRUKTOR
    def __init__ (self):
        self.__individu = []
        self.__fitness = 0
        self.__normalizedFV = 0.0
        self.__accumulated = 0.0

    def isiIndividu(self, daftar_jadwal, daftar_ruangan):
        i = 0
        for item in daftar_jadwal:
            self.__individu.append(SelGA())
            self.__individu[i].isiSel(item, daftar_ruangan)
            i = i + 1

        self.__fitness = self.fitnessFunction()

#GETTER
    def getIndividu(self):
        return self.__individu

    def getSelByIndex(self, index):
    #fungsi untuk mengembalikan satu blok mata kuliah
        return self.__individu[index]

    def getFitness(self):
        return self.__fitness

    def getNormalizedFV(self):
        return self.__normalizedFV

    def getAccumulated(self):
        return self.__accumulated

#SETTER
    def setNormalizedFV(self, value):
        self.__normalizedFV = value

    def setIndividuByIndex(self, index, attr):
        self.__individu[index] = attr;

    def setAccumulated(self, value):
        self.__accumulated = value

    def appendToIndividu(self, item):
        self.__individu.append(item)
        self.__fitness = self.fitnessFunction()

#METHOD
    def printAttribute(self, index):
    #print atribut sebuah matkul pada index tertentu
    #format: [NamaMatkul, Ruangan, Hari, Durasi, JamMulai, JamSelesai]
        matakuliah = self.__individu[index]
        print("[{0}, {1}, {2}, {3}, {4}, {5}]".format(matakuliah.getNamaMatkul(), matakuliah.getRuangan(), matakuliah.getHari(), matakuliah.getDurasi(), matakuliah.getJamMulai(), matakuliah.getJamSelesai()))

    def printIndividu(self):
    #print seluruh elemen pada IndividuGA
        for i in range(len(self.__individu)):
            self.printAttribute(i)
        print("\n")

    def numConflict(self):
    #menghitung banyaknya konflik yang terjadi
        count = 0;
        for i in range(len(self.__individu)-1):
            for j in range((i+1), len(self.__individu)):
                if ((self.__individu[i].getRuangan() == self.__individu[j].getRuangan()) and (self.__individu[i].getHari() == self.__individu[j].getHari())):
                #dua matkul berada di ruangan dan hari yang sama
                    if (self.__individu[i].getJamMulai() == self.__individu[j].getJamMulai()):
                    #dua matkul memiliki jam mulai yang sama
                        count = count + 1
                    elif (self.__individu[i].getJamMulai() < self.__individu[j].getJamMulai()):
                    #jam mulai matkul pertama lebih dahulu daripada matkul kedua
                        if (self.__individu[i].getJamSelesai() > self.__individu[j].getJamMulai()):
                        #matkul pertama belum selesai saat matkul kedua dimulai
                            count = count + 1
                    else:
                    #jam mulai matkul pertama lebih akhir daripada matkul kedua
                        if (self.__individu[i].getJamMulai() < self.__individu[j].getJamSelesai()):
                        #matkul pertama mulai saat matkul kedua belum selesai
                            count = count + 1
        return count

    def fitnessFunction(self):
        #menghitung fitness function dari setiap individu
        length = len(self.__individu) - 1
        MAX_CONFLICT = 0
        for i in range(len(self.__individu)):
            MAX_CONFLICT = MAX_CONFLICT + length
            length = length - 1

        conflict = self.numConflict()
        result = MAX_CONFLICT - conflict
        return result
