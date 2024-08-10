from heapq import nlargest, nsmallest


def three_largest_smallest(my_dict):
    return nlargest(3, my_dict, key=my_dict.get), (nsmallest(3, my_dict, key=my_dict.get))


dic = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
three_largest, three_smallest = (three_largest_smallest(dic))
print(f"Three Largest : {three_largest}")
print(f"Three Smallest : {three_smallest}")