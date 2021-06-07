def subset_checker(superset, subset):
    return all(item in superset.items() for item in subset.items())