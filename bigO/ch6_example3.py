# Example 3

def printPairs(int_array):
    for i in range(len(int_array)):
        for j in range(i+1,len(int_array)):
            print(str(int_array[i]) + "," + str(int_array[j]))

test_array = [1,2,3,4,5,6,7,8]
printPairs(test_array)

"""
1. answer:
O(N^2) time. 

2. explanation:
1) Counting the iterations
(N-1) + (N-2) + ... + 1 = N(N-1)/2 ==> O(N^2)

2) What It Means
N^2 total pairs, half of those will have i < j and the remaining half will have i > j so except the half of i > j
==> N^2/2 ==> O(N^2)

3) Visualizing What It Does
NxN matrix which has size roughly N^2/2 ==> O(N^2)

4) Average Work
The outer loop runs N times and the inner loop runs on average N/2 so N*N/2 ==> O(N^2)

"""
