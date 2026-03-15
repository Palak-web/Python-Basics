# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if  i == True:
            count +=1 
    return count

print(count_sheeps([True, True, False, True, False, True]))  
print(count_sheeps([True, False, True, True, False]))
print(count_sheeps([False, False, False]))       
