#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    v.size = 0

    if (v.left == None) & (v.right == None):	# if leaf node, subtree size is 0
        # print("\nNO roots")
        v.size = 0
    elif (v.left != None):
        # print("\nLeft root exists")
        calculate_sizes(v.left) # v.left.size = 
        v.size += v.left.size				# count up left subtree sizes
    if (v.right != None):
        # print("\nRight root exists")
        calculate_sizes(v.right) # v.right.size = 
        v.size += v.right.size				# count up right subtree sizes	
    
    v.size += 1

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices

# Runtime: O(h)
def find_vertex(r): 
    # print("\n\n\n########NEW RUN\n")
    # print("parent: ", r.parent)

    ###### yup. this works !!!!!
    # check if r has no children
    if (r.left == None) & (r.right == None):
        return r
    # check if r has only 1 child
    elif (r.left == None) ^ (r.right == None):
        nonempty = r.left if ((r.left != None) & (r.right == None)) else r.right

        check = r.size // 2
        
        # if nonempty child has two children
        if (nonempty.left != None) & (nonempty.right != None):
            if (nonempty.left.size <= check) & (nonempty.right.size <= check) & (r.size - nonempty.size <= check):
                return nonempty
        # if nonempty child has no children
        elif nonempty.left == nonempty.right == None:
            return r
        # if nonempty child has exactly 1 child
        elif (nonempty.left == None) ^ (nonempty.right == None):
            find_vertex(r)

    else:
        larger = r.left if (r.left.size > r.right.size) else r.right

        check = r.size // 2

        if larger.size <= check:
            return r
        else:
            # if larger child has two children
            if (larger.left != None) & (larger.right != None):
                if (larger.left.size <= check) & (larger.right.size <= check) & (r.size - larger.size <= check):
                    return larger
            # if larger child has no children
            elif larger.left == larger.right == None:
                return r
            # if larger child has exactly 1 child
            elif (larger.left == None) ^ (larger.right == None):
                find_vertex(r)
        

############# IGNORE EVERYTHING BELOW THIS LINE! #############
    
# def helper(v, r):
#     check = r.size // 2
#     if (v.left != None) & (v.right != None):
#         if (v.left.size <= check) & (v.right.size <= check) & (r.size - v.size <= check):
#             return v
#     elif v.left == v.right == None:
#         return r
#     elif (v.left == None) ^ (v.right == None):
#         find_vertex(r)


    ###### LATE NIGHT DRAFT
    # # if both left and right child have children
    # if not (r.right == None) and not (r.left == None):
    #     print("(1)   both L and R have children!")
    #     ls = r.left.size
    #     rs = r.right.size
    #     larger = r.left if (ls > rs) else r.right
    #     smaller = r.left if (larger == r.right) else r.right

    #     # if larger subtree is already less than 1/2 of root size, you're done
    #     if larger.size <= r.size // 2:
    #         print("returned r because one of the children is <= parent size / 2")
    #         return r
    #     else:
    #         # if one child of larger branch is empty, then remaining tree is tied to that larger node
    #         if (larger.left.size == None) ^ (larger.right.size == None):
    #             find_vertex(larger)
    #         else:
    #             # if both nodes are empty, then return r
    #             if (larger.left.size == None) & (larger.right.size == None):
    #                 print("returned r because one of the children is <= parent size / 2")
    #                 return r
    #             # if both nodes are nonempty, then compare with all other subtrees
    #             else:
    #                 if (larger.left.size <= r.size // 2) & (larger.right.size <= r.size // 2) & (r.smaller <= r.size):
    #                     print("returned r because both nodes were nonempty")
    #                     return r
    # elif (r.left == None) & (not r.right == None):
    #     print("(2)   L has no children!")
    #     print("      R:", r.right)
    #     print("      R.size:", r.right.size)
    #     # print("??? returned r because L child empty, R child not")

    #     if (r.right.size <= r.size // 2):
    #         print("returned r because L child empty, R child not")
    #         return r
    #     # find_vertex(r.right)
    # elif (r.right == None) & (not r.left == None):
    #     print("(3)   R has no children!")
    #     print("      L:", r.left)
    #     print("      L.size:", r.left.size)
    #     if (r.right.size <= r.size // 2):
    #         print("returned r because R child empty, L child not")
    #         return r
        
    #     # find_vertex(r.left)
    # else:
    #     print("returned r because its child nodes have no children")
    #     return r
    

    #### LOOK AT REMOVAL TREE CASES!!

    
    # print("parent: ", r.parent)
    # print("r.size: ", -r.size)

    

    # if r.parent == None:                              # THEN ROOT!
    #     if larger.size <= r.size // 2:
    #       return r
    #     else: find_vertex(larger)
    # else:                                             # IF NOT ROOT
        
    #     print("parent size: ", r.parent.size)
    #     if max([r.parent.size-r.size, ls, rs]) <= r.parent.size // 2:
    #         return r

    ####### DRAFT 3
    ## FOR A BALANCED TREE
    # if r.parent == None:                              # THEN ROOT!
    #     if larger.size <= r.size // 2:
    #       return r
    #     else: find_vertex(larger)
    # if r.left.size == r.right.size:
    #     return r
    # else:
    #     larger = r.left if (r.left.size > r.right.size) else r.right
    #     find_vertex(larger)

    ##### DRAFT 1
    # larger = r.left if (r.left.size > r.right.size) else r.right
    # smaller = r.left if (r.left.size < r.right.size) else r.right

        # if (r.parent.size - r.size <= r.parent.size / 2) && (larger < r.parent.size / 2):
        #   return r
        # larger.size <= r.parent.size / 2): # hmmm maybe can't check against a constant.
    #     return larger
    # else: find_vertex(larger)


    # if equal to each other, return larger?

    # each time we recurse on a new node, we have root, 

    # check whether left or right child of curr v has larger potential function by checking their "size"
    # (when curr v is removed, child's size will be remaining subtree size)
        # if left subtree has larger potential function,
        #   check if potential function is <= n/2. if so, return curr v. 
        # if left subtree has larger potential function, do the same
        # if size of either subtree is None, then you've reached a root. (maybe not necessary?)
    # pass
