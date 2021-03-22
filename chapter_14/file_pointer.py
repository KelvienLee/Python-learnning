file = open('zen.txt', 'w+')

print(file.tell())
file.write('hello world.')
file.seek(6, 0)
print(file.tell())
content = file.read()
print(content)

file.close()
