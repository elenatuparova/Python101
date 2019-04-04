def matrix_bombing_plan(m):
    width = len(m[0])
    height = len(m)
    matrix = {}
    for x in range(width):
        for y in range(height):
            matrix[(x, y)] = m[x][y]
    print(matrix)
    total_sum = 0
    for n in m:
        total_sum += sum(n)
    bombing_outcomes = {}
    moving_vectors = [(-1, 0), (1, 0), (-1, -1), (1, 1), (0, -1), (0, 1), (1, -1), (-1, 1)]
    for position in matrix:
        to_substract = 0
        for vector in moving_vectors:
            if (position[0] + vector[0]) in list(range(width)) and (position[1] + vector[1]) in list(range(height)):
                to_substract += matrix[position] if matrix[position] <= matrix[(position[0] + vector[0], position[1] + vector[1])] else matrix[(position[0] + vector[0], position[1] + vector[1])]
        bombing_outcomes[position] = total_sum - to_substract
    return bombing_outcomes
