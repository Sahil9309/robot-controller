def calculate_distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

def format_coordinates(coord):
    return f"X: {coord[0]}, Y: {coord[1]}"

def update_coordinates(current_coord, movement_vector):
    return (current_coord[0] + movement_vector[0], current_coord[1] + movement_vector[1])