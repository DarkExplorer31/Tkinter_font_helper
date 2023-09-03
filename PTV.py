from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

tkint_police = [
    "System",
    "Terminal",
    "Fixedsys",
    "Modern",
    "Roman",
    "Script",
    "Courier",
    "MS Serif",
    "MS Sans Serif",
    "Small Fonts",
    "Marlett",
    "Arial",
    "Arabic Transparent",
    "Arial Baltic",
    "Arial CE",
    "Arial CYR",
    "Arial Greek",
    "Arial TUR",
    "Arial Black",
    "Bahnschrift Light",
    "Bahnschrift SemiLight",
    "Bahnschrift",
    "Bahnschrift SemiBold",
    "Bahnschrift Light SemiCondensed",
    "Bahnschrift SemiLight SemiConde",
    "Bahnschrift SemiCondensed",
    "Bahnschrift SemiBold SemiConden",
    "Bahnschrift Light Condensed",
    "Bahnschrift SemiLight Condensed",
    "Bahnschrift Condensed",
    "Bahnschrift SemiBold Condensed",
    "Calibri",
    "Calibri Light",
    "Cambria",
    "Cambria Math",
    "Candara",
    "Candara Light",
    "Comic Sans MS",
    "Consolas",
    "Constantia",
    "Corbel",
    "Corbel Light",
    "Courier New",
    "Courier New Baltic",
    "Courier New CE",
    "Courier New CYR",
    "Courier New Greek",
    "Courier New TUR",
    "Ebrima",
    "Franklin Gothic Medium",
    "Gabriola",
    "Gadugi",
    "Georgia",
    "Impact",
    "Ink Free",
    "Javanese Text",
    "Leelawadee UI",
    "Leelawadee UI Semilight",
    "Lucida Console",
    "Lucida Sans Unicode",
    "Malgun Gothic",
    "@Malgun Gothic",
    "Malgun Gothic Semilight",
    "@Malgun Gothic Semilight",
    "Microsoft Himalaya",
    "Microsoft JhengHei",
    "@Microsoft JhengHei",
    "Microsoft JhengHei UI",
    "@Microsoft JhengHei UI",
    "Microsoft JhengHei Light",
    "@Microsoft JhengHei Light",
    "Microsoft JhengHei UI Light",
    "@Microsoft JhengHei UI Light",
    "Microsoft New Tai Lue",
    "Microsoft PhagsPa",
    "Microsoft Sans Serif",
    "Microsoft Tai Le",
    "Microsoft YaHei",
    "@Microsoft YaHei",
    "Microsoft YaHei UI",
    "@Microsoft YaHei UI",
    "Microsoft YaHei Light",
    "@Microsoft YaHei Light",
    "Microsoft YaHei UI Light",
    "@Microsoft YaHei UI Light",
    "Microsoft Yi Baiti",
    "MingLiU-ExtB",
    "@MingLiU-ExtB",
    "PMingLiU-ExtB",
    "@PMingLiU-ExtB",
    "MingLiU_HKSCS-ExtB",
    "@MingLiU_HKSCS-ExtB",
    "Mongolian Baiti",
    "MS Gothic",
    "@MS Gothic",
    "MS UI Gothic",
    "@MS UI Gothic",
    "MS PGothic",
    "@MS PGothic",
    "MV Boli",
    "Myanmar Text",
    "Nirmala UI",
    "Nirmala UI Semilight",
    "Palatino Linotype",
    "Segoe MDL2 Assets",
    "Segoe Print",
    "Segoe Script",
    "Segoe UI",
    "Segoe UI Black",
    "Segoe UI Emoji",
    "Segoe UI Historic",
    "Segoe UI Light",
    "Segoe UI Semibold",
    "Segoe UI Semilight",
    "Segoe UI Symbol",
    "SimSun",
    "@SimSun",
    "NSimSun",
    "@NSimSun",
    "SimSun-ExtB",
    "@SimSun-ExtB",
    "Sitka Small",
    "Sitka Text",
    "Sitka Subheading",
    "Sitka Heading",
    "Sitka Display",
    "Sitka Banner",
    "Sylfaen",
    "Symbol",
    "Tahoma",
    "Times New Roman",
    "Times New Roman Baltic",
    "Times New Roman CE",
    "Times New Roman CYR",
    "Times New Roman Greek",
    "Times New Roman TUR",
    "Trebuchet MS",
    "Verdana",
    "Webdings",
    "Wingdings",
    "Yu Gothic",
    "@Yu Gothic",
    "Yu Gothic UI",
    "@Yu Gothic UI",
    "Yu Gothic UI Semibold",
    "@Yu Gothic UI Semibold",
    "Yu Gothic Light",
    "@Yu Gothic Light",
    "Yu Gothic UI Light",
    "@Yu Gothic UI Light",
    "Yu Gothic Medium",
    "@Yu Gothic Medium",
    "Yu Gothic UI Semilight",
    "@Yu Gothic UI Semilight",
    "HoloLens MDL2 Assets",
    "BIZ UDGothic",
    "@BIZ UDGothic",
    "BIZ UDPGothic",
    "@BIZ UDPGothic",
    "BIZ UDMincho Medium",
    "@BIZ UDMincho Medium",
    "BIZ UDPMincho Medium",
    "@BIZ UDPMincho Medium",
    "Meiryo",
    "@Meiryo",
    "Meiryo UI",
    "@Meiryo UI",
    "MS Mincho",
    "@MS Mincho",
    "MS PMincho",
    "@MS PMincho",
    "UD Digi Kyokasho N-B",
    "@UD Digi Kyokasho N-B",
    "UD Digi Kyokasho NP-B",
    "@UD Digi Kyokasho NP-B",
    "UD Digi Kyokasho NK-B",
    "@UD Digi Kyokasho NK-B",
    "UD Digi Kyokasho N-R",
    "@UD Digi Kyokasho N-R",
    "UD Digi Kyokasho NP-R",
    "@UD Digi Kyokasho NP-R",
    "UD Digi Kyokasho NK-R",
    "@UD Digi Kyokasho NK-R",
    "Yu Mincho",
    "@Yu Mincho",
    "Yu Mincho Demibold",
    "@Yu Mincho Demibold",
    "Yu Mincho Light",
    "@Yu Mincho Light",
    "DengXian",
    "@DengXian",
    "DengXian Light",
    "@DengXian Light",
    "FangSong",
    "@FangSong",
    "KaiTi",
    "@KaiTi",
    "SimHei",
    "@SimHei",
    "Ubuntu",
    "Raleway",
    "Ubuntu Condensed",
    "Ubuntu Light",
]

