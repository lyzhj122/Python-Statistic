import sys
print(sys.executable)
print(sys.version)


mystring = 'this is test'
print(mystring)

mylist = [x**2 for x in range(11)]
print(mylist)

print('this is another test')

print(mystring.upper())

mylist = [1, 2, 3, 4, 5, 6]

for item in mylist:
    print(item)
#pa = input()
x = mystring.count('h')
print(f'h occured {x} times')
print(mystring.split())
mystring.lower()
mystring.join()
mystring.lower()


x = 1
y = 2
print('x is equal to y: %s' % (x == y))
z = 1
print('x is equal to z: %s' % (x == z))
names = ['Donald', 'Jake', 'Phil']
words = ['Random', 'Words', 'Dogs']
if names == words:
    print('Names list is equal to words')
else:
    print("Names list isn't equal to words")
new_names = ['Donald', 'Jake', 'Phil']
print('New names list is equal to names: %s' % (new_names == names))
