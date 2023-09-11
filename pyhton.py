from email.policy import default


class BangunDatar:
    nama=""
    panjang=0
    lebar=0
    atas=0
    alas=0
    tinggi=0
    jari_jari=0
    def luas():
        pass


class Persegi(BangunDatar):
    nama="Persegi"
    def luas(self):
        if self.panjang == 0:
            return "Dimensi panjang belum ditentukan!"
        return self.panjang*self.panjang
    def setPanjang(self,panjang):
        self.panjang=panjang


class PersegiPanjang(BangunDatar):
    nama="Persegi Panjang"
    def luas(self):
        if self.panjang == 0:
            return "Dimensi panjang belum ditentukan!"
        if self.lebar == 0:
            return "Dimensi lebar belum ditentukan!"
        return self.panjang*self.lebar
    def setPanjang(self,panjang):
        self.panjang=panjang
    def setLebar(self,lebar):
        self.lebar=lebar


class Segitiga(BangunDatar):
    nama="Segitiga"
    def luas(self):
        if self.alas == 0:
            return "Dimensi alas belum ditentukan!"
        if self.tinggi == 0:
            return "Dimensi tinggi belum ditentukan!"
        return self.alas*self.tinggi/2
    def setAlas(self,alas):
        self.alas=alas
    def setTinggi(self,tinggi):
        self.tinggi=tinggi
        

class Lingkaran(BangunDatar):
    nama="Lingkaran"
    def luas(self):
        if self.jari_jari == 0:
            return "Dimensi jari-jari belum ditentukan!"
        return 3.14*self.jari_jari*self.jari_jari
    def setJariJari(self,jari_jari):
        self.jari_jari=jari_jari


class Trapesium(BangunDatar):
    nama="Trapesium"
    def luas(self):
        if self.atas == 0:
            return "Dimensi atas belum ditentukan!"
        if self.alas == 0:
            return "Dimensi alas belum ditentukan!"
        if self.tinggi == 0:
            return "Dimensi tinggi belum ditentukan!"
        return (self.atas+self.alas)/2*self.tinggi
    def setAlas(self,alas):
        self.alas=alas
    def setAtas(self,atas):
        self.atas=atas
    def setTinggi(self,tinggi):
        self.tinggi=tinggi

bangun_datar=[]
jumlah=int(input("Masukkan jumlah bangun datar: "))
print(f"Jumlah bangun datar yang dimasukan: {jumlah}\n")
index=1
while index < jumlah+1 :
    bangun=None
    nama_bangun_datar=input(f"[{index}] Masukkan nama bangun datar: ").lower()
    match nama_bangun_datar:
        case "persegi":
            bangun=Persegi()
            panjang=int(input("Masukkan panjang: "))
            bangun.setPanjang(panjang)
            print(f"Bangun datar: {nama_bangun_datar} berhasil ditambahkan\n")
        case "persegi panjang" | "persegipanjang":
            bangun=PersegiPanjang()
            panjang=int(input("Masukkan panjang: "))
            bangun.setPanjang(panjang)
            lebar=int(input("Masukkan lebar: "))
            bangun.setLebar(lebar)
            print(f"Bangun datar: {nama_bangun_datar} berhasil ditambahkan\n")
        case "segitiga":
            bangun=Segitiga()
            alas=int(input("Masukkan alas: "))
            bangun.setAlas(alas)
            tinggi=int(input("Masukkan tinggi: "))
            bangun.setTinggi(tinggi)
            print(f"Bangun datar: {nama_bangun_datar} berhasil ditambahkan\n")
        case "lingkaran":
            bangun=Lingkaran()
            jari_jari=int(input("Masukkan jari-jari: "))
            bangun.setJariJari(jari_jari)
            print(f"Bangun datar: {nama_bangun_datar} berhasil ditambahkan\n")
        case "trapesium":
            bangun=Trapesium()
            alas=int(input("Masukkan alas: "))
            bangun.setAlas(alas)
            atas=int(input("Masukkan atas: "))
            bangun.setAtas(atas)
            tinggi=int(input("Masukkan tinggi: "))
            bangun.setTinggi(tinggi)
            print(f"Bangun datar: {nama_bangun_datar} berhasil ditambahkan\n")
        case _:
            print(f"Tidak ada bangun {nama_bangun_datar}!\nUlangi!\n")
            index-=1
    index+=1
    bangun_datar.append(bangun)
bangun_datar.sort(key=lambda x: x.luas(),reverse=True)
print("Urutan bangun datar berdasarkan luas")
for index in range(jumlah):
    bangun=bangun_datar[index]
    print(f"[{index}] Nama bangun: {bangun.nama}  Luas: {bangun.luas()}")