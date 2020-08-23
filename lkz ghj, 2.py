lst=[2,12,3,35,365,85,45,689,25,25]
def bubble_sort(array):
    for i in range (len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
bubble_sort(lst)
print(lst)