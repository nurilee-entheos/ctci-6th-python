# Example 1

def foo(int_array):
    sum = 0
    product = 1
    for i in range(len(int_array)):
        sum += int_array[i]

    for i in range(len(int_array)):
        product *= int_array[i]
    
    print(str(sum) + ", " + str(product))

test_array = [1,2,3,4,5]
foo(test_array)

"""
1. answer:
O(N) time. The fact that we iterate through the array twice doesn't matter.

2. explanation:
Drop the constants for the two "for loops". This is not O(2N) but O(N).

"""