#%% md
# 
# ## Use Case 6: Import vs from import
# 
# Create simple functions like add(a,b) and div(a,b) that  returns sum and division of 2 input.
# Create a package/sub package/generic_functions.py and place this function .
# Create another package/sub package/consumer.py and import the above 2 functions using import, from import with and without alias.
# 
#%%
def add(num1,num2):
    return num1+num2
#print(add(10,20))

def div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 'Except non zero number'
#print(div(1,2))
#print(div(1,0))
#print(div(2,-2))
