
max = int(input("jumlah bintang: "))
for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()
    
max = int(input("jumlah bintang: "))
for i in range(max):
    for j in range(i):
        print(" ", end=" ")
    for k in range(max - i):
        print("*", end=" ")
    print()
    
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    
    match operator:
        case "+":
            hasil = a + b
            print(f"hasil dari {a} + {b} = {hasil}")
        case "-":
            hasil = a - b
            print(f"Hasil dari {a} - {b} = {hasil}")
        case "*":
            hasil = a + b
            print(f"Hasil dari {a} * {b} = {hasil}")
        case "/":
            if b != 0:
                hasil = a / b
                print(f"Hasil dari {a} / {b} = {hasil}")
            else:
                print("Error: Pembagian dengan nol tidak bisa")
        case _:
                print("Operator tidak dikenal!")
            