# ask user for information
name = input("Write a name: ")

# type of ways to concat string
print("Hello", name)
print("Hello {}".format(name))
print(f"Hello {name}")

adj1 = input("Adjective: ")
adj2= input("Adjective: ")
adj3 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
city = input("City: ")
place = input("Place: ")
language = input("Language: ")
num1 = input("Number: ")
num2 = input("Number: ")

madlib = f"There was one day in {city} where I met {famous_person} on the \
    {place} on my way home after a {adj1} day. We had a {adj3} but {adj2} {verb1} for about \
    {num1} minutes. We were {verb2} until a person says something. After {num2} tries, we \
    could not guess what he ment because he was talking in {language}"

print(madlib)