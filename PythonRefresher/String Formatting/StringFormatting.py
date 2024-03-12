"""
String Formatting
"""


first_name = "Eric"
print("Hi " + first_name) # concatenation example

print(f"Hi {first_name}") # f formatting is like interpolation

sentence = "Hi {} {}" # sentence formatting
last_name = "Roby"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")





