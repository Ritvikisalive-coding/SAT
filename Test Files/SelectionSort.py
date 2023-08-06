import csv
'''
def partition(data, low, high):
    i = low - 1
    pivot = data[high][1]
    for j in range(low, high):
        if data[j][1] <= pivot:
            i += 1
            data[i][1], data[j][1] = data[j][1], data[i][1]
    data[i+1][1], data[high][1] = data[high][1], data[i+1][1]
    return i+1

def quick_sort(data, low, high):
    if low < high:
        pa = partition(data, low, high)
        quick_sort(data, low, pa-1)
        quick_sort(data, pa+1, high)

data = []
with open("csv/teacherallbooking.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
for i in range(len(data)):
    data[i][1] = int(data[i][1])
    data[i][0] = str(data[i][0])
    data[i][2] = str(data[i][2])
    print(data[i][1])


low = 1
high = len(data) - 1
quick_sort(data, low, high)
total_rows = len(data)
total_columns = len(data[1])
for i in range(total_rows):
            for j in range(total_columns):
                 print(data[i][j])
total_columns = len(data[1])
for i in range(total_rows):
            for j in range(total_columns):
                 print(data[i][j])
total_columns = len(data[2])
for i in range(total_rows):
            for j in range(total_columns):
                 print(data[i][j])
'''

data = []
with open("csv/teacherallbooking.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

def selectionSort(data, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if data[i][1] < data[min_idx][1]:
                min_idx = i
         
        # put min at the correct position
        (data[step], data[min_idx]) = (data[min_idx], data[step])


size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
