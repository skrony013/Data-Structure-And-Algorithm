# Runtime Complexity: log(N^2)
# Space Complexity: O(1)

def bubble_sort(Ar, n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if Ar[j] > Ar[j + 1]:
                temp = Ar[j]
                Ar[j] = Ar[j + 1]
                Ar[j + 1] = temp


arr = list(int(n) for n in input().split())
n = len(arr)
bubble_sort(arr, n)
print("Sorted Array is:", arr)
