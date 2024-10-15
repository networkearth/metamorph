from awsglue import DynamicFrame

import numpy as np
from scipy.stats import norm

def get_depth_class(depth_classes, depth):
    """
    Inputs:
    - depth_classes: np.array, the depth classes to choose from
    - depth: float, the depth of the fish as recorded

    Outputs:
    - int, the selected depth class

    Selects a depth class based on the depth of the fish.

    It turns out that PSAT summary data bins the depth into
    intervals so the actual depth is not known. However
    given the recorded depth we can estimate the depth classes
    it could belong to and the likelihoods of each.
    """
    depth_classes = np.array(depth_classes)

    sd = (
        depth * 0.08 / 1.96
    )  # ~two standard deviations gives our 95% confidence interval
    if sd == 0:
        division = np.zeros(len(depth_classes))
        division[0] = 1
    else:
        # we're going to assume the depth classes are sorted
        z = (depth_classes - depth) / sd
        division = norm.cdf(z)
        division[1:] = division[1:] - division[:-1]
    # if there aren't quite enough depth classes the
    # probabilities may not sum to 1, so we'll normalize
    division = division / division.sum()
    return float(np.random.choice(depth_classes, p=division))

def add_depth_class_for_record(row, depth_classes, depth_column):
    row['selected_depth_class'] = get_depth_class(depth_classes, row[depth_column])
    return row

def add_depth_class(self, depth_classes, depth_column='depth'):
    depth_classes = sorted([float(d) for d in depth_classes.split(",")])
    return self.map(f = lambda r: add_depth_class_for_record(r, depth_classes, depth_column))

DynamicFrame.add_depth_class = add_depth_class