def tower_builder(n_floors):
    return ['*'*(floor*2 - 1).center(n_floors*2-1, " ") for floor in range(1, n_floors+1)]