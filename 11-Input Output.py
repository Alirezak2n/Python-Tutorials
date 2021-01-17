# I/O
my_file=open ('test.txt')
print(my_file.read())  # can read content of file
my_file.seek(0)  # it moves the cursor, terminal can read file only once and we have to bring the cursor back at start23
print(my_file)
print(my_file.readline())  # read only one line
print(my_file.readlines())  # read all lines in a list
my_file.close()  # we say to close file

with open('test.txt') as my_file:  # with this method there is no need to close file
    print(my_file.readlines())  # if we dont have the file it brings error

with open('test.txt',mode='w') as my_file:  # with this mode we can write and delete all which was before
    pass  # if we dont have the file, with mode write, it will make a new file too

with open('test.txt',mode='r+') as my_file:  # with this mode we can read and write
    text = my_file.write('Alireza will win!!!')  # if there is some thing on file, we overwrite it until all characters
    print(text)

with open('test.txt',mode='a') as my_file:  # with this mode we can append at end of file
    text = my_file.write(':)')
    print(text)


