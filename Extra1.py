"""Printing a list of lists containing all possible combinations of 1,2 and 3"""
def generate_combinations(n, current_combination, combinations):
    if n == 0:
        combinations.append(list(map(int,list(current_combination))))
    else:
        generate_combinations(n-1, current_combination + "1", combinations)
        generate_combinations(n-1, current_combination + "2", combinations)
        generate_combinations(n-1, current_combination + "3", combinations)

combinations = []
generate_combinations(3, "", combinations)
print(combinations)
        