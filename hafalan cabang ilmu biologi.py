import os
try:
	import random
except:
    os.system("pip install random2")
try:	
	from colorama import Fore, Style, init
except:
    os.system("pip install colorama")
init(convert=True)

print("\n==============")
print("Tools Menghafal")
print("Rumus Refleksi dan Rotasi")
print("By eskaerpe")
print("============================")
print("Ketik 00 untuk mengakhiri\n")
materi = {
    # pertanyaan : jawaban
	"Bentuk luar organisme" : "Morfologi",
	"Struktur dalam dari organisme" : "Anatomi",
	"Struktur sel dan fungsinya" : "Sitologi",
	"Tingkat jaringan tubuh" : "Histology",
	"Hereditas dan permasalahannya" : "Genetika",
	"Jantung manusia" : "Kardiologi",
	"Paru-paru manusia" : "Pulmonologi",
	"Proses yang terjadi di dalam tubuh (faal) mencakup fungsi-fungsi organ" : "Fisiologi",
	"System saraf manusia" : "Neurologi",
	"System pencernaan manusia" : "Gastrologi",
	"System endokrin/ hormonal" : "Endokrinologi",
	"System reproduksi wanita" : "Ginekologi",
	"System reproduksi pria" : "Andrologi",
	"Virus" : "Virologi",
	"Bakteri" : "Bakteriologi",
	"Fungi/ jamur" : "Mikologi",
	"Tanaman" : "Botani",
	"Caplak, tungau" : "Acaralogi",
	"Insekta" : "Entomologi",
	"Ikan" : "Iktiologi",
	"Reptile dan amphibi" : "Herpetologi",
	"Unggas" : "Ornithologi",
	"Parasit" : "Parasitologi",
	"Mollusca" : "Malakologi",
	"Cacing- cacing parasit" : "Helminthologi",
	"Nematode" : "Nematologi",
	"Paku-pakuan" : "Pteridologi",
	"Lumut-lumutan" : "Bryologi",
	"Alga" : "Algologi",
	"Protozoa" : "Protozoologi",
	"Mamalia" : "Mamologi",
	"Kehamilan" : "Obstetri",
	"Pertumbuhan di masa embrio mulai dari zigot" : "Embriologi",
	"Kemungkinan cacat pada fetus (janin)" : "Terratologi",
	"Hubungan antara makhluk hidup dan lingkungannya" : "Ekologi",
	"Fosil dari hewan dan tumbuhan" : "Fosil dari hewan dan tumbuhan",
	"Organisme mikroskopik" : "Mikrobiologi",
	"Klasifikasi organism berdasarkan persamaan dan perbedaannya" : "Taksonomi",
	"Perilaku hewanPerilaku hewan" : "Ethologi",
	"Penyakit pada anak-anak" : "Pediatric",
	"Kesehatan melalui pendekatan lingkungannya" : "Sanitasi",
	"Kesehatan melalui pendekatan perilaku" : "Hygiene",
	"Kanker" : "Onkologi",
	"Pertanian" : "Agronomi",
	"Perkembangan di masa bayi" : "Perinatologi",
	"Kekebalan tubuh" : "Immunologi",
	"Perkembangan filum makhluk hidup dari yang paling sederhana sampai yang paling kompleks" : "Filogeni",
	"Diagnosa penyakit menggunakan x-ray" : "Radiologi",
	"Tingkat organ tubuh" : "Organologi",
	"Hewan" : "Zoologi",
}
print(type(materi))
while 1:
    random_key = random.choice(list(materi.keys())) 
    soal = f"{random_key} ({materi[random_key][0:3]}) -> "
    jawaban = str(input(soal))
    
    if jawaban.lower() == materi[random_key].lower():
        print(Fore.GREEN+"Benar"+Style.RESET_ALL)
        print(f"{materi[random_key]} is deleted")
        del materi[random_key]
    elif jawaban == "00":
        exit(0)
    else:
        print(Fore.RED+"Salah"+Style.RESET_ALL+f" yang benar adalah {Fore.GREEN}{materi[random_key]}{Style.RESET_ALL}")
        
    
    

# echo "# Cabang-Ilmu-Biologi" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/eskaerpe/Cabang-Ilmu-Biologi.git
# git push -u origin main