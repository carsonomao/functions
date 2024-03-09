def calculate_discount(price,discountPercentage):
    if discountPercentage < 20 :
        return price
    else:
        return price * (discountPercentage/100)
    
print(calculate_discount(int(input("Enter the price: ")),int(input("Enter the dicount rate: "))))