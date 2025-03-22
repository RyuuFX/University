while True :            
    print ("<==============================>")
    print ("|    Menentukan Minat Siswa    |")
    print ("<==============================>")
    print ("1. Tentukan Minat")
    print ("2. Selesai")
    pilihan = int(input("Masukkan pilihan : "))
    
    if pilihan == 1:
        from minat import cihuy
        cihuy()
    elif pilihan == 2: 
        print("Terimakasih Sudah Mencoba Program Ini")
        break
    else:
        print("Pilihan tidak valid!")