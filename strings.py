x = "hello world"
y = x[0:2]
print(y)

print(bool(0))
x = "hello world"
if x.islower():
    print("The string is in lowercase.")
if x.isupper():
    print("The string is in uppercase.")
if "world" in x:
    print("The string contains 'world'.")
x = x.upper()
print("\t"+x)
y = x.replace("WORLD", "Python")
print("\t \t" + y)
print("\t \t \t" + x + " " + y)
count = 1
sentence = input("Enter a sentence: ")
if sentence.endswith(".") or sentence.endswith("!"):
    print("The sentence ends with a period or exclamation mark.")
    count = count + 1
result = sentence.find("hey")
if result != -1:
    print(f"The word 'hey' is found at index {result}.")
if sentence.startswith("Hello") or sentence.startswith("hello"):
    print("The sentence starts with 'Hello'.")
    count = count + 1
if sentence.istitle():
    print("The sentence is in title case.")
    count = count + 1
number_of_words = len(sentence.split())
print(f"The sentence contains {number_of_words} words.")