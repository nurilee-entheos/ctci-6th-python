def printUnorderedPairs(int_arrayA, int_arrayB):
    for i in range(len(int_arrayA)):
        for j in range(len(int_arrayB)):
            for k in range(100000):
                print(str(int_arrayA[i])+ "," + str(int_arrayB[j]))

test_arrayA = [3,6,2,3,1,6,2]
test_arrayB = [2,3,1,5,6,3,6]
printUnorderedPairs(test_arrayA, test_arrayB)


"""
1. answer:
O(ab) where  a = len(arrayA) and b = len(arrayB).

2. explanation:
Drop the constant so still the runtime is O(ab)

"""