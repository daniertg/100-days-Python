# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
name = name.lower()

characters = "true"
counts_1 = sum(name.count(char) for char in characters)

characters = "love"
counts_2 = sum(name.count(char) for char in characters)

result = str(counts_1) + str(counts_2)
final = int(result)


if (final < 10) or (final > 90):
    print(f"Your score is {final}, you go together like coke and mentos.")
elif (final >= 40) and (final <= 50):
    print(f"Your score is {final}, you are alright together.")
else :
    print(f"Your score is {final}.")
