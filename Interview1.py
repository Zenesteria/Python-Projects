#interview question #1

a = [-1, 5, 12, 14, 2, 1, 92]

def ArraySorter(a):
    print("Array Length: %s" %(len(a)))
    k = 3
    if len(a) > k:
        for i in range(len(a)-2):
            new_a = []
            while len(new_a) < k:
                first_index = a[i]
                new_a.append(first_index)
                i += 1

            print(new_a)
    else:
        print('Sorry array is too small')

ArraySorter(a)