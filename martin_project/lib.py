def try_me(name):
    """Hej! Welcome to my function.
    The try me function takes your name as an input
    and returns your name the other way around.
    Example: try_me('Martin') returns 'Nitram'."""
    new_name_list = []
    for i in range(len(name)):
        new_name_list.append(name[-i-1].lower())
    return ''.join(new_name_list).capitalize()

if __name__ == "__main__":
    print(try_me('Martin'))
