def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    idx_zero = 0
    chaser_idx = 0
    idx_two = len(input_list) - 1

    while chaser_idx <= idx_two:
        if input_list[chaser_idx] == 0:
            # if item at indices for 0 are already zero, no need to perform a swap
            # swapping 0 with a 0 is useless so just move ahead
            if[idx_zero] == 0:
                idx_zero += 1
                continue
            input_list[idx_zero], input_list[chaser_idx] = input_list[chaser_idx], input_list[idx_zero]
            idx_zero += 1
            chaser_idx += 1

        elif input_list[chaser_idx] == 1:
            chaser_idx += 1

        else:
            # same optimization as above
            if[idx_two] == 2:
                idx_two -= 1
                continue
            input_list[idx_two], input_list[chaser_idx] = input_list[chaser_idx], input_list[idx_two]
            idx_two -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

test_function([2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1]) 
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) 
test_function([]) 
test_function([0,2])
test_function([2,2,0,0])
test_function([2,1,1])
test_function([0,0,0,0,2,0,0,0,0])