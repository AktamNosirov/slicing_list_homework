def main(numbers):
    """
    A list called numbers is given. Return the items in the odd index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return numbers[0:-1:2]
list1=[1,2,3,4,5,6,7,8]
print(main(list1))