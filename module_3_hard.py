def calculate_structure_sum(data_structure):
    sum1 = 0
    for i in data_structure:
        if isinstance(i, (list, tuple, set)):
            sum1 += calculate_structure_sum(i)
        elif isinstance(i, dict):
            sum1 += calculate_structure_sum(i.items())
        if isinstance(i, (int, float)):
            sum1 += i
        if isinstance(i, str):
            sum1 += len(i)
    return sum1


data_structure =[
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)