import pandas as pd #import library pandas
from view.wellcometxt import welcome_txt
from sys import stdout
from view.banner import banners
from view.colors import Colors


def iheadache(): # mendefinisikan function iheadache atau main function
    """Fungsi utama program""" 

    data_pasien = [] #list

    banners()

    while True: #perulangan while
        
        #Wellcome Text
        welcome_txt()

        #input data pasien
        namaPasien = input("{:<3}{:^10}".format('🥼',f'{Colors.CBLUE2}{Colors.RED}Masukan Nama Pasien :  {Colors.ENDC}')) #var inputan nama pasien 
        umurPasien = input("{:<5}{:^10}".format('⚕️',f'{Colors.CBLUE2}{Colors.RED}Masukan Usia Pasien : {Colors.ENDC}')) #var inputan umur pasien
        print('=' * 51) 

        #diagnosa penyakit & pertanyaan gejalanya
        gejalaSakit = [] #list kosong untuk menyimpan gejala penyakit seperti pusing,kepala berdenyut, dll

        gejala = input(f"{Colors.GREEN}Apakah anda mengalami pusing atau sakit kepala? (y/n){Colors.ENDC}").lower() #fungsi lower untuk merubah segala macam inputan menjadi huruf kecil 
        if gejala == "y": #percabangan
            gejalaSakit.append("Pusing")#menggunakan function append untuk menambahkan anggota kedalam list gejala sakit
        else:
            print("Maaf mungkin anda tidak mengalami sakit kepala ringan, silahkan cek lebih lanjut kerumah sakit")
        break
        #Gejala migrain
        gejala = input(f"{Colors.CBLUE2}Apakah anda mengalami kepala berdenyut-denyut? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Kepala Berdenyut")#menggunakan function append untuk menambahkan anggota kedalam list gejala sakit

        gejala = input(f"{Colors.CBLUE2}Apakah anda mengalami sensitif terhadap cahaya dan bunyi? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Sensitif Cahaya")
        
        gejala = input(f"{Colors.CBLUE2}Apakah anda mengalami pandangan kabur ? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Pandangan Kabur")

        #gejala hipertensi / kepala tegang
        gejala = input(f"{Colors.CRED2}Apakah anda mengalami durasi sakit kepala lebih dari 30 menit hingga 7 hari? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Kepala Tegang")
        
        gejala = input(f"{Colors.CRED2}Apakah anda mengalami rasa mual? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Mual")

        #gejala sakit kepala belakang / neuragia okspital
        gejala = input(f"{Colors.GREEN}Apakah anda mengalami sakit kepala bagian belakang berdenyut? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Neuragia Okspital")
        
        gejala = input(f"{Colors.GREEN}Apakah anda mengalami nyeri tajam di leher atau kulit kepala? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Nyeri Leher")
        
        #gejala sinus
        gejala = input(f"{Colors.CBLUE2}Apakah anda mengalami rasa nyeri pada bagian wajah? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Nyeri Wajah")
        
        gejala = input(f"{Colors.CBLUE2}Apakah anda mengalami rasa sakit pada telinga? (y/n){Colors.ENDC}").lower()
        if gejala == "y":
            gejalaSakit.append("Tekanan Telinga")


        #jika memiliki riwayat penyakit berat
        #membuat var riwayat penyakit
        riwayatPenyakit = input("Apakah anda memiliki riwayat penyakit berat sebelumnya ? (y/n)").lower()
        print('=' * 51)
        #hasil dari diagnosa penyakit & mengelola jawaban dari pertanyaan
        hasilDiagnosis = []

        if "Pusing" in gejalaSakit: # menggunakan percabangan if, operator(keanggotaan) in jika suatu var ditemukan atau termasuk didalam list atau data
            if "Kepala Berdenyut" in gejalaSakit or "Sensitif Cahaya" in gejalaSakit: # penggunaan operator(logika) or pendefinisian atau 
                hasilDiagnosis = "Migrain"
            elif "Pandangan Kabur" in gejalaSakit or "Kepala Tegang" in gejalaSakit or "Mual" in gejalaSakit:
                hasilDiagnosis = "Hipertensi"
            elif "Neuragia Okspital" in gejalaSakit or "Nyeri Leher" in gejalaSakit:
                hasilDiagnosis = "Neuralgia Oksipital"
            elif "Nyeri Wajah" in gejalaSakit or "Tekanan Telinga" in gejalaSakit:
                hasilDiagnosis = "Sinusitis"
            else:
                print("Tidak ada gejala yang cocok,silahkan konsultasi lebih lanjut dengan dokter")

        #print atau output data
        print(f"\n{Colors.GREEN}---- Hasil Diagnosa Penyakit Iheadache ----{Colors.ENDC}")
        print("Nama Pasien : ", namaPasien) #menggabungkan string
        print("Umur Pasien : "+ str(umurPasien)) #merubah inputan int menjadi string menggunakan str()
        print("Hasil Diagnosa : ", hasilDiagnosis)

        #saran dari masing masing diagnosa atau penyakit
        if hasilDiagnosis == "Migrain":
            print(f"{Colors.CBLUE2}Saran dan penanganan pertama : {Colors.ENDC}")
            print("1. Kompress air hangat atau dingin")
            print("2. Cari tempat yang tenang untuk istrirahat")
            print("3. Memperbanyak konsumsi air mineral")
            if riwayatPenyakit == "y":
                print("- jika ada riwayat penyakit berat sebelumnya silahkan konsuldasikan ke dokter atau datang kerumah sakit untuk evaluasi lebih lanjut🏥")
        elif hasilDiagnosis == "Hipertensi":
            print(f"{Colors.GREEN}Saran dan penanganan pertama : {Colors.ENDC}")
            print("1. Mengurangi konsumsi garam")
            print("2. Istirahat yang cukup")
            print("3. Hindari Stress dan rileks")
            if riwayatPenyakit == "y":
                print("- jika ada riwayat penyakit berat sebelumnya silahkan konsuldasikan ke dokter atau datang kerumah sakit untuk evaluasi lebih lanjut🏥")
        elif hasilDiagnosis == "Neuralgia Oksipital":
            print(f"{Colors.CRED2}Saran dan penanganan pertama : {Colors.ENDC}")
            print("1. Istirahat yang cukup 7-8 jam sehari")
            print("2. Hindari konsumsi alkohol & rokok")
            print("3. Melakukan peregangan agar otot leher tidak kaku")
            if riwayatPenyakit == "y":
                print("- jika ada riwayat penyakit berat sebelumnya silahkan konsuldasikan ke dokter atau datang kerumah sakit untuk evaluasi lebih lanjut🏥")
        elif hasilDiagnosis == "Sinusitis":
            print(f"{Colors.CBLUE2}Saran dan penanganan pertama : {Colors.ENDC}")
            print("1. Hirup uap hangat")
            print("2. Perbanyak istirahat dan minum air putih")
            print("3. Lakukan bilas hidung")
            if riwayatPenyakit == "y":
                print("- jika ada riwayat penyakit berat sebelumnya silahkan konsuldasikan ke dokter atau datang kerumah sakit untuk evaluasi lebih lanjut🏥")

        #pertanyaan lanjutan untuk proses diagnosa
        prosesDiagnosa = input("\nApakah anda ingin melanjutkan diagnosa lagi ? (y/n)").lower()
        if prosesDiagnosa != 'y':
            print(f"{Colors.GREEN}👋🏼Terimakasih semoga lekas sembuh👋🏼{Colors.ENDC}")
            break #statement untuk memaksa program keluar dari blok looping
        
        #jika melanjutkan proses diagnosa maka hasil diagnosa sebelumnya akan tercatat
        data_pasien.append({"Nama Pasien": namaPasien, "Usia Pasien": umurPasien, "Hasil Diagnosa": hasilDiagnosis})

        #Data frame pandas
        hasilData_pasien = pd.DataFrame(data_pasien) # format data pandas data frame

        #menampilkan data frame
        print(f"{Colors.CBLUE2}\n---- Data Pasien ----{Colors.ENDC}")
        print(hasilData_pasien) # mencetak hasil dari variable data pandas

if __name__ == "__main__": # menjalankan skrip level teratas
    iheadache() #memanggil function


                

