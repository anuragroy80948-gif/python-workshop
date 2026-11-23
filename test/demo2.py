# Demonstrate list update, append, pop, index, and remove.
a = [18, 52, 98]

a[1] = 60         
a.append(75)        
position = a.index(98)  
removed_item = a.pop()  
a.remove(18)       

print(a)
print("Index of 98:", position)
print("Popped item:", removed_item)

