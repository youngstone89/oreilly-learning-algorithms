from typing import List


def alternate(a: List[str]):
    compare_cnt = 0
    for v in a:
        v_is_largest = True
        for x in a:
            compare_cnt += 1
            # 주요 연산(main operation)
            if v < x :
                v_is_largest = False
                break
        if v_is_largest:
            print("found largest compare count: {}".format(compare_cnt))
            return v
    print("None largest compare count: {}".format(compare_cnt))
    return None


# main operation execution : N times
best_case = [9,5,2,1,3,4]

max = alternate(best_case)
print("best case max : {}".format(max))

# ascending order
# main operation execution: (N squre + 3N-2)/2
worst_case = [1,2,3,4,5,9]
max = alternate(worst_case)
print("worst case max : {}".format(max))

