import sys

#masukkan token (misal aba, abb, aaaba, abbaaa)
token = input("Masukkan token : ")
panjangToken = len(token)

# membuat array untuk menampung semua state berdasarkan panjang karakter token
allState = [''] * (panjangToken + 1)

# State awalan diisi A (sesuai gambar)
allState[0] = 'A'

#jika karakter awal token bukan a maka token ditolak, state terakhir adalah A
#jika sebaliknya, maka state selanjutnya adalah B
if token[0] != 'a':
    print("Token ditolak")
    print("State : ")
    print(allState[0])
    sys.exit(0)
else :
    allState[1] = 'B'

    # cek karakter token selanjutnya
    i = 1
    while i in range(panjangToken):

        #jika karakter token selanjutnya a dan state sebelumnya B
        if token[i] == 'a' and allState[i] == 'B' :
            #maka state berikutnya adalah B
            allState[i+1] = 'B'
        
        #jika karakter token selanjutnya a dan state sebelumnya C
        elif token[i] == 'a' and allState[i] == 'C' :
            #maka state berikutnya adalah D
            allState[i+1] = 'D'
        
        #jika karakter token selanjutnya b dan state sebelumnya B
        elif token[i] == 'b' and allState[i] == 'B' :
            #maka state berikutnya adalah C
            allState[i+1] = 'C'
        
        #jika karakter token selanjutnya a dan state sebelumnya D
        elif token[i] == 'a' and allState[i] == 'D' :
            #maka state berikutnya adalah D
            allState[i+1] = 'D'
        
        #jika karakter token selanjutnya b dan state sebelumnya C
        elif token[i] == 'b' and allState[i] == 'C' :
            #maka state berikutnya tidak ada, dan langsung keluar dari perulangan
            break
        
        #jika kondisi diatas tidak terpenuhi, token ditolak
        else :
            print("Token ditolak")
            sys.exit(0)
        
        i += 1

    #keluarkan semua state
    print("State : ")
    for j in range(panjangToken+1):
        print(allState[j], sep=' ',end =' ')

#tampilkan pernyataan token diterima apabila state berakhir di D
if allState[panjangToken] != 'D' :
    print("Token ditolak")
else :
    print("Token diterima")