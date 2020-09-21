def main():
    K = float(input('Enter temperature in Kelvin: '))
    C = K-273.15
    F = (K-273.15)*9/5+32
    print('The temperature in Celsius is', C)
    print('The temperature in Fahrenheit is', F)


if __name__ == "__main__":
    main()
