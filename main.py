import numpy as np


def input_matriks():
    matriks = []

    # Pilih ordo matriks
    print(">>> Input ordo matriks")
    baris = int(input("Pilih jumlah baris dan kolom matriks: "))
    kolom = baris
    print(f"Matriks A berordo {baris}x{kolom}")
    print('-' * 20)

    # Input element matriks A dan B
    print(">>> Input element matriks")
    for i in range(baris):
        matriks.append([])
        for j in range(kolom):
            matriks[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
    print('-' * 20)

    # Tampilkan matriks A dan B
    print(">>> Hasil Kalkulasi")
    print("A:")
    for i in range(baris):
        print('\t[', end=' ')
        for j in range(kolom):
            print(f"{matriks[i][j]}", end=' ')
        print(']\n', end='')

    return matriks


def invers_matriks(matriks):
    # cari determinan
    determinan = cari_determinan(matriks)
    print(determinan)


def cari_determinan(matriks):
    kolom = len(matriks)
    if kolom > 2:
        determinan_akhir = 0
        for i in range(kolom):
            matriks2 = []
            iterasi = 0
            for j in [x for x in range(kolom) if x != 0]:
                matriks2.append([])
                for k in [y for y in range(kolom) if y != i]:
                    matriks2[iterasi].append(matriks[j][k])
                iterasi += 1
            determinan = cari_determinan(matriks2)
            if (i % 2) == 0:
                determinan_akhir -= matriks[0][i] * determinan
            else:
                determinan_akhir += matriks[0][i] * determinan
        return determinan_akhir
    else:
        a = matriks[0][0]
        b = matriks[0][1]
        c = matriks[1][0]
        d = matriks[1][1]
        determinan = (a * d) - (b * c)
        return determinan


def test_invers_matriks(matriks):
    matriks_np = np.array(matriks)
    matriks_invers = np.linalg.inv(matriks_np)
    print(matriks_invers)


def main():
    # matriks = [[1, 2],
    #            [3, 4]]
    matriks = [[2, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    # matriks = [[2, 2, 3, 4],
    #            [5, 6, 7, 8],
    #            [9, 10, 11, 12],
    #            [13, 14, 15, 16]]

    # matriks = input_matriks()
    invers_matriks(matriks)
    print("-" * 20)
    test_invers_matriks(matriks)


if __name__ == '__main__':
    main()
