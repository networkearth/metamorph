import h3
import geopy.distance

from awsglue import DynamicFrame

def find_neighbors(h3_index, max_km):
    """
    Input:
    - h3_index (str): the H3 index

    Finds all the h3 indices whose centroids are 
    within `max_km`. 
    """
    h3_coords = h3.h3_to_geo(h3_index)
    checked = set([h3_index])
    neighbors = set([h3_index])
    distance = 1
    found_neighbors = True

    while found_neighbors:
        found_neighbors = False
        candidates = h3.k_ring(h3_index, distance)
        new_candidates = set(candidates) - checked
        for candidate in new_candidates:
            if geopy.distance.geodesic(h3_coords, h3.h3_to_geo(candidate)).km <= max_km:
                neighbors.add(candidate)
                found_neighbors = True
            checked.add(candidate)
        distance += 1
    return list(neighbors)

def add_h3_options_for_record(row, col, max_km):
    row['neighbors'] = find_neighbors(row[col], max_km)
    return row

def add_h3_options(self, col, max_km):
    return self.map(f = lambda r: add_h3_options_for_record(r, col, max_km))

DynamicFrame.add_h3_options = add_h3_options