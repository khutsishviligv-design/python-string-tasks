#davaleba1:

def my_decorator (fun):
    def wrapper(a,b,action):
        if a < 0 or b < 0:
            return "Only positive numbers are alloewed"
        return fun(a,b,action)
    return wrapper

@my_decorator
def mathematicalactions(a,b,action):
    if action=="add":
        return a+b
    elif action=="subtract":
        return a-b
    elif action=="multiply":
        return a*b
    elif action=="divide":
        return a/b

print(mathematicalactions(20,10,"multiply"))
#davaleba2

from functools import wraps
def my_decorator(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)

        return (
            f"called function '{fun.__name__}', "
            f"with attributes {args[0]} and {args[1]}, "
            f"returned {result}"
        )
    return wrapper
@my_decorator
def add(a,b):
    return a+b
@my_decorator
def subtract(a,b):
    return a-b

print (add(3,5))

davaleba 3
import time


def my_decorator(times, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
                time.sleep(delay)
        return wrapper
    return decorator


@my_decorator(3, 2)
def my_func():
    print("Hello Hello")


my_func()
davaleba 4
current_user = {
    "username": "Nika",
    "role": "admin"  # შეცვალე შემდეგში სხვადასხვა როლზე ტესტირებისთვის
}

def role_required(role):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if current_user["role"] != role:
                print("You dont have permission to access this resource")
            return function(*args, **kwargs)
        return wrapper
    return decorator
@role_required("admin")
def delete_user(user_id):
    print(f" User {user_id} has been deleted")
@role_required("editor")
def edit_user(user_id):
    print(f" User {user_id} has been edited")
@role_required("user")
def create_user(first_name):
    print(f" User {first_name} has been created")




print(delete_user(1))
edit_user(2)
create_user("Nika")
