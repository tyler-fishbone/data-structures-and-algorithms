
""" These are not my solutions. it is one I found on the internet that I am still trying to understand. I am not getting this stuff... """

# source = [4,3,2,1]
# aux = []
# target = []

# def towers_of_hanoi(n, source, aux, target):
#     """ recursive solution for tower of hanoi puzzle """
#     recursion(n, source, target, aux)
#     return target

# def recursion(n, source, target, aux):
#     if len(target) < n:
#         print('hit')
#         disc = source.pop()
#         aux.append(disc)
#         recursion(n, target, source, aux)

# print(towers_of_hanoi(4, source, aux, target))

# print('source: {}'.format(source))
# print('aux: {}'.format(aux))
# print('target: {}'.format(target))


def hanoi(n, source, helper, target):
    print('hanoi( ', n, source, helper, target, ' called')
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print(' moving ' + str(disk) + ' from ' + source[1] + ' to ' + target[1])
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = ([3,2,1], 'A')
target = ([], 'C')
helper = ([], 'B')
hanoi(len(source[0]),source,helper,target)

print(source, helper, target)