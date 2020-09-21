def main():
    price_pack = float(input('Price per six-pack: \n'))
    price_bottle = float(input('Price per two-liter: '))
    per_pack = price_pack/(6*0.355)
    per_bottle = price_bottle/2
    print('Six-pack price per liter:', per_pack)
    print('Two-liter price per liter:', per_bottle)


if __name__ == "__main__":
    main()
