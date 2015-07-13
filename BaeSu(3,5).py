def _3BaeSu(n):
    sum_3 = int(n/3)
    sum3 = 0
    for sum_3 in range(1, sum_3+1):
        sum3 = sum3 + 3 * sum_3
    return sum3

def _5BaeSu(n):
    sum_5 = int(n/5)
    sum5 = 0
    for sum_5 in range(1, sum_5+1):
        sum5 = sum5 + 5 * sum_5
    return sum5

def main():
    n=input('n보다 작은 3 or 5의 배수를 모두 더하면?')
    n = int(n)
    print('3의 배수를 더한값:', _3BaeSu(n))
    print('5의 배수를 더한값:', _5BaeSu(n))

if __name__ == '__main__':
    main()

