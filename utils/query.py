from sklearn.neighbors import KDTree
from utils.database import get_lists

RUMOR_THRESHOLD = 2
rumors, truths, links, vectors = get_lists()
tree = KDTree(vectors, metric="euclidean")

def get_closest_neighbors(vector, num=1):
    """
    gets the closest rumors and their distances
    """
    distances, indices = tree.query(vector.reshape(1, vector.shape[0]), k=num)
    return distances, indices

def is_rumor(vector):
    """
    returns truth, link if it is a rumor
    returns False if not
    """
    distances, indices = get_closest_neighbors(vector)
    distances = distances.reshape(distances.shape[1])
    indices = indices.reshape(indices.shape[1])
    # if the closest distance is below the threshold, return true
    if distances[0] < RUMOR_THRESHOLD:
        return {
            "truth": truths[indices[0]],
            "source": links[indices[0]]
        }
    return False