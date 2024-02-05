def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams_needed = 100
result = grams_to_ounces(grams_needed)
print(f"{result:.2f}")
