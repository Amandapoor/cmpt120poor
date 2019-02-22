# a program to compute the nth Fibonacci number with user input for n

def main():
    n = int(input("Enter a value for n: "))
    n2 = 1
    n3 = 1
    n4 = 1
    for i in range(n-2):
        n4 = n3 + n2
        n2 = n3
        n3 = n4
    print(n4)

main()

