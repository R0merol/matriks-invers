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

    return matriks


def invers_matriks(matriks):
    # Cari Determinan
    determinan = cari_determinan(matriks)
    if determinan == 0:
        return print("Matrix Singular! (Determinan = 0)")

    # Check if matrix is 2x2 or not
    kolom = len(matriks)
    if kolom > 2:
        # Step 1: Generate Matrix of Minors
        matriks2 = []
        if kolom > 2:
            for i in range(kolom):
                matriks2.append([])
                for j in range(kolom):
                    matriks3 = []
                    iterasi = 0
                    for k in [x for x in range(kolom) if x != i]:
                        matriks3.append([])
                        for l_ in [y for y in range(kolom) if y != j]:
                            matriks3[iterasi].append(matriks[k][l_])
                        iterasi += 1
                    matriks2[i].append(cari_determinan(matriks3))
        print_matriks(matriks2, "Step 1:")

        # Step 2: Generate the Matrix of Cofactors
        for i in range(kolom):
            for j in range(kolom):
                if ((i + j) % 2) == 1:
                    if kolom > 2:
                        matriks2[i][j] *= -1
        print_matriks(matriks2, "Step 2:")

        # Step 3: Find the Adjugate/Adjoint
        matriks3 = []
        for i in range(kolom):
            matriks3.append([])
            for j in range(kolom):
                if i == j:
                    matriks3[i].append(matriks2[i][j])
                else:
                    matriks3[i].append(matriks2[j][i])
        print_matriks(matriks3, "Step 3:")

        # Step 4: Divide Adjugate by Determinant
        for i in range(kolom):
            for j in range(kolom):
                matriks3[i][j] /= determinan
        print_matriks(matriks3, "Step 4:")

        # Print Hasil Invers Matriks
        print_matriks(matriks3, "A^-1:")

    else:
        # Step 1:
        matriks2 = []
        for i in range(kolom):
            matriks2.append([])
            for j in range(kolom):
                if ((i + j) % 2) == 1:
                    matriks2[i].append(matriks[i][j] * -1)
                else:
                    matriks2[i].append(matriks[i][j])


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
                determinan_akhir += matriks[0][i] * determinan
            else:
                determinan_akhir -= matriks[0][i] * determinan

        return determinan_akhir
    else:
        a = matriks[0][0]
        b = matriks[0][1]
        c = matriks[1][0]
        d = matriks[1][1]
        determinan = (a * d) - (b * c)
        return determinan


def test_invers_matriks(matriks):
    # matriks_np = np.array(matriks)
    matriks_invers = np.linalg.inv(matriks)
    print(matriks_invers)


def print_matriks(matriks, teks=""):
    kolom = len(matriks)
    print(f"{teks}")
    for i in range(kolom):
        print('\t[', end=' ')
        for j in range(kolom):
            print(f"{round(matriks[i][j], 3)}\t", end=' ')
        print(']\n', end='')


def main():
    # matriks = input_matriks()
    matriks = [[1, 2],
               [3, 4]]
    # matriks = [[2, 2, 3],
    #            [4, 5, 6],
    #            [7, 8, 9]]
    # matriks = [[3, 2, 3, 4],
    #            [5, 6, 10, 8],
    #            [9, 10, 11, 12],
    #            [13, 14, 15, 16]]

    # Tampilkan matriks A dan B
    print(">>> Hasil Kalkulasi")
    print_matriks(matriks, "A:")
    invers_matriks(matriks)


if __name__ == '__main__':
    main()

# Nilai-nilai percobaan
# matriks = [[1, 2],
#            [3, 4]]
# matriks = [[2, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]
# matriks = [[3, 2, 3, 4],
#            [5, 6, 10, 8],
#            [9, 10, 11, 12],
#            [13, 14, 15, 16]]
# matriks = [[3, 2, 3, 4, 1],
#            [5, 6, 10, 8, 2],
#            [9, 10, 11, 12, 3],
#            [13, 14, 15, 16, 4],
#            [13, 14, 15, 16, 6]]
# matriks = [[1, 2, 3],
#            [0, 1, 4],
#            [5, 6, 0]]
