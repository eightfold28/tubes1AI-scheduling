#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from Ruangan import *
from Jadwal import *
from FileReader import *

class CSP:
#STATIC
    __count = 0

#CTOR CCTOR DTOR
    def __init__ (self, filename):
        self.__jumlah_conflict = 0
        self.__jumlah_conflict1 = 0
        self.__jumlah_conflict2 = 0
        self.__list_of_ruangan = []
        self.__list_of_jadwal = []

        FR1 = FileReader(filename)
        FR1.openFile()
        FR1.splitList()
        FR1.parseInfo()
        FR1.formatListType()

        for item in FR1.getListOfRuangan():
            self.__list_of_ruangan.append(Ruangan(item[0],item[1],item[2],item[3]))

        for item in FR1.getListOfJadwal():
            self.__list_of_jadwal.append(Jadwal(item[0],item[1],item[2],item[3],item[4],item[5]))

        CSP.__count += 1

    def copy (self):
        CSP.__count += 1
        return copy.deepcopy(self)

    def __del__ (self):
        CSP.__count -= 1

#GETTER
    def getJumlahConflict(self):
        return self.__jumlah_conflict

    def getJumlahConflict1(self):
        return self.__jumlah_conflict1

    def getJumlahConflict2(self):
        return self.__jumlah_conflict2

    def getListOfRuangan(self):
        return self.__list_of_ruangan

    def getRuangan(self, index):
        return self.__list_of_ruangan[index]

    def getRuanganByNama(self, nama):
        for ruangan in self.getListOfRuangan():
            if ruangan.getNamaRuangan() == nama:
                return ruangan

    def getListOfJadwal(self):
        return self.__list_of_jadwal

    def getJadwal(self, index):
        return self.__list_of_jadwal[index]

    def getJadwalByNama(self, nama):
        for jadwal in self.getListOfJadwal():
            if jadwal.getNamaKegiatan() == nama:
                return jadwal

    def getCount():
        return CSP.__count

    def getIndexRuangan(self, nama_ruangan):
        for index in range(len(self.__list_of_ruangan)):
            if nama_ruangan == self.getRuangan(index).getNamaRuangan():
                return index
        return -1

    def getIndexJadwal(self, nama_kegiatan):
        for index in range(len(self.__list_of_jadwal)):
            if nama_kegiatan == self.getJadwal(index).getNamaKegiatan():
                return index
        return -1

#SETTER
    def setJumlahConflict(self, jml):
        self.__jumlah_conflict = jml

    def setJumlahConflict1(self, jml):
        self.__jumlah_conflict1 = jml

    def setJumlahConflict2(self, jml):
        self.__jumlah_conflict2 = jml

    def setListOfRuangan(self, list_of_ruangan):
        self.__list_of_ruangan = list_of_ruangan

    def setListOfJadwal(self, list_of_jadwal):
        self.__list_of_jadwal = list_of_jadwal

