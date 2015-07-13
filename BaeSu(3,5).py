def sum_3_or_5(n):
    for i in range(2, n+1):
        pass

def main():
    n=input('n보다 작은 3 or 5의 배수를 모두 더하면?')
    n = int(n)
    print('3과 5의 배수를 모두 더한값:', sum_3_or_5(n))

if __name__ == '__main__':
    main()

