#lab4.py

# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME
# EMAIL
# STUDENT ID

import random

"""
The default numbers here are generally good enough to create a rich tree. 
You are free to play with the numbers if you want. Lower numbers will simplify the results, 
larger numbers will take more time to render and create hundreds of acorns.
"""

TREE_DEPTH = 5
NODE_DEPTH = 5

def tree_builder(nodes:list, level:int, acorn:str) -> list:
    """
    Builds a tree using the random integers selected from the tree_depth and node_depth defaults
    """
    r = random.randrange(1, NODE_DEPTH)
    for i in range(r):
        if level < TREE_DEPTH:
            level_id  = f"L{level}-{i}"
            if level_id == acorn:
                level_id += "(acorn)"
            n = [level_id]
            nodes.append(tree_builder(n, level+1, acorn_placer()))

    return nodes

def acorn_placer() -> str:
    """
    Returns a random acorn location based on tree_depth and node_depth defaults
    """
    return f"L{random.randrange(1,TREE_DEPTH)}-{random.randrange(1,NODE_DEPTH)}"

def run():
    # create a tree and start placing acorns
    tree = tree_builder([], 1, acorn_placer())
    # print the tree for testing. 
    # TODO: REMOVE THIS PRINT STATEMENT BEFORE YOU SUBMIT YOUR LAB
    print(tree)
    
    # insert your solution code here
    acorn_list = [] #will be a nested list 
    path_list = []
    locate_acorns(tree, tree[1:], acorn_list, path_list)
    print("You have", len(acorn_list), "acorns on your tree!\nThey are located on the following branches:")
    for path in acorn_list:
        for i in range(len(path)):
            if i == len(path)-1: #if it's the last elem (acorn) in path
                print(path[i][:4]) #get rid of the (acorn) at the end when printing using slicing
            else:
                print(path[i], "->")
    # end solution

def locate_acorns(tree, branches, acorn_list, path_list): #should return a list of paths 
    #len(tree) should be tree depth 
    if branches != tree[len(tree)-1:]: #if node of tree has no branches (aka leaf node)
        if not tree[len(tree)-1:].endswith('acorn'): #if reached leaf node & is not an acorn, empty path_list 
            path_list = []
        else:
            acorn_list.append(branches[0])
            acorn_list = [pathlist + acorn_list] #combine the 2 lists together to make acorn_list a nested list 
    else: #node of tree has branches 
        for i in range(len(tree)):
            path_list.append(tree[0]) #tree[0] = label at the node 
            if tree[branches[0]].endswith('(acorn)'): #if the last node on branch is an acorn
                acorn_list.append(branches[0])
                acorn_list = [pathlist + acorn_list] #combine the 2 lists together to make acorn_list a nested list 
            locate_acorns(branches, tree[i+2:], acorn_list, path_list)

if __name__ == "__main__":
    print("Welcome to PyAcornFinder! \n")

    run()

# Citations:
# - https://www.youtube.com/watch?v=qFCJANh5ht8

#keep track of the path: always add the path to path_list, until a branch is reached, extend acorn_list to include path_list
