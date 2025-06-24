from .clearTerminal import clear_terminal as ct

class Fibonacci:
    def __init__(self, n: int):
        self.n = n

    def hitung_fibonacci(self) -> int:
        # Kasus dasar (base case):
        # Suku pertama (n=0) atau suku kedua (n=1) dari deret Fibonacci
        # adalah 0 dan 1. Ini menghentikan rekursi.
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1
        # Langkah rekursif:
        # Suku ke-n adalah jumlah dari dua suku sebelumnya (n-1 dan n-2).
        else:
            # Kita membuat objek Fibonacci baru untuk setiap panggilan rekursif
            # agar 'n' tidak berubah di objek asli.
            return Fibonacci(self.n - 1).hitung_fibonacci() + \
                   Fibonacci(self.n - 2).hitung_fibonacci()
    
    def main(self) -> None:
        ct()
        print("="*50)
        print("{:^50}".format("program deret fibonacci".upper()))
        print("="*50)
        try:
            # Simpan nilai 'n' asli untuk ditampilkan
            original_n = self.n 
            hasil_fibonacci = self.hitung_fibonacci()
            print(f"Suku ke-{original_n} dari deret Fibonacci adalah: {hasil_fibonacci}")
        except RecursionError:
            print("Terjadi kesalahan rekursi. Angka mungkin terlalu besar.")
        except TypeError:
            print("Angka tidak valid. Harap masukkan bilangan bulat.")
