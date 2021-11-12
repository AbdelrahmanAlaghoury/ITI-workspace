# In[1]:


# Iterator factorial
def factorial(number):
    if number <=1 : return 1
    factorial = 1
    for n in range(2, number+1):
        factorial *= n
    return factorial
factorial(5)


# In[2]:


# Recursive factorial
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)
factorial(5)


# In[3]:


# Iteration Fibonacci Series
def fibonacci(n):
    f = [0, 1]
    if n <= 2 and n > 0:
        return f[n-1]
    elif n <= 0: return -1
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f[-1]
fibonacci(10)


# In[4]:


# Recursive Fibonacci Series
def fibonacci(n):
    if n <= 0 : return -1 
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)


# In[5]:


# Iteration Greatest Common Divisor (GCD)
def GCD(n1, n2):
    while n2:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1
GCD(21,27)


# In[6]:


# Recursive Greatest Common Divisor (GCD)
def GCD(n1, n2):
    if n2 == 0:
        return n1
    return GCD(n2, n1%n2)
GCD(54, 24)


# In[7]:


# Iterations insertion_sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while(j >= 0 and key < arr[j]):
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1

arr = [10,9,45,4,7,2]
insertion_sort(arr)
arr


# In[8]:


# Recursive insertion_sort
def insertion_sort(arr, i, n):
        key = arr[i]
        j = i-1
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
        if i + 1 < n:
            insertion_sort(arr, i + 1, n)
arr = [10,9,45,4,7,2]
insertion_sort(arr, 0, len(arr))
arr


# In[9]:


# Iteration bubble_sort
def bubble_sort(arr):
    swap_flag = 1
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = 0
        if swap_flag:
            print("Sorted array!!!")
            break
arr = [10,9,45,4,7,2]
arr_2 = [2, 4, 7, 9, 10, 45]
bubble_sort(arr)
print(arr)

# bubble_sort(arr_2)
# arr_2


# In[10]:


# linear search
def linear_search(arr, element):
    for value in arr:
        if value == element:
            return arr.index(value)
    return False
linear_search(arr, 45)


# In[11]:


# Recursive linear search
def linear_search(arr, element, index = 0):
    if index > len(arr):
        return index
    elif arr[index] == element:
        return index
    return linear_search(arr, element, index+1)
arr_test_search = [2, 4, 7, 9, 10, 45]
print(linear_search(arr_test_search, 45))


# In[12]:


# Iteration Binary Search
def binary_search(arr, element):
    low = 0
    high = len(arr) - 1 
    while(high >= low):
        mid = int((high + low) /2)
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            high = mid-1
        else:
            low = mid+1
print(binary_search([2, 4, 7, 9, 10, 45], 9))


# In[21]:


# Recursive Binary Search
def binary_search(arr, element, high, low = 0):
    if(high < low):
        return -1
    
    mid = int((high + low) /2)
    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        return binary_search(arr, element, mid-1, low)
    else:
        return binary_search(arr, element, high, mid+1)
arr_test = [2, 4, 7, 9, 10, 45]
binary_search(arr_test, 4, len(arr_test))


# In[14]:


# Last one stand Quiz
ppl = list(range(1, 8))
def last_one(number_of_pepole):  
    ppl = list(range(1, number_of_pepole+1))
    i = 0
    while(len(ppl) != 1):
        print(ppl)
        i += 1
        i = i % len(ppl)
        ppl.pop(i)
    return ppl[0]
last_one(7)




