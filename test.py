mymessage = "hello world"
print(mymessage)
mymessage.capitalize()


lucky_numbers=[4,8,34,6,343,665]
friends=["Gilles","Michi","Eric"]
friends.extend(lucky_numbers)
print(friends)

friends.insert(1, "kelly")
friends.remove('Eric')

print(friends)

def cube(num):
    return pow(num,3)

result = cube(2)
print(result)