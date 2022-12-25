import cmath
import math
import mpmath
mpmath.mp.prec = 99999
mpmath.mp.dps = 99999
while True:
    print()
    a = int(input("Enter Rubik's Cube Size:\n"));
    if(a % 2 == 0):
        print()
        b = (mpmath.power(a - 2, 2) * 6);
        c = ((a - 2) * 4 * 3);
        d = (b + c) / 24;
        e = ((b / 24) * 6) + 1;
        z = (mpmath.factorial(8) * mpmath.power(3, 7) * mpmath.power(mpmath.factorial(24), d)) / mpmath.power(24, e);
    else:
        print()
        b = (mpmath.power(a - 2, 2) * 6);
        c = ((a - 2) * 4 * 3);
        d = ((b - 6) + (c - 12)) / 24;
        e = (((b - 6) / 24) * 6);
        z = (mpmath.factorial(8) * mpmath.power(3, 7) * mpmath.factorial(12) * mpmath.power(2, 10) * mpmath.power(mpmath.factorial(24), d)) / mpmath. power(24, e)
    if(a < 2):
        print()
        print("The number of possible permutations for a " + str(a) + "x" + str(a) + "x" + str(a) + " rubik's cube with size is:")
        print()
        print(1)
    else:
        print("The number of possible permutations for a " + str(a) + "x" + str(a) + "x" + str(a) + " rubik's cube with size is:")
        print()
        print(int(mpmath.mpf(z)))
        mpmath.mp.dps = 4
        print()
        print("as scientific notation:")
        print()
        print(z)
        mpmath.mp.prec = 99999
        mpmath.mp.dps = 99999
