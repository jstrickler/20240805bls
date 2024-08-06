    
x = 42  # (file) global variable

#  local -> nonlocal -> global -> builtin

def function_b():
    z = 32  # local variable
    print("function_b(): z is", z)  # local scope
    print("function_b(): x is", x)  # global scope
    print("function_b(): type(x) is", type(x))  # 'type()' is builtin scope


f = function_b()  