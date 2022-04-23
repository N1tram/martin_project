def try_me(name='Martin'):
    """Hej! Welcome to my function.
    The try me function takes your name as an input
    and returns your name the other way around.
    Example: try_me('Martin') returns 'Nitram'."""
    new_name_list = []
    if name != 'Martin':
        for i in range(len(name)):
            new_name_list.append(name[-i-1].lower())
            output = ''.join(new_name_list).capitalize()
    else:
        output = 'Please provide your name (string) as an input to the function.'
    return output

if __name__ == "__main__":
    print(try_me('Adam'))
