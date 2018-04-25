# Overview
While vacationing on the galapogos island (camping over night illegally as I am 'oft-to-do', I came upon a small bird, yellow in color and surprisingly friendly. After watching it run around the beach for a while I notices it's footprints were spelling out words...

## Challenge
### Specifications
- Create a new branch in your `data-structures-and-algorithms` repository called `k-tree`. **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Create a new directoruy called `k_tree/`, with all of your standard module configuration for each directory
    - `__init__.py`, `README.md`, etc.
- Create a file called `k_tree.py`, as well as a test file and a config file for your tests.

- In `k_tree.py`:
    - Create a Class or a `Node` which is aware of the value as `val` and children as a list collection of Nodes
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the node
    - Create a Class for a `KTree`, which is aware of the root of the tree as `root`
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the tree
        - This class should be aware of depth-first traversal methods for `pre_order`, and `post_order` traversals
        - This class should be aware of a breadth-first traversal method
        - This class should have the ability to `insert` a new node into the tree at a given parent node

- Ensure that your class and any subsequent methods are properly tested, and that your test coverage is above 80%.


### Submission
1. Create a pull request from your `k_tree` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `k_tree` into `master`

## acknowledgements
I was super stumped by this and used beverly's code as a guidepost for much of what I did with Queues.