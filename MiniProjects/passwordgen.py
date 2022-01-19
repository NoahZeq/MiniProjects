import random

upper = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
lower = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "z"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

all = upper + lower + digits
length = 12

random_pass = "".join(random.sample(all, length))

print(f"Password generated: {random_pass}")