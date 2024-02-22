my_list = []       # Create an empty list

  # Append the list [10, 20, 30, 40] to my_list
my_list.append(10) 
my_list.append(20) 
my_list.append(30) 
my_list.append(40) 

my_list.insert(1, 15)  # Insert the value 15 at index 1

my_list.extend([50,60,70])
my_list.pop()       # Remove the last element of the list
my_list.sort()      # Sort the list in ascending order


print(my_list.index(30))

