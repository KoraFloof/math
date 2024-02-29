import math
import sys

print("!IMPORTANT! If side is unknown, input 0 !IMPORTANT!")

while True:
    adj = float(input("\nInput the length of the adjacent side of theta: "))
    opp = float(input("Input the length of the opposing side from theta: "))
    hyp = float(input("Input the length of the hypoteneuse: "))

    if adj == 0:
        length = math.sqrt(pow(hyp, 2) - pow(opp, 2))
        angle = math.asin(opp/hyp)
    elif opp == 0:
        length = math.sqrt(pow(hyp, 2) - pow(adj, 2))
        angle = math.acos(adj/hyp)
    else:    
        length = math.sqrt(pow(adj, 2) + pow(opp, 2))
        angle = math.atan(opp/adj)
    
    angle = math.degrees(angle)

    print("----------", "\nAngle: " + "%.2f" % angle + "°", "\nLength of Unknown Side: " + "%.2f" % length,  "\n----------")

    if str(input("Would you like to continue? (y/n) ")) == "y":
        continue
    else:
        sys.exit()