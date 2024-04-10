
def ounces_to_grams(weight_in_oz):
    return weight_in_oz * 28.35
result = ounces_to_grams(3)
print (result)

weight_in_oz_str = input("Enter weight in oz: ")

weight_in_oz = float(weight_in_oz_str)

weight_in_g = ounces_to_grams(weight_in_oz)

print("Weight in grams =", weight_in_g)

