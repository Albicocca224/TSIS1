def spy_game(nums):
    zero_found = False
    seven_found = False
    for num in nums:
        if num == 0:
            zero_found = True
        elif num == 7 and zero_found:
            seven_found = True
        if zero_found and seven_found:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))  
