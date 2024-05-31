from operator import add, sub, mul
import math

def vector_add(a, b):
    return list(map(add, a, b))

def vector_sub(a, b):
    return list(map(sub, a, b))

def vector_dot(a,b):
    return sum(list(map(mul, a, b)))

def squared_diff(a,b):
    return (a - b)**2
def vector_dist(a,b):
    return math.sqrt(
        sum(list(map(
        lambda a, b: (a - b)**2,
        a, b
        )))
    )
def magnitude(a):
    return vector_dist(a, [0 for x in range(len(a))])
def vector_cos(a,b):
    dot = vector_dot(a,b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    return dot / (mag_a * mag_b)

def closest_vector(a, allVectors, disallowed_keys=set()):
    return closest_vectors(a, allVectors, 1, disallowed_keys)
def closest_vectors(a, allVectors, num_closest=5, disallowed_keys=set()):
    min_dists = [(None, math.inf) for x in range(num_closest)]
    for key in allVectors:
        if key not in disallowed_keys:
            vector = allVectors[key]
            dist = vector_dist(a, vector)
            if dist < min_dists[num_closest - 1][1]:
                min_dists[num_closest - 1] = (key, dist)
            min_dists = sorted(min_dists, key=lambda x: x[1])
    return min_dists
def most_similar_vectors(a, allVectors, num_closest=5, disallowed_keys=set()):
    max_cos = [(None, -1) for x in range(num_closest)]
    for key in allVectors:
        if key not in disallowed_keys:
            vector = allVectors[key]
            cos = vector_cos(a, vector)
            if cos > max_cos[0][1]:
                max_cos[0] = (key, cos)
            max_cos = sorted(max_cos, key=lambda x: x[1], )
    return sorted(max_cos, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    a = [1,3,9,7]
    b = [3,4,5,6]

    assert vector_add(a,b) == [4,7,14,13]
    assert vector_sub(a,b) == [-2,-1,4,1]
    assert vector_dot(a,b) == 102
    assert vector_dist(a,b) == math.sqrt(22)

    c = [13, 2, 17, -28]
    d = [0,0,0,0]
    vector_dict = {'d': d, 'b': b, 'c': c}
    
    assert closest_vectors(a, vector_dict, 2) == [('b', math.sqrt(22)), ('d', vector_dist(a,d))]
    assert closest_vectors(a, vector_dict, 2, disallowed_keys={'b'}) == [('d', vector_dist(a,d)),('c', vector_dist(a,c))]
    
    assert magnitude(a) == math.sqrt(140)
    assert magnitude(b) == math.sqrt(86)
    assert vector_cos(a,b) == 102 / (math.sqrt(140) * math.sqrt(86))