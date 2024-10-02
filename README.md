Python script to crack md5 or sha1 passwords
"""
Method 1: Provide a input and output the hexadecimal equivalent of the encoded value.

"""
# initializing string
str2hash = "qwerty"
  
# encoding qwerty using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
