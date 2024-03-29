"""
A challenge to write a function that returns true if there are an even number of even numbers

writing the assertions first and working backwards
"""

def even_number_of_evens(number):
    even_number_count = 0

    for n in number:
        if n % 2 == 0:
            even_number_count += 1

    return even_number_count > 0 and even_number_count % 2 == 0


assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even number"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print ("All tests passed!")