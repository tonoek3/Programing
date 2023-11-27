class CD:
    def __init__(self, autor, album, canciones):
        self.autor = autor
        self.album = album
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.album} del cantante {self.autor} con {self.canciones} canciones."

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("El disco ha sido eliminado")



mi_cd = CD("Bad Bunny", "YHLQMDLG", 16)
print(mi_cd)

del mi_cd

