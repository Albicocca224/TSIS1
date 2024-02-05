from itertools import permutations
def print_permutations(input_string):
    all_permutations = permutations(input_string)
    for permutation in all_permutations:
        print(''.join(permutation))
user_input = input()
print_permutations(user_input)
