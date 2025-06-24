from module import Faktorial
from module import Fibonacci
from module import MenaraHanoi
from module import clear_terminal as ct

class Main:
    def main():
        while True:
            ct()
            print("="*50)
            print("{:^50}".format("Program Rekursif"))
            print("="*50)
            print("{:^50}".format("A. Faktorial"))
            print("{:^50}".format("B. Fibbonaci"))
            print("{:^50}".format("C. Menara Hanoi"))
            print("="*50)
            inputTipe = input("{:<40}".format("Masukkan Tipe Program [A/B/C] :"))
            if inputTipe == "A" or inputTipe == "a":
                try:
                    inputData = int(input("Masukkan Angka Faktorial [Cth: 4] : "))
                    faktorial = Faktorial(inputData)
                    faktorial.main()
                except TypeError:
                    print("Data yang dimasukkan bukan angka!")
            elif inputTipe == "B" or inputTipe == "b":
                try:
                    inputData = int(input("Masukkan Suku Angka Faktorial [Cth: 4] : "))
                    fibonaci = Fibonacci(inputData)
                    fibonaci.main()
                except TypeError:
                    print("Data yang dimasukkan bukan angka!")
            elif inputTipe == "C" or inputTipe == "c":
                try:
                    inputData = int(input("Masukkan Jumlah Cakram [Cth: 4] : "))
                    menara_hanoi = MenaraHanoi(inputData)
                    menara_hanoi.main()
                except TypeError:
                    print("Data yang dimasukkan bukan angka!")
            break

if __name__ == "__main__":
    Main.main()