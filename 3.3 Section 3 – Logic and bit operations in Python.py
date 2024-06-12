# Example 1:
var=1
print(var > 0)
print(not (var <= 0))

# Example 2:
var=1
print(var != 0)
print(not (var == 0))

'''De Morgan's laws. They say that:
The negation of a conjunction is the disjunction of the negations.
The negation of a disjunction is the conjunction of the negations.'''
#not (p and q) == (not p) or (not q)
#not (p or q) == (not p) and (not q)


