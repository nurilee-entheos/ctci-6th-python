# Example 2

def printPairs(int_array):
    for i in range(len(int_array)):
        for j in range(len(int_array)):
            print(str(int_array[i]) + "," + str(int_array[j]))

test_array = [1,2,3,4,5]
printPairs(test_array)

"""
1. answer:
O(N^2) time. 

2. explanation:
The inner for loop has O(N) iterations and it is called N times. Therefore, the runtime is O(N^2).

Also there are total O(N^2) pairs when printing so the runtime is O(N^2)

"""