def soalenam(a):
    kalimat = {i for i in a}
    panjang = [len(i) for i in kalimat]
    print(f'Jumlah karakter terbanyak adalah sebesar {max(panjang)} karakter')
    for i in kalimat:
        if len(i) == max(panjang):
            print(f'Karakter yang berjumlah {max(panjang)} adalah {i}')

user = input().split() 
soalenam(user)
