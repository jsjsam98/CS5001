def main():
    initial_balance = float(input('Initial balance: '))
    interest = 0.06
    total1 = initial_balance*0.06/12+initial_balance
    total2 = total1*0.06/12+total1
    total3 = total2*0.06/12+total2
    print('After first month:', total1)
    print('After second month:', total2)
    print('After third month:', total3)


if __name__ == "__main__":
    main()
