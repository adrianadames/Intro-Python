a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[len(a)-2])
# print(a[-2]) #alternate solution

# Output the last three elements in the array: [7, 9, 6]
print(a[slice((len(a)-3),len(a))])
# print(a[3:]) #alternate solution

# Output the two middle elements in the array: [1, 7]
print(a[slice(2,4)])
# print(a[2:3]) #alternate solution

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[slice(1,(len(a)))])
# print(a[1:]) #alternate solution

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[slice(0,(len(a)-1))])
# print(a[:-1]) #alternate solution

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[slice(7,12)])
# print(s[7:12]) #alternate solution