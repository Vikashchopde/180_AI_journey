x = 20
y = x
y = 10

print(x)
print(y)

print(id(x))
print(id(y))


a = [1,2,3,4]
b = a 

b.append(5)

print(a)
print(b)

print(id(a))
print(id(b))

name = "vikas"
new_name = name

print(name)
print(new_name)

print(id(name))
print(id(new_name))

new_name += " chopde"

print(name)
print(new_name)

print(id(name))
print(id(new_name))

