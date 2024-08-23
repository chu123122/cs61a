HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    def helper(r,c):
        if c==0:
            return 1
        elif r==c:
            return 1
        elif c>r:
            return 0
        else:
            return helper(r-1,c-1)+helper(r-1,c)
    return helper(row,column)
    # if column == 0:
    #     return 1
    # elif row == 0:
    #     return 0
    # else:
    #     above = pascal(row - 1, column)
    #     above_left = pascal(row - 1, column - 1)
    #     return above + above_left


def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
    def insert_helper(check):
        def change_helper(current,check,memory,s):
            if current==len(s)-1:
                s+=[memory]
                return 
            elif s[check+1]!=after:
                only=s[current+1]
                s[current+1]=after
                return change_helper(current+1,check,only,s)
            else:
                 print("DEBUG",current+1,len(s))
                 only=s[current+1]
                 s[current+1]=memory
                 return change_helper(current+1,check,only,s)

        if check==len(s):
            print("DEBUG","End",s)
            return s
        elif s[check]==before:
            change_helper(check,check,after,s)
            return insert_helper(check+2)
        else:
            return insert_helper(check+1)
    return insert_helper(0)
# index = 0
# while index < len(s):
#     if s[index] == before:
#         s.insert(index + 1, after)
#         index += 1
#     index += 1
# return s

# # Alternate solution (backward traversal):
# i = len(s) - 1
# while i >= 0:
#     if s[i] == before:
#         s.insert(i + 1, after)
#     i -= 1
# return s

HW_SOURCE_FILE=__file__


def planet(mass):
    """Construct a planet of some mass."""
    assert mass > 0
    "*** YOUR CODE HERE ***"
    return ['planet',mass]

def mass(p):
    """Select the mass of a planet."""
    assert is_planet(p), 'must call mass on a planet'
    "*** YOUR CODE HERE ***"
    return p[1]

def is_planet(p):
    """Whether p is a planet."""
    return type(p) == list and len(p) == 2 and p[0] == 'planet'

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return t, u, v

def total_mass(m):
    """Return the total mass of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_mass(t)
    3
    >>> total_mass(u)
    6
    >>> total_mass(v)
    9
    """
    if is_planet(m):
        return mass(m)
    else:
        assert is_mobile(m), "must get total mass of a mobile or a planet"
        return total_mass(end(left(m))) + total_mass(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> p = mobile(arm(3, t), arm(2, u))
    >>> balanced(p)
    False
    >>> balanced(mobile(arm(1, v), arm(1, p)))
    False
    >>> balanced(mobile(arm(1, p), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    def check_all(lef,rig):
        l_all=total_mass(end(lef))*length(lef)
        r_all=total_mass(end(rig))*length(rig)
        if l_all==r_all:
            return True
        else:
            return False
    l,r=left(m),right(m)
    if not check_all(l,r):
        return False
    if is_mobile(end(l)) and is_mobile(end(r)):
        return all([balanced(end(l)),balanced(end(r))])
    elif is_mobile(end(l)):
        return balanced(end(l))
    elif is_mobile(end(r)):
        return balanced(end(r))
    else:
        return check_all(l,r)
    # if is_planet(m):
    #     return True
    # else:
    #     left_end, right_end = end(left(m)), end(right(m))
    #     torque_left = length(left(m)) * total_mass(left_end)
    #     torque_right = length(right(m)) * total_mass(right_end)
    #     return torque_left == torque_right and balanced(left_end) and balanced(right_end)


def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(t):
        if label(t)=='berry':
            return True
        else:
            for i in branches(t):
                if is_leaf(i):
                    if label(i)=='berry':
                        return True
                else:
                    return helper(i)
    if(helper(t)==True):
        return True
    else:
        return False
    # if label(t) == 'berry':
    #     return True
    # for b in branches(t):
    #     if berry_finder(b):
    #         return True
    # return False

    
     


HW_SOURCE_FILE=__file__


def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    "*** YOUR CODE HERE ***"
    def max_helper(tree,max): 
        if is_leaf(tree):
            return label(tree)
        else:
            for i in branches(tree):
                num=label(tree)+max_helper(i,max)
                if max<num:
                    max=num 
            return max
    return max_helper(t,0)
    # if is_leaf(t):
    #     return label(t)
    # highest_sum = 0
    # for b in branches(t):
    #     highest_sum = max(max_path_sum(b), highest_sum)
    # return label(t) + highest_sum

    # # List comprehension solution
    # if is_leaf(t):
    #   return label(t)
    # else:
    #   return label(t) + max([max_path_sum(b) for b in branches(t)])



def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'


def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be an arm"
    assert is_arm(right), "right must be an arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct an arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is an arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of an arm."""
    assert is_arm(s), "must call length on an arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of an arm."""
    assert is_arm(s), "must call end on an arm"
    return s[2]



# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

