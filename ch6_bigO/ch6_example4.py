def printUnorderedPairs(int_arrayA, int_arrayB):
    for i in range(len(int_arrayA)):
        for j in range(len(int_arrayB)):
            if int_arrayA[i] < int_arrayB[j]:
                print(str(int_arrayA[i])+ "," + str(int_arrayB[j]))

test_arrayA = [3,6,2,3,1,6,2]
test_arrayB = [2,3,1,5,6,3,6]
printUnorderedPairs(test_arrayA, test_arrayB)


"""
1. answer:
O(ab) where  a = len(arrayA) and b = len(arrayB).

2. explanation:
The if statement within j's for loop is O(1).

for each element of arrayA, the inner loop goes through b iterations, where b = len(arrayB).
If a = len(arrayA), then the runtime is O(ab)

It's not O(N^2) because there are two different inputs. 

"""