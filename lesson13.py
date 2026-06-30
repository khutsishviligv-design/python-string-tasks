#davaleba1
def safe_get(lst, index):
    try:
        return lst[index]

    except IndexError:
        print("Error: There is no item with this index")

    except TypeError:
        print("Error: Index is not a number")



my_list = [10, 20, 30]

print(safe_get(my_list, 1))
print(safe_get(my_list, 10))
print(safe_get(my_list, "a"))
#davaleba2

def safe_get_value(dictionary, key):
    try:
        return dictionary[key]

    except KeyError:
        print(f"Error: Key '{key}' doesn't exist")
        return None


print(safe_get_value({"a":1,"b":2},"5") )
#davaleba3

try:
    costumer_input=int(input("Enter your number:"))
    square=costumer_input**2

except ValueError:
    print("Please enter a number")
else:
 print (square)
finally:
 print(" მადლობა, ოპერაცია დასრულებულია")
