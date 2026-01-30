#========================================================================================
# 2.1 INPUT VALIDATION FUNCTION
def get_valid_input(question, type_func=str):
    """
    Docstring for get_valid_input
    
    Args: 
    - userinput (string) : the input entered by user 
    - type_func (type object): the type we want to validate the input with when we called the fuction
    Returns:
    - type_func(user_input) : the user input casted into specified data type

    """
    while True:
        try:
            #here type_func variable will be have class of "type" not string
            user_input = input(question).strip()
            if not user_input:  #if empty continue
                continue 
            if type_func == int or type_func == float :
                #print("number detected")
                if int(user_input) <= 0 :
                    print(f"  Invalid input. Please enter a valid positive number.")
                    continue
            if type_func == str and user_input.isdigit():
                print("product name must be mix of alphabets and numbers")
                continue
            return type_func(user_input) #will be evaluated as str(user_input) by default unless the type is specified
        except ValueError:
            print(f"  Invalid input. Please enter a valid {type_func.__name__}.") #this will just print "int"
            #print(f"  Invalid input. Please enter a valid {type_func}.") #this will print <class 'int'>

