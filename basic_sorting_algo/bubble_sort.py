def bubble_sort(array):
    size = len(array) - 1

    #Sort in ascending order 
    for j in range (size):
        swapped = False #To check if array is already swapped
        for i in range(size - j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if not swapped:
            break

def bubble_sort_key(data, key):
    size = len(data) -1

    for j in range(size):
        for i in range(size - j):
            first_item, second_item = elements[i], elements[i+1] #extracted one dictionary 
            first_value, second_value = first_item[key], second_item[key]
            if first_value > second_value:
                elements[i], elements[i+1] = second_item, first_item #swapping

    pass

data = [0,4,1,8,3,20,10,-1]
bubble_sort(data)
print(data)

elements = [
        { 'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort_key(elements, "transaction_amount")
print(elements)