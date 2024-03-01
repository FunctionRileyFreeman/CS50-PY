'''
#ask user name
name = input("whats your name? ")
#print user name might need to fix print end
print("Hello, " + name)
print("Hello,",name)
print("Hello,",name, sep="???")
print("Hello, ", end="")
print("Hello, ", end="???")
print(name)
print("Hello, \Freind\"")
print(f"Hello, {name}")
---------------------------------
#Get rid of space and capitalize
name = input("whats your name? ").strip().title()
first, last = name.split(" ")
print(f"Hello, {first}")
#name = name.capitalize()
#{name}
'''

'''
is a comment
https://docs.python.org/3/
https://www.youtube.com/watch?v=nLRL_NcnK-4&t=11623s
interactive mode ran thro terminal
/n new line
sep' ' seperate by a space
'''