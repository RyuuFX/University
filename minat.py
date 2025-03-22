def cihuy():
    while True:
        print("<=========================================>")
        print("  Silahkan Masukkan Minat dan Nilai Siswa  ")
        print("<=========================================>") 
        M = str(input("Minat Siswa (IPA/IPS/Bahasa): ")).strip().lower()
        N_mat = int(input("Nilai Matematika : "))
        N_bio = int(input("Nilai Biologi : "))
        N_fis = int(input("Nilai Fisika : "))
        N_kim = int(input("Nilai Kimia : "))
        N_geo = int(input("Nilai Geografi : "))
        N_eko = int(input("Nilai Ekonomi : "))
        N_sos = int(input("Nilai Sosiologi : "))
        N_bindo = int(input("Nilai Bahasa Indonesia : "))
        N_bing = int(input("Nilai Bahasa Inggris : "))
        N_blain = int(input("Nilai Bahasa Lain : "))
        
        if M == "ipa":
            if N_mat >= 80 and N_bio >= 78 and N_fis >= 78 and N_kim >= 78:
                print("Minat IPA sesuai dengan nilai Anda.")
            else:
                print("Nilai tidak memenuhi syarat untuk IPA. Memeriksa kemungkinan jurusan lain...")
                if N_mat >= 80 and N_geo >= 78 and N_eko >= 80 and N_sos >= 78:
                    print("Disarankan Jurusan IPS.")
                elif N_mat >= 75 and N_bindo >= 80 and N_bing >= 78 and N_blain >= 75:
                    print("Disarankan Jurusan Bahasa.")
                else:
                    print("Tidak ada jurusan yang cocok. Silakan perbaiki nilai Anda.")
        elif M == "ips":
            if N_mat >= 80 and N_geo >= 78 and N_eko >= 80 and N_sos >= 78:
                print("Minat IPS sesuai dengan nilai Anda.")
            else:
                print("Nilai tidak memenuhi syarat untuk IPS. Memeriksa kemungkinan jurusan lain...")
                if N_mat >= 80 and N_bio >= 78 and N_fis >= 78 and N_kim >= 78:
                    print("Disarankan Jurusan IPA.")
                elif N_mat >= 75 and N_bindo >= 80 and N_bing >= 78 and N_blain >= 75:
                    print("Disarankan Jurusan Bahasa.")
                else:
                    print("Tidak ada jurusan yang cocok. Silakan perbaiki nilai Anda.")
        elif M == "bahasa":
            if N_mat >= 75 and N_bindo >= 80 and N_bing >= 78 and N_blain >= 75:
                print("Minat Bahasa sesuai dengan nilai Anda.")
            else:
                print("Nilai tidak memenuhi syarat untuk Bahasa. Memeriksa kemungkinan jurusan lain...")
                if N_mat >= 80 and N_bio >= 78 and N_fis >= 78 and N_kim >= 78:
                    print("Disarankan Jurusan IPA.")
                elif N_mat >= 80 and N_geo >= 78 and N_eko >= 80 and N_sos >= 78:
                    print("Disarankan Jurusan IPS.")
                else:
                    print("Tidak ada jurusan yang cocok. Silakan perbaiki nilai Anda.")
        else:
            print("Minat yang dimasukkan tidak valid. Silakan masukkan IPA, IPS, atau Bahasa.")
        
        lanjut = input("Apakah ingin mencoba lagi? (ya/tidak): ").strip().lower()
        if lanjut == "ya":
            cihuy()
        elif lanjut == "tidak":
            return

