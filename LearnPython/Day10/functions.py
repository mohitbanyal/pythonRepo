#Title letter names

def format_name(f_name,l_name):
    #f_name = f_name[0].upper() + f_name[1:].lower()
    #l_name = l_name[0].upper() + l_name[1:].lower()

    return f"{f_name.title()} {l_name.title()}"

print(format_name("mOHIT","banYAL"))