bilangan_terbesar = float('-inf') # inisialisasi bilangan terbesar 

while True:
    bilangan_input = input('Masukkan angka: ')
    
    try: 
        input_number = float(bilangan_input) 
    except ValueError: 
        print("Bilangan input harus angka")
        continue 
    
    if (float(bilangan_input) == 0):
        print('bilangan terbesar adalah', bilangan_terbesar)
        break
    
    if (float(bilangan_input) > bilangan_terbesar): 
        bilangan_terbesar = float(bilangan_input)
        