# Dictionaries:
# Name : John Smith
# Email: john@gmail.com
# Phone: 123456789
customer = {
    "name": "John SMith",
    "age": 30,
    "is_verified": True
}
print(customer["name"], customer["age"])

# Dictionaries:
# Phone: 1234
# One Two Three Four
phone = (input("Enter Phone Number"))
digit_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10" : "Ten"
}
output = " "
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)
# Smiley face emojis
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😃",
    ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)