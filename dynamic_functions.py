# a function with args and kwargs
def dynamic_function(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)
    for arg in args:
        print("Argument:", arg)    
    for key, value in kwargs.items():
        print(f"Keyword Argument: {key} = {value}")
dynamic_function(1, 2, 3, name="Alice", age=30)