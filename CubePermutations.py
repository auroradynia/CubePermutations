import mpmath

def print_result():
    print()
    print(int(result))
    mpmath.mp.dps = 4
    print()
    print("as scientific notation:")
    print()
    print(result)

while True:
    mpmath.mp.dps = 99999 #increase this, see readme
    print()
    try:
        faces = int(input("Enter number of faces: (6 for cube, 12 for megaminx)\n"));
    except ValueError:
        print("ERROR: invalid value (input must be integer)")
        continue
    if(faces == 6): #cube
        try:
            size = int(input("Enter number of divisions: (e.g. 2 for pocket cube, 3 for regular rubik's cube, 5 for professors rubik's cube)\n"))
        except ValueError:
            print("ERROR: invalid value (input must be integer)")
            continue
        centres = (mpmath.power(size - 2, 2) * faces);
        edges = ((size - 2) * 4 * (faces / 2));
        if(size < 2):
            print()
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " rubik's cube is:")
            print()
            print(1)
        elif(size % 2 == 0): #even
            print()
            sets = (centres + edges) / 24;
            nsets = ((centres / 24) * faces) + 1;
            result = (mpmath.factorial(8) * mpmath.power(3, 7) * mpmath.power(mpmath.factorial(24), sets)) / mpmath.power(24, nsets);
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " rubik's cube is:")
            print_result()
        elif(size % 2 == 1): #odd
            print()
            sets = ((centres - faces) + (edges - 12)) / 24;
            nsets = (((centres - faces) / 24) * 6);
            result = (mpmath.factorial(8) * mpmath.power(3, 7) * mpmath.factorial(12) * mpmath.power(2, 10) * mpmath.power(mpmath.factorial(24), sets)) / mpmath. power(24, nsets)
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " rubik's cube is:")
            print_result()

    elif(faces == 12): #megaminx
        try:
            size = int(input("Enter number of divisions: (e.g. 2 for kilominx, 3 for megaminx, 5 for gigaminx)\n"))
        except ValueError:
            print("ERROR: invalid value (input must be integer)")
            continue
        if(size < 2):
            print()
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " megaminx is:")
            print()
            print(1)
        elif(size % 2 == 0): #even
            result = ((mpmath.factorial(20) * mpmath.power(3, 20)) / (mpmath.power(5 * 12, mpmath.fmod(size + 1, 2)) * 3 * 2)) * mpmath.power(((mpmath.factorial(30) * mpmath.power(2, 30)) / (2 * 2)), mpmath.fmod(size, 2)) * mpmath.power((mpmath.factorial(60) / 2), ((size - 2) / 2)) * mpmath.power((mpmath.factorial(60) / mpmath.power(mpmath.factorial(5), 12)), mpmath.power((size - 2) / 2, 2));
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " megaminx is:")
            print_result()
        elif(size % 2 == 1): #odd
            sized = int((size - 1) / 2);
            result = (mpmath.factorial(30) * mpmath.factorial(20) * mpmath.power(mpmath.factorial(60), (mpmath.power(sized, 2) - 1)) * mpmath.power(2, (28 - sized)) * mpmath.power(3, 19)) / (mpmath.power(mpmath.factorial(5), (12 * sized * (sized - 1))));
            print("The number of possible permutations for a " + str(size) + "x" + str(size) + "x" + str(size) + " megaminx is:")
            print_result()
    else:
        print("ERROR: invalid value (supported faces are 6 and 12)")
