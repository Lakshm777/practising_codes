# Find the largest number in an array
'''numbers = [5,8,9,6,4,7]
print(max(numbers))'''

# OR

def largest_number(arr):
    if not arr:
        return None
    
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
 

numbers = [5,2,7,1,9]
print(largest_number(numbers))