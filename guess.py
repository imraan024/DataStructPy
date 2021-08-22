secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

var = int(input("Enter an integer number: "))

while(var != secret_number):
    print("Ha ha! You're stuck my loop!")
    var = int(input("Enter an integer number: "))

print("Well done, Muggle! You are free now.")
