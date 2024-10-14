def is_prime(n):
    """
    Checks if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Corrected condition
            return False
    return True

def sum_of_digits(n):
    """
    Calculate the sum of the digits of a given number.
    
    Args:
    n (int): The number to calculate the sum of digits for.
    
    Returns:
    int: The sum of the digits.
    """
    sum = 0

    while(n > 0):
        sum += n%10
        n //= 10

    return sum

def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    
    Args:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1] 

def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of the number.
    """
    if n == 0:
        return 1
    
    fact_n = n
    n -= 1

    while n > 0:
        fact_n *= n
        n -= 1

    return fact_n

def count_vowels(s):
    """
    Count the number of vowels in a given string.
    
    Args:
    s (str): The string to count vowels in.
    
    Returns:
    int: The number of vowels in the string.
    """
    vowels = ['a','e','i','o','u']
    num_vowels = 0

    for char in s:
        if char.lower() in vowels:
            num_vowels += 1
            
    return num_vowels

def find_maximum(lst):
    """
    Find the maximum value in a list of numbers.
    
    Args:
    lst (list): The list of numbers.
    
    Returns:
    int: The maximum value in the list.
    """
    max = -2**31

    for i in range(0, len(lst)):
        if lst[i] > max:
            max = lst[i]
    
    return max

def sum_of_list(lst):
    """
    Calculate the sum of all elements in a list.
    
    Args:
    lst (list): The list of numbers.
    
    Returns:
    int: The sum of all elements in the list.
    """
    sum = 0

    for i in range(0, len(lst)):
        sum += lst[i]
    
    return sum

def is_even(n):
    """
    Check if a given number is even.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return n%2==0

def longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The length of the longest substring without repeating characters.
    """
    # Implement the function here
    pass

def merge_intervals(intervals):
    """
    Merge all overlapping intervals.
    
    Args:
    intervals (list of list of int): A list of intervals where each interval is a list of two integers.
    
    Returns:
    list of list of int: The merged intervals.
    """
    # Implement the function here
    pass

def word_ladder(begin_word, end_word, word_list):
    """
    Find the length of the shortest transformation sequence from begin_word to end_word.
    
    Args:
    begin_word (str): The starting word.
    end_word (str): The target word.
    word_list (list of str): The list of allowed words.
    
    Returns:
    int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """
    # Implement the function here
    pass

def reverse_words(s):
    """
    Reverse the order of words in a given string.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The string with the order of words reversed.
    """
    word_list = s.split()

    if len(word_list) == 0:
        return ''

    revS = ''

    for string in reversed(word_list):
        revS += string + ' '
    
    revS = revS[:-1]

    return revS

def first_unique_char(s):
    """
    Find the first non-repeating character in a given string and return its index.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The index of the first non-repeating character, or -1 if it doesn't exist.
    """
    if len(s) == 0:
        return -1
    
    if len(s) == 1:
        return 0
    
    charMap = {}

    for i in range(0, len(s)):
        if s[i] in charMap:
            charMap[s[i]] += 1
        else:
            charMap[s[i]] = 1

    uniqueVal = ''

    for key in charMap:
        if charMap[key] == 1:
            uniqueVal = key
            break
    
    if uniqueVal == '':
        return -1

    for i in range(0, len(s)):
        if s[i] == uniqueVal:
            return i

    return -1

def is_valid_parentheses(s):
    """
    Determine if the input string containing just the characters '(', ')', '{', '}', '[' and ']' is valid.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the input string is valid, False otherwise.
    """
    # Implement the function here
    pass

def remove_duplicates(nums):
    """
    Remove duplicates from a sorted array in-place and return the new length.
    
    Args:
    nums (List[int]): The input sorted array.
    
    Returns:
    int: The new length of the array after removing duplicates.
    """
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return 1

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i-1]:
            nums.pop(i)

    return len(nums)

def two_sum(nums, target):
    """
    Find two numbers in the array that add up to the target and return their indices.
    
    Args:
    nums (List[int]): The input array of integers.
    target (int): The target sum.
    
    Returns:
    List[int]: The indices of the two numbers that add up to the target.
    """
    if len(nums) == 0 or len(nums) == 1:
        return None

    for i in range(0, len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None

def is_anagram(s, t):
    """
    Determine if t is an anagram of s.
    
    Args:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    if len(s) != len(t):
        return False
    
    charMapS = {}
    charMapT = {}

    for i in range(0, len(s)):

        if s[i] in charMapS:
            charMapS[s[i]] += 1
        else:
            charMapS[s[i]] = 1

        if t[i] in charMapT:
            charMapT[t[i]] += 1
        else:
            charMapT[t[i]] = 1

    for key in charMapS:
        if key not in charMapT:
            return False
        elif charMapS[key] != charMapT[key]:
            return False
    
    return True