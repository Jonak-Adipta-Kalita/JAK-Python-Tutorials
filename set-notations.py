l1 = {5, 6, 8, 5, 4}
l2 = {1, 8, 2, 0}

l1.add(10)

# l2.remove(9)  # Error as 9 doesn't exist
l2.discard(9)  # Removes duplicates too


### Operations between the Sets ###

print(l1 | l2, l1.union(l2))  # Union
print(l1 & l2, l1.intersection(l2))  # Intersection

print(l1 - l2, l1.difference(l2))  # Subtraction

print(l1 ^ l2, l1.symmetric_difference(l2))  # Symmetric Difference

# On a note, all the functions shown here, use the *_update() versions to directly update l1 or... just do assignment operators like |=, &=


### Checks between Sets ###

print(l1.isdisjoint(l2))  # Check for Disjoint

print(l1 <= l2, l1.issubset(l2))  # Check for Subset
print(l1 < l2)  # Check for Proper Subset

print(l1 >= l2, l1.issuperset(l2))  # Check for Superset
print(l1 > l2)  # Check for Proper Superset
