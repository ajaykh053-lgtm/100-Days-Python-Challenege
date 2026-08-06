import random

letter = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
    "r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H",
    "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to Password geneterator")
nr_letter = int(input(f"How many letter would you like in your password.\n"))
nr_number = int(input(f"How many number would you like?\n"))
nr_symbols = int(input(f"How many symbls would you like?\n"))
# easy

password = ""
for char in range(0, nr_letter):
    random_char = random.choice(letter)
    password += random_char
for num in range(0, nr_number):
    random_num = random.choice(number)
    password += str(random_num)
for sym in range(0, nr_symbols):
    random_sym = random.choice(symbols)
    password += str(random_sym)
print(password)
print("\n" * 10)
# Hard version

password_list = []
for char in range(0, nr_letter):
    random_char = random.choice(letter)
    password_list.append(random_char)
for num in range(0, nr_number):
    random_num = random.choice(number)
    password_list.append(random_num)
for sym in range(0, nr_symbols):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password : {password}")

lathaEmailid_password = "Latha@Ajay"
