# Median Program
def FindMedian(a, n):
    sorted(a)

    # check if the array is not even

    if n%2 != 0:
        print('odd array')
        return (a[int((n-1)/2)])
    return ((a[int((n-1)/2)]+ a[int((n/2))])/2)

a=[1,2,3,4,5,6]
n = len(a);

print("Median "+str(FindMedian(a, n)))