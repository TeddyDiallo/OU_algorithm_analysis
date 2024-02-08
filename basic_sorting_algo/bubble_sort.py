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


data = [0,4,1,8,3,20,10,-1]
bubble_sort(data)
print(data)

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]