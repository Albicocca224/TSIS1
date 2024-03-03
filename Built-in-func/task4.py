import math
import time
def sqRoot(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result
number = int(input("Enter the number: "))
ms = int(input("Enter the milliseconds: "))
result = sqRoot(number, ms)
print(f"Square root of {number} after {ms} milliseconds is {result}")

