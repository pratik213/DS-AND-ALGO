#Example for time complexiy at constant time
def great(a,b):
    if a>b:
       return True
    else:
        return False
print(great(4,5))



#Example 2
def first_item(data):
    return data[0]

if __name__=='__main__':
    data=[5,2,5,2,4]
    print(first_item(data))