# Creer la fenetre secondaire
window1 = Tk()

# Définitions des liens utilisés
lien_absolu = os.path.abspath(__file__)
direction_vers_le_dossier = os.path.dirname(lien_absolu)
os.chdir(direction_vers_le_dossier)
lien_font = "Font.png"

# Personnaliser la fenetre
window1.title("Programme de Visualisation des Police Tkinter")
window1.geometry("600x300")
window1.minsize(600, 300)
window1.configure(background="#224466")

# Reparamètrage à partir des dimensions de l'image (Fond d'écran)
img = PhotoImage(file=lien_font)
w = img.width()
h = img.height()
window1.geometry("%dx%d+0+0" % (w, h))

# Création du Canvas
can_page_1 = Canvas(window1, width=w, height=h, bg="black")
can_page_1.create_image(0, 0, anchor=NW, image=img)
can_page_1.place(x=0, y=0, relwidth=1, relheight=1)

# Le titre:
lab1 = Label(
    can_page_1,
    text="Bienvenue sur le programme de Visualisation de Police Tkinter",
    font=("Courrier", 45),
    bg="#224466",
    fg="deepskyblue2",
)
lab1.pack(pady=10)
can_page_1.create_window(w / 2, 50, window=lab1)

# Création de la Listbox
list_principal = Listbox(
    can_page_1,
    font=("Courrier", 30),
    bg="#224466",
    fg="deepskyblue2",
    height=4,
    activestyle="dotbox",
    selectbackground="deepskyblue2",
    selectforeground="#224466",
)
list_principal.pack()
can_page_1.create_window(w / 2, 250, window=list_principal)

# Ajout de la Scollbar vertical
scrollbarV = Scrollbar(can_page_1, orient="vertical")
scrollbarV.pack(side=RIGHT, fill=BOTH)
can_page_1.create_window(w - 730, 250, window=scrollbarV, height=200)

# Ajout des variables
pas = 0
for pas in range(len(tkint_police)):
    list_principal.insert(pas, tkint_police[pas])
    pas += 1
list_principal.config(yscrollcommand=scrollbarV.set)
scrollbarV.config(command=list_principal.yview)


# Création de la fonction pour le bouton
def liste_fonc():
    result = list_principal.get(list_principal.curselection())
    message = "Texte de Test de la police sélectionner"
    rep_info.delete(0, END)
    rep_info.insert(0, message)
    rep_info.configure(font=(result, 40))


# Boutton pour chercher le lien du dossier
but_aide = Button(
    can_page_1,
    text="Tester la police",
    command=liste_fonc,
    font=("Courrier", 25),
    fg="#224466",
    bg="deepskyblue2",
)
but_aide.pack()
can_page_1.create_window(w / 2, 450, window=but_aide)

# Parametrage du widget d'info
rep_info = Entry(
    can_page_1,
    textvariable=liste_fonc,
    font=("Courrier", 40),
    bg="#224466",
    fg="white",
    relief=FLAT,
)
rep_info.pack(pady=10)
can_page_1.create_window(w / 2, 750, width=1200, window=rep_info)

window1.mainloop()
