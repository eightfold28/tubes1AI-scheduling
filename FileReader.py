#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

import re

class FileReader:
    def __init__(self, filename):
        self.__filename = filename
        self.__list_of_ruangan = []
        self.__list_of_jadwal = []
        self.__nRuangan = 0
        self.__nJadwal = 0

    def timeToInt (self, t):
    #fungsi untuk mwngubah waktu (string) menjadi integer (misal "07.00" --> 7)
    #pre-requisite: tidak ada elemen menit pada waktu
        num = t[:2]
        num = int(num)
        return num

    def openFile (self):
        file_object = open(self.__filename, 'r')

        for line in file_object:
            self.__list_of_ruangan.append(line)
            self.__nJadwal += 1

        self.__list_of_ruangan.pop(0) #hapus elemen yang berisi "Ruangan"
        for index in self.__list_of_ruangan:
            if (index != '\n'):
                self.__nRuangan += 1
            else:
                break

        self.__nJadwal -= self.__nRuangan - 3
        self.__list_of_ruangan.pop(self.__nRuangan) #hapus elemen yang berisi "\n"
        self.__list_of_ruangan.pop(self.__nRuangan) #hapus elemen yang berisi "Jadwal"

    def splitList (self):
        for item in self.__list_of_ruangan[self.__nRuangan:]:
            self.__list_of_jadwal.append(item)

        for item in self.__list_of_ruangan[self.__nRuangan:]:
            self.__list_of_ruangan.pop()

    def parseInfo (self):
        #Parsing berdasarkan ';'
        for index in range(len(self.__list_of_ruangan)):
            temp = re.split('[;]+', (''+self.__list_of_ruangan[index]).rstrip('\n'))
            self.__list_of_ruangan[index] = temp

        for index in range(len(self.__list_of_jadwal)):
            temp = re.split('[;]+', (''+self.__list_of_jadwal[index]).rstrip('\n'))
            self.__list_of_jadwal[index] = temp

        #Parsing berdasarkan ','
        for index in range(len(self.__list_of_ruangan)):
            temp = re.split('[,]+', (''+self.__list_of_ruangan[index][3]))
            self.__list_of_ruangan[index][3] = temp #elemen hari

        for index in range(len(self.__list_of_jadwal)):
            temp = re.split('[,]+', (''+self.__list_of_jadwal[index][1]))
            self.__list_of_jadwal[index][1] = temp #elemen ruangan
            temp = re.split('[,]+', (''+self.__list_of_jadwal[index][5]))
            self.__list_of_jadwal[index][5] = temp #elemen hari

    def formatListType (self):
        for i in range(len(self.__list_of_ruangan)):
            self.__list_of_ruangan[i][1] = self.timeToInt(self.__list_of_ruangan[i][1]) #waktu mulai
            self.__list_of_ruangan[i][2] = self.timeToInt(self.__list_of_ruangan[i][2]) #waktu selesai
            for k in range(len(self.__list_of_ruangan[i][3])):
                self.__list_of_ruangan[i][3][k] = int(self.__list_of_ruangan[i][3][k]) #hari

        for i in range(len(self.__list_of_jadwal)):
            self.__list_of_jadwal[i][2] = self.timeToInt(self.__list_of_jadwal[i][2]) #waktu mulai
            self.__list_of_jadwal[i][3] = self.timeToInt(self.__list_of_jadwal[i][3]) #waktu selesai
            self.__list_of_jadwal[i][4] = int(self.__list_of_jadwal[i][4])
            for k in range(len(self.__list_of_jadwal[i][5])):
                self.__list_of_jadwal[i][5][k] = int(self.__list_of_jadwal[i][5][k]) #hari

        temp = []
        for ruangan in self.__list_of_ruangan:
            temp.append(ruangan[0])

        for i in range(len(self.__list_of_jadwal)):
            if self.__list_of_jadwal[i][1][0] == '-':
                self.__list_of_jadwal[i][1] = temp

#GETTER
    def getListOfRuangan (self):
        return self.__list_of_ruangan

    def getListOfJadwal (self):
        return self.__list_of_jadwal
