# Capitalize the first character of the string
First_name = "mary"
Last_name = "malumyan"
print(First_name.capitalize(), Last_name.capitalize())
# Center the string with the given width
print(First_name.center(15))
# Count how many times the specified character happens in the string
print(Last_name.count('a'))
# Count how many times the specified character happens in the string in the given range
print(Last_name.count('a',3))
# Encode converts the string into encoded version
a = "This is my strիng!"
print(a.encode('ascii', 'ignore'))
b = a.encode('ascii', 'ignore')
# Decoding works opposite the encoding
print(b.decode('ascii', 'ignore'))
# Replaces the specified character
print(a.replace('ի', 'i'))
#Checks if the string ends with the specified character
print(a.endswith('g'))
print(a.endswith('!'))
# Converts the string into uppercase
print(a.upper())
