def main(list1,n):
    """
    A list of several elements is given. Return all items except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[n:-1]
list1=[1,2,3,4,5,6,7,8]
print(main(list1,3))