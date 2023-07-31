import random
from guess import Tebak

tebak = random.randint(1, 10)

jawab= int(input('masukan angka: '))

tebak1 = Tebak(tebak,jawab)
tebak1.cek()