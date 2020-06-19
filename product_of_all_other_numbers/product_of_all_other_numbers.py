'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    product_arr = []
    
    for i in range(0, len(arr)):
        to_product = []
        for j in range(0, len(arr)):
            if i != j:
                to_product.append(arr[j])
        
        res = 1
        for nums in to_product:
            res = res * nums
        product_arr.append(res)
    
    return product_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]

    print(product_of_all_other_numbers(arr))
