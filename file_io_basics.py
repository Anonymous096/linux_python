# Files IO Basics

'''
"r" = open file for reading - Default 
"w" = open file for writing
"x" = create file if not existed
"a" = add more content to a file
"t" = text mode - Default
"b" = binary mode
"+" = read and write

so for a sample we have already made a .txt file named as "function.txt" from where we will
read and open the file.
'''

f = open("function.txt") # used to read a file but will now return anything but if we made a file pointer(variable) it will return when we print that variable. In this case f is the variable.
# explaination of command is: open("<file_name>", "<mode>"), inverted commas are mandatory, modes are generally:
# r = which is default, rt = default(it will return the content of file in text mode), rb = it will return the content of the file in binary mode.
content = f.read()
print(content)
print(f.readline()) # this will only read a line from the content of the file, starts from the first line.
print(f.readlines()) # This will stores the lines of content of file in a list format


f.close() # This will close the file and it is good to close a file after reading because it will free the resources which had been used to make it open and read and if any other program needs to read this file it can do it easily

# Even to write in the file we have to open the file and then write it.
d = open("file_basics.txt", "w") # Here putting writing mode <"w"> is mandetory and and the if you put the file name which already exists then it would over write it and all the stuff which was written before will be ddeleted, if you put new name of file it will create the file by itself in this case it made <"file_basics.txt">
d.write("This is written from the python code using write function") # It will write the content in the file
d.close() # Close the file whenever not in need