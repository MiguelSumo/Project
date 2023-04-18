def price_code(amount, item):
    Jeans = 0
    Shoes = 0
    Hoodies = 0
    Shorts = 0

    # discount code and item discount item
    if amount > 0:
        if amount <= 300:
            discount = amount * 0.30
        elif amount <= 200:
            discount = amount * 0.20
        elif amount <= 100:
            discount = amount * 0.10
        else:
            discount = amount * 0.05

        if item == "Jeans":
            discount += amount * 0.06
        elif item == "Shoes":
            discount += amount * 0.05
        elif item == "Hoodies":
            discount += amount * 0.07
        elif item == "Shorts":
            discount += amount * 0.04

        print("discount amount :", discount)
        print("final price  :", amount - discount)

    else:
        print("invalid amount")


price_code(750,"Jeans")





