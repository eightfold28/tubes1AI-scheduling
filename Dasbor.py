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

class Dasbor:
    def __init__(self, master):
        self.frame = Frame(master)

        self.label_nama_file = Label(self.frame, text='Nama File')
        self.entry_nama_file = Entry(self.frame)
        self.label_pilihan_algoritma = Label(self.frame, text='Pilihan Algoritma')
        self.radiobutton_hill_climbing_search = Radiobutton(self.frame, text='Hill Climbing Search')
        self.radiobutton_simulated_annealing = Radiobutton(self.frame, text='Simulated Annealing')
        self.radiobutton_genetic_algorithm = Radiobutton(self.frame, text='Genetic Algorithm')
        self.button_reset = Button(self.frame, text='Reset')
        self.button_arrange = Button(self.frame, text='Arrange')
        self.label_total_jadwal_bentrok = Label(self.frame, text='Total Jadwal Bentrok: ')
        self.label_angka_jadwal_bentrok = Label(self.frame, text='0')
        self.label_persentase_ruangan = Label(self.frame, text='Persentase Keefektifan Penggunaan Ruangan: ')
        self.label_angka_persentase = Label(self.frame, text='0%')
        self.label_iterasi_maksimal = Label(self.frame, text='Iterasi Maksimal')
        self.entry_iterasi_maksimal = Entry(self.frame)
        self.label_T = Label(self.frame, text='T')
        self.entry_T = Entry(self.frame)
        self.label_Tmin = Label(self.frame, text='Tmin')
        self.entry_Tmin = Entry(self.frame)
        self.label_alpha = Label(self.frame, text='alpha')
        self.entry_alpha = Entry(self.frame)

    def show(self):
        self.label_nama_file.grid(row=0, column=0, sticky=W)
        self.entry_nama_file.grid(row=0, column=1)
        self.label_pilihan_algoritma.grid(row=1, column=0, sticky=W)
        self.radiobutton_hill_climbing_search.grid(row=1, column=1, sticky=W)
        self.radiobutton_simulated_annealing.grid(row=2, column=1, sticky=W)
        self.radiobutton_genetic_algorithm.grid(row=3, column=1, sticky=W)
        self.button_reset.grid(row=4, column=0)
        self.button_arrange.grid(row=4, column=1)

        self.label_total_jadwal_bentrok.grid(row=0, column=4, sticky=E)
        self.label_angka_jadwal_bentrok.grid(row=0, column=5, sticky=W)
        self.label_persentase_ruangan.grid(row=1, column=4, sticky=E)
        self.label_angka_persentase.grid(row=1, column=5, sticky=W)

        self.label_iterasi_maksimal.grid(row=0, column=2, sticky=W)
        self.entry_iterasi_maksimal.grid(row=0, column=3)
        self.label_T.grid(row=1, column=2, sticky=W)
        self.entry_T.grid(row=1, column=3)
        self.label_Tmin.grid(row=2, column=2, sticky=W)
        self.entry_Tmin.grid(row=2, column=3)
        self.label_alpha.grid(row=3, column=2, sticky=W)
        self.entry_alpha.grid(row=3, column=3)
        self.frame.pack(side=LEFT)
