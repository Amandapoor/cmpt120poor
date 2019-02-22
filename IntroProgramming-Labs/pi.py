
# a program to approximate the value of pi by summing the terms of the series
# the series is "4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 +..."

import math

def main():
    
    n = int(input("Enter how many terms should be used to approximate the value of pi: "))

    total = 0.0
    sign = 1.0  
    for denom in range(1, n*2, 2):
        total = total + sign * 4.0/denom
        sign = -sign 

    print("Approximation to pi is:", total)
    print("Difference from math.pi:", math.pi - total)

main()
