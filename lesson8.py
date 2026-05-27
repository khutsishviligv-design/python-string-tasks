
#davaleba1
def minmax_calculator (*args):
   min_=min(args)
   max_=max(args)
   return (min_,max_)

print(minmax_calculator (10,5,6,100))

#davaleba2
kewy= input("What is your Operation? select from the list: "
"sum"" "
"max" " "
"min" " "
"mult:")
def calculate (*args):
    if kewy=="sum":
        return sum(args)
    elif kewy=='max':
        return max(args)
    elif kewy=='min':
        return min(args)
    elif kewy=='mult':
        result =1
        for n in args:
            result *= n
        return result


    else:
        return "please select operator from the list"


print(calculate (5,10))

#davaleba3:

def format_user(first_name, last_name, **kwargs):
    full_name = first_name + " " + last_name

    if kwargs:
        return full_name + " | " + str(kwargs)
    else:
        return full_name



#davaleba4:
def safe_divide(a,b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a//b, a%b
print (safe_divide(10,3))
