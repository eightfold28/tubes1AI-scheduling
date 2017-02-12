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

class JadwalKegiatan:
    counter = 0;
    list_of_color = ['PaleTurquoise4', 'LightSkyBlue1', 'light coral', 'SteelBlue3',
    'midnight blue', 'yellow3', 'PaleVioletRed4', 'DarkSeaGreen2', 'pale green', 'burlywood1',
    'DarkOrchid2', 'alice blue', 'VioletRed1', 'goldenrod2', 'AntiqueWhite2', 'gray34', 'green4',
    'pink2', 'green2', 'gray27', 'DarkOrange1', 'gray35', 'linen', 'RosyBrown4', 'lawn green',
    'LightSteelBlue1', 'MistyRose3', 'SkyBlue3', 'light blue', 'dark slate gray', 'gray83', 'gray70',
    'SlateGray2', 'MediumPurple1', 'orange2', 'salmon1', 'sienna1', 'gray99', 'gray', 'aquamarine2',
    'gray50', 'cornsilk2', 'light grey', 'red4', 'AntiqueWhite3', 'coral2', 'SlateBlue4', 'gold3',
    'tomato3', 'maroon4', 'purple3', 'gray61', 'gray52', 'LightGoldenrod2', 'light slate blue', 'gainsboro',
    'turquoise4', 'gray46', 'bisque4', 'gray30', 'LightYellow3', 'gray98', 'gold4', 'thistle3', 'seashell4',
    'goldenrod', 'cyan4', 'LavenderBlush4', 'CadetBlue1', 'SeaGreen2', 'DarkOliveGreen3', 'PaleGreen3',
    'sandy brown', 'olive drab', 'gray60', 'gray12', 'gray79', 'gray10', 'slate blue', 'IndianRed3', 'gray89',
    'OliveDrab2', 'gray84', 'gray94', 'gray51', 'tomato', 'MediumPurple4', 'gray5', 'medium blue', 'SlateBlue3',
    'rosy brown', 'PaleTurquoise1', 'red3', 'LightSalmon4', 'pink3', 'seashell2', 'dark slate blue',
    'antique white', 'LightSteelBlue3', 'dark salmon', 'NavajoWhite4', 'LightBlue4', 'SteelBlue4', 'gray26',
    'DarkOliveGreen4', 'gray54', 'purple4', 'bisque3', 'DodgerBlue2', 'DeepSkyBlue3', 'PeachPuff3', 'sienna3',
    'DeepSkyBlue4', 'gray81', 'NavajoWhite2', 'bisque', 'gray21', 'snow4', 'khaki4', 'gray2', 'gray91',
    'brown4', 'gray20', 'papaya whip', 'HotPink2', 'coral4', 'yellow4', 'SeaGreen1', 'OrangeRed2', 'CadetBlue2',
    'lavender', 'dark orange', 'steel blue', 'SlateGray3', 'gray48', 'DarkSlateGray3', 'LavenderBlush2',
    'LightPink2', 'LightGoldenrod3', 'honeydew2', 'PeachPuff4', 'gray33', 'gray73', 'VioletRed2', 'DeepPink4',
    'dark violet', 'firebrick3', 'coral1', 'khaki', 'ghost white', 'gray76', 'DarkGoldenrod4', 'deep pink',
    'blue violet', 'PaleTurquoise3', 'green3', 'RoyalBlue4', 'wheat3', 'pink4', 'aquamarine4', 'gray71',
    'DarkSlateGray4', 'AntiqueWhite1', 'gray6', 'turquoise2', 'plum4', 'gray1', 'salmon', 'SeaGreen3', 'IndianRed2',
    'gray55', 'pale violet red', 'sienna4', 'khaki3', 'LightYellow4', 'dodger blue', 'gray66', 'magenta3',
    'DarkSeaGreen4', 'DeepPink3', 'wheat1', 'purple1', 'coral3', 'gray80', 'gray9', 'MediumOrchid1', 'SkyBlue2',
    'gray87', 'blue2', 'turquoise', 'gray65', 'goldenrod1', 'gray22', 'purple', 'dark khaki', 'medium orchid',
    'saddle brown', 'HotPink3', 'gray31', 'DarkSeaGreen1', 'honeydew3', 'goldenrod4', 'orchid4', 'green yellow',
    'blue4', 'deep sky blue', 'HotPink1', 'gray63', 'LightGoldenrod4', 'dark goldenrod', 'DodgerBlue4', 'chartreuse2',
    'thistle2', 'violet red', 'cornsilk3', 'DeepSkyBlue2', 'SpringGreen2', 'old lace', 'wheat2', 'chartreuse3',
    'gray36', 'SlateBlue2', 'DarkOrange2', 'light goldenrod yellow', 'gray43', 'yellow2', 'firebrick1', 'gray29',
    'tomato2', 'plum3', 'snow3', 'honeydew4', 'dark green', 'RosyBrown3', 'tan1', 'gray15', 'slate gray', 'brown2',
    'burlywood3', 'sea green', 'burlywood2', 'blanched almond', 'forest green', 'tomato4', 'gray18', 'PaleGreen4',
    'lime green', 'gray13', 'blue', 'dark olive green', 'misty rose', 'orange3', 'firebrick2', 'gray93', 'peach puff',
    'magenta4', 'HotPink4', 'medium spring green', 'LightSalmon3', 'MistyRose2', 'gray28', 'MistyRose4',
    'medium aquamarine', 'SlateGray4', 'pale goldenrod', 'maroon1', 'LightCyan3', 'gray72', 'gray44', 'plum2',
    'gray68', 'DarkOrchid4', 'royal blue', 'gray77', 'wheat4', 'LightYellow2', 'cornsilk4', 'gray14', 'gray42',
    'gray25', 'salmon4', 'indian red', 'aquamarine', 'gray40', 'LightGoldenrod1', 'LemonChiffon4', 'gray69',
    'cyan2', 'light steel blue', 'PaleVioletRed2', 'mint cream', 'IndianRed1', 'SkyBlue1', 'gray53', 'CadetBlue4',
    'medium sea green', 'brown1', 'thistle4', 'MediumOrchid2', 'thistle', 'chartreuse4', 'DarkSlateGray1',
    'light yellow', 'LightBlue1', 'gray64', 'lemon chiffon', 'LightSalmon2', 'PeachPuff2', 'gray58',
    'light sky blue', 'turquoise3', 'salmon3', 'PaleGreen1', 'VioletRed4', 'gray62', 'chocolate2', 'sienna2',
    'cadet blue', 'SlateGray1', 'SlateBlue1', 'gray24', 'DarkGoldenrod1', 'LemonChiffon2', 'navy', 'dim gray',
    'LightCyan2', 'gray8', 'gray59', 'RosyBrown2', 'DarkSeaGreen3', 'LightPink4', 'SteelBlue2', 'LightSteelBlue2',
    'gray23', 'hot pink', 'lavender blush', 'LightBlue3', 'orange red', 'thistle1', 'medium slate blue', 'DarkGoldenrod3',
    'orange', 'gray86', 'DarkOrange3', 'red', 'DarkOliveGreen1', 'SpringGreen4', 'gray3', 'yellow', 'LightSkyBlue3',
    'gray75', 'seashell3', 'ivory2', 'gray19', 'pink1', 'gray39', 'PaleVioletRed1', 'DodgerBlue3', 'gray45',
    'LemonChiffon3', 'gray11', 'azure2', 'AntiqueWhite4', 'NavajoWhite3', 'DarkSlateGray2', 'gray7', 'OliveDrab1',
    'PaleVioletRed3', 'powder blue', 'maroon3', 'OrangeRed4', 'gray95', 'LightPink3', 'goldenrod3', 'dark turquoise',
    'medium violet red', 'orchid1', 'spring green', 'firebrick4', 'gray74', 'RoyalBlue1', 'DarkOrchid1', 'azure3',
    'RoyalBlue3', 'ivory3', 'orchid3', 'LightSteelBlue4', 'maroon2', 'coral', 'snow2', 'SpringGreen3', 'gold',
    'gray32', 'medium purple', 'MediumPurple2', 'DarkGoldenrod2', 'IndianRed4', 'PaleGreen2', 'gray97', 'burlywood4',
    'pink', 'dark sea green', 'gray78', 'azure4', 'medium turquoise', 'pale turquoise', 'LightPink1', 'VioletRed3',
    'yellow green', 'gray56', 'LightSkyBlue2', 'SkyBlue4', 'gray16', 'cornflower blue', 'gray57', 'light pink',
    'salmon2', 'navajo white', 'light slate gray', 'tan2', 'OliveDrab4', 'light sea green', 'light goldenrod',
    'cyan3', 'chocolate1', 'orchid2', 'gray85', 'RosyBrown1', 'DeepPink2', 'OrangeRed3', 'white smoke', 'orange4',
    'gray47', 'gold2', 'light salmon', 'MediumOrchid4', 'maroon', 'turquoise1', 'gray38', 'floral white',
    'MediumOrchid3', 'RoyalBlue2', 'DarkOliveGreen2', 'brown3', 'CadetBlue3', 'cyan', 'SteelBlue1', 'gray17',
    'gray82', 'LightCyan4', 'gray67', 'magenta2', 'chocolate3', 'bisque2', 'gray37', 'purple2', 'khaki2', 'gray92',
    'LavenderBlush3', 'DarkOrchid3', 'snow', 'gray88', 'plum1', 'tan4', 'MediumPurple3', 'dark orchid', 'azure',
    'gray4', 'DarkOrange4', 'PaleTurquoise2', 'LightSkyBlue4', 'LightBlue2', 'red2', 'gray49', 'khaki1', 'sky blue',
    'ivory4', 'light cyan', 'gray90']

    def __init__(self, list_of_jadwal_ruangan, kegiatan):
        self.list_of_button = []
        kolom_hari = kegiatan.getHari() + 1
        baris_jam_mulai = kegiatan.getJamMulai() - 5
        for jadwal_ruangan in list_of_jadwal_ruangan:
            if jadwal_ruangan.label_nama_ruangan.cget('text') == kegiatan.getNamaRuangan():
                for index_baris in range(baris_jam_mulai, baris_jam_mulai+kegiatan.getDurasi()):
                    self.list_of_button.append(Button(jadwal_ruangan.matrix_of_frame_jadwal_ruangan[index_baris][kolom_hari], text=kegiatan.getNamaKegiatan(), bg=JadwalKegiatan.list_of_color[JadwalKegiatan.counter]))
                if JadwalKegiatan.counter == 478:
                    JadwalKegiatan.counter == 0
                else:
                    JadwalKegiatan.counter += 1
                break

    def show(self):
        for button in self.list_of_button:
            button.pack()

    def remove(self):
        for button in self.list_of_button:
            button.pack_forget()
