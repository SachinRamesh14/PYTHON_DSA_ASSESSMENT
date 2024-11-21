                               # Python Problems - DSA

# 1. You are given an array containing n integers and an integer x. Write a function to determine whether the element x exists in the array. If it exists, return the index of its first occurrence; otherwise, return -1.
# Input: arr = [1, 2, 3, 4], x = 3
# Output: 2

def find_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1, 2, 3, 4]
x = 3
print(find_index(arr, x))



# 2. You are given an array of n integers. For each element in the array, find the next greater element. The next greater element for an element x is defined as the first element greater than x that appears to its right in the array. If no such element exists, return -1 for that element.
# Input: arr = [ 4 , 5 , 2 , 25 ]
# Output:  4      –>   5
#          5      –>   25
#          2      –>   25
#          25    –>   -1

def next_greater_element(arr):
   result = [-1] * len(arr)
   stack = []

   for i in range(len(arr)):
       while stack and arr[stack[-1]] < arr[i]:
           index = stack.pop()
           result[index] = arr[i]
       stack.append(i)

   return result


arr = [4, 5, 2, 25]
output = next_greater_element(arr)
for i, val in enumerate(arr):
   print(f"{val} -> {output[i]}")


# 3. Given a string str consisting of opening and closing parenthesis ‘(‘ and ‘)‘. Find the length of the longest valid parenthesis substring.
# Input: ((()
# Output : 2

def longest_valid_parentheses(s):
   stack = [-1]
   max_length = 0

   for i in range(len(s)):
       if s[i] == '(':
           stack.append(i)
       else:
           stack.pop()
           if not stack:
               stack.append(i)
           else:
               max_length = max(max_length, i - stack[-1])

   return max_length

s = "((()"
print(longest_valid_parentheses(s))


# 4. Write a python function to sort a given list of integers. The algorithm repeatedly selects the smallest element from the unsorted portion of the list and swaps it with the first element in that portion. This process continues until the entire list is sorted.
# Input: [14, 46, 43, 27, 57, 41, 45, 21, 70]
# Output : [14, 21, 27, 41, 43, 45, 46, 57, 70]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print(selection_sort(arr))


# 5. You are given a list of employees' names, each represented as a string. Write a program to sort the list of names in lexicographical order using appropriate algorithm. Avoid using built-in sorting functions like sorted() or .sort().
# Input: ["Steve", "Alice", "bob", "Charlie", "dave"]
# Output : ['Alice', 'Charlie', 'Steve', 'bob', 'dave']

def lexicographical_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j].lower() > names[j + 1].lower():
                names[j], names[j + 1] = names[j + 1], names[j]
    return names


names = ["Steve", "Alice", "bob", "Charlie", "dave"]
print(lexicographical_sort(names))


