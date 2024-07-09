str = "happy"

# Reverse the string
reversed_str = str[::-1]

# Iterate over the reversed string
for i in range(1, len(reversed_str) + 1):
    # Get the substring from the end of the string
    substring = reversed_str[:i]
    # Reverse the substring back to the original order
    subs = substring[::-1]
    # Print the substring
    print(subs)

for i in range(1,len(str)+1):
    subs=str[:i]
    print(subs)











































