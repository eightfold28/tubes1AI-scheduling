#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

import random
from IndividuGA import *
import math

class PopulasiGA:
#KONSTRUKTOR
    def __init__ (self):
        self.__populasi = []

    def isiPopulasi (self, daftar_jadwal, daftar_ruangan):
        i = 0
        for item in range(len(daftar_jadwal) * len(daftar_ruangan)):
            self.__populasi.append(IndividuGA())
            self.__populasi[i].isiIndividu(daftar_jadwal, daftar_ruangan)
            i = i + 1

#GETTER
    def getPopulasi(self):
        return self.__populasi

    def getIndividuByIndex(self, index):
    	return self.__populasi[index]

#METHOD
    def appendToPopulasi(self, item):
        self.__populasi.append(item)

    def selection(self):
        temp = PopulasiGA()
        minim = IndividuGA()
        total = 0
        #cari nilai normalized value
        for i in range(len(self.__populasi)):
            total += self.getIndividuByIndex(i).getFitness()
        for k in range(len(self.__populasi)):
            prob = self.getIndividuByIndex(k).getFitness() / total
            self.getIndividuByIndex(k).setNormalizedFV(prob)

        #sorting nilai fitness
        for j in range(len(self.__populasi)):
            minim = self.getIndividuByIndex(j)
            for i in range((j+1), len(self.__populasi)):
                if (self.getIndividuByIndex(i).getNormalizedFV() > minim.getNormalizedFV()):
                    minim = self.getIndividuByIndex(i)
                    self.__populasi[j], self.__populasi[i] = self.__populasi[i], self.__populasi[j]

        #bikin accumulated value
        acc = 0.0
        for l in range(len(self.__populasi)):
            acc += self.getIndividuByIndex(l).getNormalizedFV()
            self.getIndividuByIndex(l).setAccumulated(acc)

        #core selection
        copyPopulasi = copy.deepcopy(self)
        selected = PopulasiGA()
        for item in range(len(self.__populasi)):
            v_random = random.uniform(0, 1)
            selected = copyPopulasi.getIndividuByIndex(item)
            for isi in range(len(self.__populasi)):
                if (copyPopulasi.getIndividuByIndex(isi).getAccumulated() > v_random):
                    self.__populasi[item] = copyPopulasi.getIndividuByIndex(isi)
                    break

    def crossOver(self):
        x = 0
        y = 1
        for i, j in zip(self.__populasi[0::2], self.__populasi[1::2]):
            panjang1 = randint(0, len(i.getIndividu()))
            panjang2 = len(i.getIndividu()) - panjang1
            individu1 = IndividuGA()
            for k in range(panjang1):
                individu1.appendToIndividu(i.getSelByIndex(k))
            for l in range(panjang2):
                individu1.appendToIndividu(j.getSelByIndex(panjang1+l))
            individu2 = IndividuGA()
            for m in range(panjang2):
                individu2.appendToIndividu(i.getSelByIndex(panjang1+m))
            for n in range(panjang1):
                individu2.appendToIndividu(j.getSelByIndex(n))

            self.__populasi[x] = individu1
            self.__populasi[y] = individu2

            x = x + 2
            y = y + 2

    def mutasi(self, csp):
        for i in range(len(self.__populasi)):
            r_mutasi = randint(0,1)
            if (r_mutasi == 1):
                rand_mutasi = randint(0, len(self.__populasi[0].getIndividu())-1)
                namaMatkul = self.getIndividuByIndex(i).getSelByIndex(rand_mutasi).getNamaMatkul()
                jadwal = csp.getJadwal(csp.getIndexJadwal(namaMatkul))
                self.__populasi[i].getSelByIndex(rand_mutasi).isiSel(jadwal, csp.getListOfRuangan())

    def cekKonflikPopulasi(self):
        i = 0
        minConflict = self.__populasi[0].numConflict()
        idxMin = 0
        for i in range(1, len(self.__populasi)):
            currentConflict = self.__populasi[i].numConflict()
            if (currentConflict < minConflict):
                minConflict = currentConflict
                idxMin = i
                if (minConflict == 0):
                    break

        return minConflict, idxMin

    def assignToCSP(self, solution, CSP):
        for i in range(len(solution.getIndividu())):
            CSP.getListOfJadwal()[i].setNamaKegiatan(solution.getSelByIndex(i).getNamaMatkul())
            CSP.getListOfJadwal()[i].setRuanganSpecial(solution.getSelByIndex(i).getRuangan())
            CSP.getListOfJadwal()[i].setHariSpecial(solution.getSelByIndex(i).getHari())
            CSP.getListOfJadwal()[i].setJamMulaiSpecial(solution.getSelByIndex(i).getJamMulai())
            CSP.getListOfJadwal()[i].setJamSelesaiSpecial(solution.getSelByIndex(i).getJamSelesai())
            CSP.getListOfJadwal()[i].setDurasi(solution.getSelByIndex(i).getDurasi())
