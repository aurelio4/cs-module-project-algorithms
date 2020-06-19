'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr.insert(count, arr.pop(i))
            count += 1
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")