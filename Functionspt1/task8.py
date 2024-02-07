def spy_game(nums):
    found_0 = False
    found_00 = False
    for num in nums:
        if num == 0:
            if found_0:
                found_00 = True
            else:
                found_0 = True
        elif num == 7:
            if found_0 and found_00:
                return True
    return False
print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,7,0]))  