#METHOD
    def isConstraintSatisfied_1 (self, index):
        'Jadwal.JamSelesai - Jadwal.JamAwal = Jadwal.Durasi'
        jadwal = self.getJadwal(index)
        if jadwal.getJamSelesai() - jadwal.getJamMulai() == jadwal.getDurasi():
            return True
        else:
            self.getJadwal(index).setJamMulaiConflictStatus(True)
            self.getJadwal(index).setJamSelesaiConflictStatus(True)
            return False

    def isConstraintSatisfied_2 (self, index_ruangan, index_jadwal):
        'Ruangan.Hari harus tersedia untuk Jadwal'
        ruangan = self.getRuangan(index_ruangan)
        jadwal = self.getJadwal(index_jadwal)

        if ruangan.getNamaRuangan() == jadwal.getNamaRuangan():
            if ruangan.isHariAvailable(jadwal.getHari()):
                return True
            else:
                self.getJadwal(index_jadwal).setHariConflictStatus(True)
                return False
        else:
            return True

    def isConstraintSatisfied_3 (self, index_ruangan, index_jadwal):
        'Jadwal.JamMulai >= Ruangan.JamMulai'
        ruangan = self.getRuangan(index_ruangan)
        jadwal = self.getJadwal(index_jadwal)

        if ruangan.getNamaRuangan() == jadwal.getNamaRuangan():
            if jadwal.getJamMulai() >= ruangan.getJamMulai():
                return True
            else:
                self.getJadwal(index_jadwal).setJamMulaiConflictStatus(True)
                return False
        else:
            return True

    def isConstraintSatisfied_4 (self, index_ruangan, index_jadwal):
        'Jadwal.JamSelesai <= Ruangan.JamSelesai'
        ruangan = self.getRuangan(index_ruangan)
        jadwal = self.getJadwal(index_jadwal)

        if ruangan.getNamaRuangan() == jadwal.getNamaRuangan():
            if jadwal.getJamSelesai() <= ruangan.getJamSelesai():
                return True
            else:
                self.getJadwal(index_jadwal).setJamSelesaiConflictStatus(True)
                return False
        else:
            return True

    def isConstraintSatisfied_5 (self, index_jadwal_1, index_jadwal_2):
        """   jadwal_1    jadwal_2
                        ============
            ============
        """
        jadwal_1 = self.getJadwal(index_jadwal_1)
        jadwal_2 = self.getJadwal(index_jadwal_2)

        if jadwal_1.getNamaKegiatan() != jadwal_2.getNamaKegiatan() and jadwal_1.getHari() == jadwal_2.getHari() and jadwal_1.getNamaRuangan() == jadwal_2.getNamaRuangan():
            if jadwal_1.getJamMulai() < jadwal_2.getJamMulai():
                if jadwal_1.getJamSelesai() <= jadwal_2.getJamMulai():
                    return True
                else:
                    self.getJadwal(index_jadwal_1).setJamSelesaiConflictStatus(True)
                    self.getJadwal(index_jadwal_2).setJamMulaiConflictStatus(True)
                    return False
            else:
                return True
        else:
            return True

    def isConstraintSatisfied_6 (self, index_jadwal_1, index_jadwal_2):
        """   jadwal_1    jadwal_2
            ============
                        ============
        """
        jadwal_1 = self.getJadwal(index_jadwal_1)
        jadwal_2 = self.getJadwal(index_jadwal_2)

        if jadwal_1.getNamaKegiatan() != jadwal_2.getNamaKegiatan() and jadwal_1.getHari() == jadwal_2.getHari() and jadwal_1.getNamaRuangan() == jadwal_2.getNamaRuangan():
            if jadwal_1.getJamMulai() >= jadwal_2.getJamMulai():
                if jadwal_1.getJamMulai() >= jadwal_2.getJamSelesai():
                    return True
                else:
                    self.getJadwal(index_jadwal_1).setJamMulaiConflictStatus(True)
                    self.getJadwal(index_jadwal_2).setJamSelesaiConflictStatus(True)
                    return False
            else:
                return True
        else:
            return True

    def hitungConflict(self):
        for index_jadwal in range(len(self.getListOfJadwal())):
            self.getJadwal(index_jadwal).setRuanganConflictStatus(False)
            self.getJadwal(index_jadwal).setHariConflictStatus(False)
            self.getJadwal(index_jadwal).setJamMulaiConflictStatus(False)
            self.getJadwal(index_jadwal).setJamSelesaiConflictStatus(False)

        temp = 0

        for index_jadwal in range(len(self.getListOfJadwal())):
            if not(self.isConstraintSatisfied_1(index_jadwal)):
                temp += 1

        for index_ruangan in range(len(self.getListOfRuangan())):
            for index_jadwal in range(len(self.getListOfJadwal())):
                if not(self.isConstraintSatisfied_2(index_ruangan, index_jadwal)):
                    temp += 1

                if not(self.isConstraintSatisfied_3(index_ruangan, index_jadwal)):
                    temp += 1

                if not(self.isConstraintSatisfied_4(index_ruangan, index_jadwal)):
                    temp += 1

        for index_jadwal_1 in range(len(self.getListOfJadwal()[:len(self.getListOfJadwal())-1])):
            for index_jadwal_2 in range(index_jadwal_1+1,len(self.getListOfJadwal())):
                if not(self.isConstraintSatisfied_5(index_jadwal_1, index_jadwal_2)):
                    temp += 1

                if not(self.isConstraintSatisfied_6(index_jadwal_1, index_jadwal_2)):
                    temp += 1

        self.setJumlahConflict(temp)

    def hitungConflict1(self):
        for index_jadwal in range(len(self.getListOfJadwal())):
            self.getJadwal(index_jadwal).setRuanganConflictStatus(False)
            self.getJadwal(index_jadwal).setHariConflictStatus(False)
            self.getJadwal(index_jadwal).setJamMulaiConflictStatus(False)
            self.getJadwal(index_jadwal).setJamSelesaiConflictStatus(False)

        temp = 0

        for index_jadwal in range(len(self.getListOfJadwal())):
            if not(self.isConstraintSatisfied_1(index_jadwal)):
                temp += 1

        for index_ruangan in range(len(self.getListOfRuangan())):
            for index_jadwal in range(len(self.getListOfJadwal())):
                if not(self.isConstraintSatisfied_2(index_ruangan, index_jadwal)):
                    temp += 1

                if not(self.isConstraintSatisfied_3(index_ruangan, index_jadwal)):
                    temp += 1

                if not(self.isConstraintSatisfied_4(index_ruangan, index_jadwal)):
                    temp += 1

        self.setJumlahConflict1(temp)

    def hitungConflict2(self):
    #menghitung banyaknya konflik yang terjadi
        count = 0;
        for i in range(len(self.getListOfJadwal())-1):
            for j in range((i+1), len(self.getListOfJadwal())):
                if ((self.getListOfJadwal()[i].getNamaRuangan() == self.getListOfJadwal()[j].getNamaRuangan()) and (self.getListOfJadwal()[i].getHari() == self.getListOfJadwal()[j].getHari())):
                #dua matkul berada di ruangan dan hari yang sama
                    if (self.getListOfJadwal()[i].getJamMulai() == self.getListOfJadwal()[j].getJamMulai()):
                    #dua matkul memiliki jam mulai yang sama
                        count = count + 1
                    elif (self.getListOfJadwal()[i].getJamMulai() < self.getListOfJadwal()[j].getJamMulai()):
                    #jam mulai matkul pertama lebih dahulu daripada matkul kedua
                        if (self.getListOfJadwal()[i].getJamSelesai() > self.getListOfJadwal()[j].getJamMulai()):
                        #matkul pertama belum selesai saat matkul kedua dimulai
                            count = count + 1
                    else:
                    #jam mulai matkul pertama lebih akhir daripada matkul kedua
                        if (self.getListOfJadwal()[i].getJamMulai() < self.getListOfJadwal()[j].getJamSelesai()):
                        #matkul pertama mulai saat matkul kedua belum selesai
                            count = count + 1

        self.setJumlahConflict2(count)

    def hitungEfisiensi(self):
        #hitung jumlah slot
        jmlslot = 0
        for ruangan in self.getListOfRuangan():
            durasi = ruangan.getJamSelesai() - ruangan.getJamMulai()
            for isHariAvailable in ruangan.getListOfAvailableHari():
                if isHariAvailable:
                    jmlslot += durasi

        #hitung jumlah slot yang terisi
        jmljadwal = 0
        for ruangan in self.getListOfRuangan():
            for index_hari in range(len(ruangan.getListOfAvailableHari())):
                if ruangan.isHariAvailable(index_hari):
                    for index_jam in range(ruangan.getJamMulai(), ruangan.getJamSelesai()):
                        for jadwal in self.getListOfJadwal():
                            if jadwal.getNamaRuangan() == ruangan.getNamaRuangan() and jadwal.getHari() == index_hari and index_jam >= jadwal.getJamMulai() and index_jam < jadwal.getJamSelesai():
                                jmljadwal += 1
                                break
                                
        return (jmljadwal/jmlslot)
