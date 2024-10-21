# MEMBUAT KODE PROGRAM DARI FLOWCHART PADA PERTEMUAN KE-5
<li>Tugas pertemuan ke 5</li>
<li>NAMA: Mochammad Hafilla Dasuki</li>
<li>Kelas: TI 24 A3</li>
<li>NIM: 312410375</li>
# 1.BILANGAN TERBESAR DI PRGRAM PHYTON
Program pertama yang di buat untuk menampilkan bilangan terbesar dari 3 bilangan

berikut flowchartnya :
<img width="385" alt="flowchartprogram1" src="https://github.com/user-attachments/assets/aaa130da-5cc4-4a2a-9464-9d9df93e9011">
program akan diminta untuk memasukan 3 angka untuk di bandingkan:
<img width="797" alt="outputprogram1" src="https://github.com/user-attachments/assets/3dcf732a-e072-4d9c-94e2-cf9f25b7effc">
Penjelasan code 
<img width="395" alt="code1" src="https://github.com/user-attachments/assets/e6da71e7-4142-437d-b6ec-46d0f6dea837">
misalkan ada 3 buah bilangan yaitu bilangan (a,b,c)
contoh:
bilangan A : 1
bilangan B : 2
bilangan C : 3
maka C = 3 yaitu bilangan terbesar
bilangan A : 2
bilangan B : 3
bilangan C : 1
maka B = 3 yaitu bilangan terbesar
bilangan A : 5
bilangan B : 3
bilangan C : 1
maka A = 5 yaitu bilangan terbesar
Algoritma :
Deklarasi :
 a,b,c terbesar = integer
Deskripsi :
 read(a,b,c)
if(a>b) and (a>c) then
terbesar <--a
Else :
If b>c then
Terbesar <--b
Else :
Terbesar <--c
Endif
Endif
Write(terbesar)
# 2.BILANGAN N PADA PROGRAM PHYTON
Program Kedua adalah untuk membandingkan bilangan yang di Input, input akan terus berjalan kecuali user memasukkan nilai 0
Flowchartnya :
<img width="377" alt="flowchartprogram2" src="https://github.com/user-attachments/assets/15b0f6f4-5336-419b-bd10-4ec39aa4bb2a">
Program akan meminta kita untuk memasukkan angka untuk dibandingkan, `input akan terus diminta sebelum user memasukkan angka 0 :
<img width="796" alt="outputprogram2" src="https://github.com/user-attachments/assets/6acd1eed-153d-4e75-a915-8e7229b88063">
Penjelasan codenya:
<img width="518" alt="code2" src="https://github.com/user-attachments/assets/d570251b-2ba3-426a-aa1f-bb874af2cf77">
Algoritma :
 Mulai
 Inisialisasi: Tetapkan angka terbesar = -Tak terhingga
 Input bilangan_input
 Apakah bilangan_input valid ?
 Tidak: print(bilangan input harus angka) lalu continue ke langkah ke 3
 Ya: Lanjutkan ke langkah selanjut nya
 Apakah bilangan inputan = 0
 Ya: print ( bilangan terbesar ) ,lalu selesai
 Tidak: apakah bilangan inputan > bilangan bilangan terbesar ?
 Tidak: repeat ke langkah ke 3
 Ya: lalu output kan bilangan terbesar = bilangan input,dan repeat ke langkah 3




