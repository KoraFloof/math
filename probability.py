import math
import sys

while True:
    # n = Number of trials
    # You should do n+1 trials for 0 to n
    n = int(input("Input the number of trials: "))
    # x = Number of successes
    # Will increment to show every value up to n
    x = 0
    # p = Probability of success (0 being 0% and 100 being 100%)
    p = float(input("Input the probability of a success: ")) / 100
    # q = Probability of failure
    q = 1 - p

    print("------------")
    while x <= n:
        factn = math.factorial(n)
        factx = math.factorial(x)
        factd = math.factorial(n-x)
        probability = factn/(factd * factx) * (p ** x) * (q ** (n-x)) * 100
        inverse = pow((probability/100), -1)
        print("Probability of it happening", x , "times:", str(probability) + "%", "| 1 in", "%.1f" % inverse)
        x+=1
    
    print("------------")
    
    if str(input("Would you like to continue? (y/n) ")) == "y":
        continue
    else:
        sys.quit()