from typing import List


def largest(a: List[str]):
    my_max = a[0] # get value at zero index
    for idx in range(1, len(a)):
        # main operation
        if my_max < a[idx]:
            my_max = a[idx]
    return my_max



a = [1,5,2,9,3,4]

# main operation execution: N-1
max = largest(a)
print(max)

