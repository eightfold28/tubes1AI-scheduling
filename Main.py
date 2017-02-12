#!/usr/bin/python3

"""
FANDA YULIANA PUTRI     13514023
DHARMA KURNIA SEPTIALOKA    13514028
MUHAMMAD KAMAL NADJIEB  13514054
HISHSHAH GHASSANI       13514056
ARNETTHA SEPTINEZ       13514093
"""
from CSP import *
from Dasbor import *
from JadwalRuangan import *
from JadwalKegiatan import *
from HillClimbing import *
from PopulasiGA import *
from SimulatedAnnealing import *

class Main:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame_top = Frame(self.frame)
        self.frame_body = Frame(self.frame)
        self.csp = None
        self.kegiatan_botton = None
        self.nama_kegiatan = None
        self.pilihan_algoritma = IntVar()
        self.list_of_jadwal_ruangan = []
        self.list_of_jadwal_kegiatan = []

        self.dasbor = Dasbor(self.frame_top)
        self.dasbor.radiobutton_hill_climbing_search.config(variable=self.pilihan_algoritma, value=0)
        self.dasbor.radiobutton_simulated_annealing.config(variable=self.pilihan_algoritma, value=1)
        self.dasbor.radiobutton_genetic_algorithm.config(variable=self.pilihan_algoritma, value=2)
        self.dasbor.button_arrange.bind('<Button-1>', self.arrange)
        self.dasbor.button_reset.bind('<Button-1>', self.reset)

    def show(self):
        self.dasbor.show()
        self.frame_top.pack(side=TOP, expand=True, fill=X)
        self.frame.grid(row=0, column=0)

    def arrange(self, event):
        self.frame_body.pack_forget()
        self.frame_body = Frame(self.frame)
        self.csp = None
        self.list_of_jadwal_ruangan = []
        self.list_of_jadwal_kegiatan = []

        self.csp = CSP(self.dasbor.entry_nama_file.get())

        if self.pilihan_algoritma.get() == 0:
            schedule = Schedule()
            hill = HillClimbing()
            hill.algorithm(schedule, self.csp, int(self.dasbor.entry_iterasi_maksimal.get()))
        elif self.pilihan_algoritma.get() == 1:
            Schedule1 = Schedule()
            Schedule1.inisialisasi(self.csp)
            SimulatedAnnealing1 = SimulatedAnnealing(float(self.dasbor.entry_T.get()), float(self.dasbor.entry_Tmin.get()), float(self.dasbor.entry_alpha.get()))
            SimulatedAnnealing1.inisialisasi(Schedule1, self.csp)
        elif self.pilihan_algoritma.get() == 2:
            for i in range(int(self.dasbor.entry_iterasi_maksimal.get())):
                PopulasiGA1 = PopulasiGA()
                PopulasiGA1.isiPopulasi(self.csp.getListOfJadwal(), self.csp.getListOfRuangan())
                PopulasiGA1.selection()
                PopulasiGA1.crossOver()
                PopulasiGA1.mutasi(self.csp)
                konflikMinimal, idxMinimal = PopulasiGA1.cekKonflikPopulasi()
                self.csp.setJumlahConflict2(konflikMinimal)
                if (konflikMinimal == 0):
                    break
            PopulasiGA1.assignToCSP(PopulasiGA1.getIndividuByIndex(idxMinimal), self.csp)

        self.dasbor.label_angka_jadwal_bentrok.config(text=str(self.csp.getJumlahConflict2()))
        self.dasbor.label_angka_persentase.config(text=str(self.csp.hitungEfisiensi()*100)+'%')

        for ruangan in self.csp.getListOfRuangan():
            self.list_of_jadwal_ruangan.append(JadwalRuangan(self.frame_body, ruangan))

        for kegiatan in self.csp.getListOfJadwal():
            self.list_of_jadwal_kegiatan.append(JadwalKegiatan(self.list_of_jadwal_ruangan, kegiatan))

        #BINDING
        for jadwal_ruangan in self.list_of_jadwal_ruangan:
            for index_baris in range (2,13):
                for index_kolom in range (1,6):
                    frame_jadwal_ruangan = jadwal_ruangan.matrix_of_frame_jadwal_ruangan[index_baris][index_kolom]
                    frame_jadwal_ruangan.bind('<Button-1>', lambda event, a=jadwal_ruangan, b=index_baris, c=index_kolom: self.pindah_jadwal(a,b,c))

        for jadwal_kegiatan in self.list_of_jadwal_kegiatan:
            for button in jadwal_kegiatan.list_of_button:
                button.bind('<Button-1>', lambda event, a=button.cget('text'), b=jadwal_kegiatan: self.pilih_kegiatan(a,b))

        #SHOW
        for jadwal_ruangan in self.list_of_jadwal_ruangan:
            jadwal_ruangan.show()

        for jadwal_kegiatan in self.list_of_jadwal_kegiatan:
            jadwal_kegiatan.show()

        self.frame_body.pack(side=TOP, expand=True)

    def reset(self, event):
        self.frame_body.pack_forget()
        self.frame_body = Frame(self.frame)
        self.csp = None
        self.list_of_jadwal_ruangan = []
        self.list_of_jadwal_kegiatan = []

    def pilih_kegiatan(self, nama_kegiatan, kegiatan_button):
        self.nama_kegiatan = nama_kegiatan
        self.kegiatan_button = kegiatan_button

    def pindah_jadwal(self, jadwal_ruangan, index_jam_mulai, index_hari):
        kegiatan = self.csp.getJadwalByNama(self.nama_kegiatan)
        ruangan = self.csp.getRuanganByNama(jadwal_ruangan.label_nama_ruangan.cget('text'))

        kegiatan.setRuanganSpecial(ruangan.getNamaRuangan())
        kegiatan.setJamMulaiSpecial(index_jam_mulai+5)
        kegiatan.setJamSelesaiSpecial(kegiatan.getJamMulai()+kegiatan.getDurasi())
        kegiatan.setHariSpecial(index_hari-1)

        if kegiatan.getJamSelesai() <= 18:
            self.kegiatan_button.remove()
            self.list_of_jadwal_kegiatan.remove(self.kegiatan_button)
            temp = JadwalKegiatan(self.list_of_jadwal_ruangan, kegiatan)
            self.list_of_jadwal_kegiatan.append(temp)
            temp.show()

        for jadwal_kegiatan in self.list_of_jadwal_kegiatan:
            for button in jadwal_kegiatan.list_of_button:
                button.bind('<Button-1>', lambda event, a=button.cget('text'), b=jadwal_kegiatan: self.pilih_kegiatan(a,b))

        self.nama_kegiatan = None
        self.kegiatan_button = None

#PROGRAM UTAMA
root = Tk()
root.title('Scheduler')
frame = Frame(width="1000", height="1000")
frame.pack()
swin = ScrolledWindow(frame, width=1000, height=1000)
swin.pack()
win = swin.window

main = Main(win)
main.show()

root.mainloop()
