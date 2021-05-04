def filter_list(l):
    """This function takes a list of non-negative integers and strings, and filters the strings out"""
    return [item for item in l if isinstance(item, int)]


if __name__ == '__main__':
    # tests
    print(filter_list([1,'a','b',0,15]))
    print(filter_list([1,2,'a','b']))
    print(filter_list([1,2,'aasf','1','123',123]))