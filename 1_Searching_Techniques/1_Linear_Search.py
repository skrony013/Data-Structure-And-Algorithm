# Time Complexity in case of The Worst Case: O(N)
# Space Complexity: O(1)

t = int(input())
while t:
    def linear_search(Arr, n, Item):
        for i in range(0, n):
            if Arr[i] == Item:
                return i
        return -1


    print("Enter the Element of Array:")
    arr = list(int(n) for n in input().split())
    n = len(arr)
    print("Enter the item to be searched from the array:")
    item = int(input())
    index = linear_search(arr, n, item)
    if index == -1:
        print("Item not found")
    else:
        print("Item Found At the index:", index)
    t -= 1
