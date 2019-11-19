# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):

        Fn1 = fibs[i-1]
        Fn2 = fibs[i]
        Fn = Fn1 + Fn2
        fibs.append(Fn)

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
