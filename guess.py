class Tebak:
    def __init__(self,tebak,jawab):
        self.tebak = tebak
        self.jawab = jawab
    def cek(self):
        if self.tebak == self.jawab:
            print('jawaban kamu benar')
        else:
            print('jawaban kamu salah')