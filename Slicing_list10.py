def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    
    
    a=list1[::-1]
    return a[0:-n]
list1=[1,2,3,4,5,6,7,8]
print(main(list1,2))