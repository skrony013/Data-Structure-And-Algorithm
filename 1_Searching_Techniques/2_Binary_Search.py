# Runtime Complexity: log(N)
# Space Complexity: O(1)

t = int(input())
while t:
    def Binary_Search(Arr, N, Item):
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if Arr[mid] == Item:
                return mid
            elif Item > Arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


    arr = list(int(n) for n in input().split())
    n = len(arr)
    item = int(input())
    index = Binary_Search(arr, n, item)
    if index == -1:
        print("Not Found")
    else:
        print("Item found at the index of:", index)
    t -= 1
