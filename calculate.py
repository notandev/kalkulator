
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b


print("Kalkulator python by andpe")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:
    choice = input("Pilih Salah Satu (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan Angka pertama: "))
        num2 = float(input("Masukkan Angka kedua: "))

        if choice == '1':
            print(num1, "+", num2, "=", tambah(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", kurang(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", kali(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", bagi(num1, num2))
        
        next_calculation = input("Menghitung lagi? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Invalid Input")