#!
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('data.txt', 'r')
text = f.read()
print(text)

words = text.split()
print(words)
