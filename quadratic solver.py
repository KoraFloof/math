import cmath
import sys

print("QUADRATIC SOLVER BY KORA | ax^2 + bx + c = 0")

# Input Section
while True:
    a = float(input("Input the value of a in your quadratic: "))
    b = float(input("Input the value of b in your quadratic: "))
    c = float(input("Input the value of c in your quadratic: "))

    # Discriminant (b^2-4ac)
    discriminant = (pow(b, 2)) - 4 * a * c
    disc_sqrt = cmath.sqrt(discriminant)
    if disc_sqrt.imag == 0:
        disc_sqrt = disc_sqrt.real    

    # Sorting out errors
    if a == 0:
        print("-------------------------\nValue of a can not be equal to 0\n-------------------------")
        if str(input("Would you like to quit? (y/n): ")) == "n":
            print("-------------------------")
            continue
        else:
            sys.exit()

    # Finding the roots
    roota = (-b + disc_sqrt) / (2 * a)
    rootb = (-b - disc_sqrt) / (2 * a)

    # Printing the results
    if roota == rootb:
        print("-------------------------\n", roota, "\n-------------------------")
        if str(input("Would you like to quit? (y/n): ")) == "n":
            print("-------------------------")
            continue
        else:
            sys.exit()
    else:
        print("-------------------------\n",roota, rootb, "\n-------------------------")
        if str(input("Would you like to quit? (y/n): ")) == "n":
            print("-------------------------")
            continue
        else:
            sys.exit()