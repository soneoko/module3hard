def calculate_structure_sum(*structure):
    count = 0
    for i in structure:
        if isinstance(i, int):
            count += i
        elif isinstance(i, str):
            count += len(i)
        elif isinstance(i, dict):
            for key in i:
                count += calculate_structure_sum(key)
                count += calculate_structure_sum(i[key])
        else:
            count += calculate_structure_sum(*i)
    return count
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)