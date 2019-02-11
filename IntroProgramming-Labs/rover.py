# distance = 34,000,000 miles
# speed of light = 186,000 miles/sec
# a program to calculate how long it takes a photo from Curiosity to reach NASA when Mars is at its closest orbit to Earth, from distance 34 million miles

def main():
    dist = eval(input("distance: "))
    speedOfLight = 186000
    time = dist/speedOfLight
    print(time, "seconds")

main()
