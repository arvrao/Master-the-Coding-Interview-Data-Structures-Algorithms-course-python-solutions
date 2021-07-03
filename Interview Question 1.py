Write a function to check for any common item in the given list of strings. Return true if anything is common, else return false.

def func(x,y):
    for i in range(len(x)):
        for j in range(len(y)):
            if(x[i]==y[j]):
                return True
        return False


print(func(['a','b','c'],['x','y','z','a']))  # return true
print(func(['a','b','c'],['x','y','z']))  # return false
