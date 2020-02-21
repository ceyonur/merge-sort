import heapq
import os

# Total of O(k*N/k) = O(N) reading files
def read_files(folder_path):
    result = []
    # O(k) following loop
    for filename in os.listdir(folder_path):
        filepath = folder_path + '/' + filename
        # Maybe N/k numbers? so O(N/k) following line
        result.append([int(line.rstrip('\n')) for line in open(filepath)])
    return result

# O(n) complexity
def write_file(list, path):
    with open(path, 'a') as out:
        out.write('\n'.join(map(str, list)))

current_path = os.getcwd() + '/'
num_array = read_files(current_path + "files")
# Referred to https://docs.python.org/2/library/heapq.html#theory
# Since we have already sorted lists, we can use merge function directly.
# It returns iterable so we don't actually pull all data.
# When we add the elements to list the space would become O(N)
sorted_list = list(heapq.merge(*num_array))
write_file(sorted_list, current_path + "result.txt" )

# Same thing can be done with constructing heap at the first when we read the numbers.
# Then also we have to use heapq.pop method to pop each item.
