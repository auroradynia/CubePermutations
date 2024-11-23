from gmpy2 import fac, mpz, mod, mpfr

import sys

sys.set_int_max_str_digits(99999)  # set this to 0, see readme

def print_result():
    print()
    print(int(result))
    print()
    print("as scientific notation:")
    print()
    print(mpfr(result))

while True:
    print()
    try:
        faces = int(input("Enter number of faces: (6 for cube, 12 for megaminx)\n"))
    except ValueError:
        print("ERROR: invalid value (input must be integer)")
        continue
    if(faces == 6): #cube
        try:
            size = mpz(int(input("Enter number of divisions: (e.g. 2 for pocket cube, 3 for regular rubik's cube, 5 for professors rubik's cube)\n")))
        except ValueError:
            print("ERROR: invalid value (input must be integer)")
            continue
        centres = (size - 2) ** 2 * faces
        edges = (size - 2) * 4 * (faces // 2)
        if(size < 2):
            print()
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " rubik's cube is:")
            print()
            print(1)
        elif(size % 2 == 0): #even
            print()
            sets = (centres + edges) // 24
            nsets = ((centres // 24) * faces) + 1
            result = (fac(8) * 3 ** 7 * fac(24) ** sets) // 24 ** nsets
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " rubik's cube is:")
            print_result()
        elif(size % 2 == 1): #odd
            print()
            sets = ((centres - faces) + (edges - 12)) // 24
            nsets = ((centres - faces) // 24) * 6
            result = (fac(8) * 3 ** 7 * fac(12) * 2 ** 10 * fac(24) ** sets) // 24 ** nsets
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " rubik's cube is:")
            print_result()

    elif(faces == 12): #megaminx
        try:
            size = mpz(int(input("Enter number of divisions: (e.g. 2 for kilominx, 3 for megaminx, 5 for gigaminx)\n")))
        except ValueError:
            print("ERROR: invalid value (input must be integer)")
            continue
        if(size < 2):
            print()
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " megaminx is:")
            print()
            print(1)
        elif(size % 2 == 0): #even
            result = ((fac(20) * 3 ** 20) // ((5 * 12) ** (mod(size + 1, 2)) * 3 * 2)) * ((fac(30) * 2 ** 30) // (2 * 2)) ** mod(size, 2) * (fac(60) // 2) ** ((size - 2) // 2) * (fac(60) // fac(5) ** 12) ** (((size - 2) // 2) ** 2)
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " megaminx is:")
            print_result()
        elif(size % 2 == 1): #odd
            sized = (size - 1) // 2
            result = fac(30) * fac(20) * fac(60) ** (sized ** 2 - 1) * 2 ** (28 - sized) * 3 ** 19 // fac(5) ** (12 * sized * (sized - 1))
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " megaminx is:")
            print_result()
    else:
        print("ERROR: invalid value (supported faces are 6 and 12)")
