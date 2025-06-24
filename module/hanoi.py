from .clearTerminal import clear_terminal as ct

class MenaraHanoi:
    def __init__(self, jumlah_cakram: int):
        self.jumlah_cakram = jumlah_cakram
        self.langkah_pemindahan = [] # Untuk menyimpan urutan langkah

    def pindahkan_cakram(self, cakram: int, sumber: str, tujuan: str, bantu: str) -> None:
        """
        Fungsi rekursif untuk memindahkan cakram.

        Args:
            cakram (int): Jumlah cakram yang akan dipindahkan.
            sumber (str): Nama tiang sumber (misal: 'A').
            tujuan (str): Nama tiang tujuan (misal: 'C').
            bantu (str): Nama tiang bantu (misal: 'B').
        """
        # Kasus dasar (base case):
        # Jika hanya ada 1 cakram, pindahkan langsung dari sumber ke tujuan.
        if cakram == 1:
            self.langkah_pemindahan.append(f"Pindahkan cakram 1 dari {sumber} ke {tujuan}")
            return
        
        # Langkah rekursif:
        # 1. Pindahkan cakram (n-1) dari sumber ke tiang bantu, menggunakan tiang tujuan sebagai tiang bantu.
        self.pindahkan_cakram(cakram - 1, sumber, bantu, tujuan)
        
        # 2. Pindahkan cakram terbesar (cakram ke-n) dari sumber ke tiang tujuan.
        self.langkah_pemindahan.append(f"Pindahkan cakram {cakram} dari {sumber} ke {tujuan}")
        
        # 3. Pindahkan cakram (n-1) dari tiang bantu ke tiang tujuan, menggunakan tiang sumber sebagai tiang bantu.
        self.pindahkan_cakram(cakram - 1, bantu, tujuan, sumber)

    def main(self) -> None:
        ct()
        print("="*50)
        print("{:^50}".format("program menara hanoi".upper()))
        print("="*50)
        
        if self.jumlah_cakram <= 0:
            print("Jumlah cakram harus lebih dari 0.")
            return

        print(f"Memecahkan Menara Hanoi dengan {self.jumlah_cakram} cakram:")
        print("Tiang awal: A, Tiang bantu: B, Tiang tujuan: C\n")
        
        # Panggil fungsi rekursif utama
        self.pindahkan_cakram(self.jumlah_cakram, 'A', 'C', 'B')
        
        print("Urutan langkah pemindahan:")
        for i, langkah in enumerate(self.langkah_pemindahan):
            print(f"{i+1}. {langkah}")
        
        # Jumlah langkah minimum adalah (2^n - 1)
        jumlah_minimum_langkah = (2**self.jumlah_cakram) - 1
        print(f"\nTotal langkah yang dibutuhkan: {len(self.langkah_pemindahan)}")
        print(f"Jumlah langkah minimum teoritis: {jumlah_minimum_langkah}")
