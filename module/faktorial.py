from .clearTerminal import clear_terminal as ct

class Faktorial:
    def __init__(self, data: int):
        self.data = data

    # def hitung_faktorial(self) -> int:
    #     hasil = 1
    #     for i in range(1, self.data + 1):
    #         hasil *= i
    #     return hasil

    def hitung_faktorial(self) -> int:
        # Base case: if data is 0 or 1, the factorial is 1
        if self.data == 0 or self.data == 1:
            return 1
        # Recursive step: data * factorial of (data - 1)
        else:
            # We need to create a new instance or pass the decremented value
            # directly to avoid modifying self.data in the recursive calls
            return self.data * Faktorial(self.data - 1).hitung_faktorial()
    
    def main(self) -> None:
        while True:
            ct()
            print("="*50)
            print("{:^50}".format("program faktorial".upper()))
            print("="*50)
            try:
                self.hasilPerhitungan = self.hitung_faktorial()
                print(f"Hasil Faktorial dari angka {self.data} = {self.hasilPerhitungan}")
                break
            except TypeError:
                print("Angka tidak dikenali")