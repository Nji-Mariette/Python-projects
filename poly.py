from cmath import sqrt
# from re import X


def main():
    S: list[int] = [-1, -2, -206, -6, -1001, -2002, 10, 36, 19, 120, 17]

    while True:
        a = int(input('enter a: '))
        b = int(input('enter b:'))
        c = int(input('enter c:'))
        p = sqrt((b*b) - (4*a*c))

        
        x1: complex = (-b-p)/(2*a)
        x2: complex = (-b+p)/(2*a)
        # print(x1)
        # print(x2)

        if x1 and x2 in S:
            print('cheer!you guessed one of our jackpots polynomials >>')
            break
        elif x1 or x2 in S:
            print("Congratulations! you guessed one of our polynomials winners >>")
            # start all over
            main()
        else:
            print("Thanks for participating! you can try again your luck >>")
            # start all over
            main()


if __name__ == '__main__':
    main()
