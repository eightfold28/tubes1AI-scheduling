#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""

from tkinter import *
from tkinter.tix import *

class JadwalRuangan:
    def __init__(self, master, ruangan):
        self.frame = Frame(master)
        self.matrix_of_frame_jadwal_ruangan = [[0 for x in range(6)] for x in range(13)]
        for index_baris in range(13):
            for index_kolom in range(6):
                self.matrix_of_frame_jadwal_ruangan[index_baris][index_kolom] = Frame(self.frame)
                if index_baris >= 2 and index_kolom >= 1:
                    self.matrix_of_frame_jadwal_ruangan[index_baris][index_kolom].config(width=50, height=50)

        for index_baris in range(2,13):
            self.matrix_of_frame_jadwal_ruangan[index_baris][0].config(bg='black')

        self.label_nama_ruangan = Label(self.matrix_of_frame_jadwal_ruangan[0][1], text=ruangan.getNamaRuangan())

        self.list_of_label_hari = [  Label(self.matrix_of_frame_jadwal_ruangan[1][1], text='Senin'),
                                Label(self.matrix_of_frame_jadwal_ruangan[1][2], text='Selasa'),
                                Label(self.matrix_of_frame_jadwal_ruangan[1][3], text='Rabu'),
                                Label(self.matrix_of_frame_jadwal_ruangan[1][4], text='Kamis'),
                                Label(self.matrix_of_frame_jadwal_ruangan[1][5], text='Jumat')  ]

        self.list_of_label_jam = [   Label(self.matrix_of_frame_jadwal_ruangan[2][0], text='07.00-08.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[3][0], text='08.00-09.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[4][0], text='09.00-10.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[5][0], text='10.00-11.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[6][0], text='11.00-12.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[7][0], text='12.00-13.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[8][0], text='13.00-14.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[9][0], text='14.00-15.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[10][0], text='15.00-16.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[11][0], text='16.00-17.00'),
                                Label(self.matrix_of_frame_jadwal_ruangan[12][0], text='17.00-18.00')   ]

    def show(self):
        self.label_nama_ruangan.pack()

        for item in self.list_of_label_hari:
            item.pack()

        for item in self.list_of_label_jam:
            item.pack()

        for index_baris in range(13):
            for index_kolom in range(6):
                if index_baris == 0 and index_kolom == 1:
                    self.matrix_of_frame_jadwal_ruangan[index_baris][index_kolom].grid(row=index_baris, column=index_kolom, sticky=N+S, columnspan=5)
                else:
                    self.matrix_of_frame_jadwal_ruangan[index_baris][index_kolom].grid(row=index_baris, column=index_kolom, sticky=N+S)

        self.frame.pack(side=LEFT)
