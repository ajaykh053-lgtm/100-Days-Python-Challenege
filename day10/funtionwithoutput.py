def mul():
    result = 3 * 2
    return result


print(f"Output={mul()}")
print("\n" * 10)


# Formstiing the Unfrmated words
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())


conitnue_name = True
while conitnue_name:
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    format_name(first_name, last_name)
    user_choice = input("Do you want to do it again ? \n 'yes' or 'no' ")
    if user_choice == "no":
        conitnue_name = False
print("\n" * 10)


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


conitnue_name = True
while conitnue_name:
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    print(format_name(first_name, last_name))
    user_choice = input("Do you want to do it again ? \n 'yes' or 'no' ")
    if user_choice == "no":
        conitnue_name = False
