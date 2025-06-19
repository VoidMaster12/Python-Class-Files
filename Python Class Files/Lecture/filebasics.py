#filebasics.py

# A FILE is a named, linear array of bytes on a disk.

# A file's NAME is actually important. It's the name you, the user, know the
#file by. You can recognize it, search for it, find it, and use the file with
#it. The computer will also have internal numerica identifies for the file,
#but the computer has to be able to translate between those and the name you
#know for anything to work.

#We think of a file as being catalogued in a DIRECTORY or a FOLDER.
#A reference to the original "file" metaphor. Physical paper files pre-date
#computer "files". 

# A file is a sequence of chararacters, like a list in Python, that come one
# after the other. "Text" files like this are readable by humans once rendered
# character-by-character into their corresponding letters, numbers, punctuation.
# Other files are purer computer code.
# These BINARY files aren't intelligible to us, but they are to the computer.
# They're made purely of ones and zeroes, and there are many kinds of them.

# A file is a LINEAR array. It has a first byte, second byte, next byte,
# and so on until the last byte. Every byte has a specific number, like an index
# in a Python list.

# A file lives on a disk. Originally we called disks that because they were
# actually round.

# For our purposes, a disk is a DEVICE THAT HOLDS FILES. We say that files
# are AT REST on disks: unlike the information in the primary memory, when you
# turn the computer off, files persist. This is why we use the term SAVING: we
# are "saving" the information from being erased.

# To start working with a file, we OPEN it. 

f = open("ourfile.txt", "w")

# Here, we're opening ourfile.txt for writing, shown by the w. We want to
# produce output TO that file.

# When you think of input and output, think of the "core" of the computer as the
# center of the universe. INPUT is read FROM FILES, the user, etc., into the
# computer for processing. OUTPUT is written TO files, the user, etc. for 
# reporting.

# By default, all files in Python are text files. We don't reach binary files in 
# this class.

f.write("Hello, world!")

# There we write a string to the file. Now that we're done working with it, we
# have to CLOSE it.

f.close()

# If you don't close the file, whatever you write may not be properly finished 
# writing, or "finalized", when the program ends. You must ALWAYS close files.

# YOU WILL LOSE POINTS IF YOU DON'T CLOSE THE FILES.

# Notice that if you run the program several times, we only get one "Hello,
# World!" in the file.

# f=open.("ourfile.txt","w")

# "w" is for WRITING. Mode w creates a new file with the given filename, and
# prepares it to be written to. Any existing file with that name will be
# "clobbered" - its contents will be deleted, and will start over as an empty
# file.

# "a" is for APPENDING - tacking on to the end. Mode "a" creates a new file
# only if the file doesn't already exist; otherwise it prepares the file to
# have new information "appended" to it.

# "r" is for READING - inputting information FROM a file. If the file exists,
# mode "r" prepares it to be read by our program. If the files doesn't exist,
# mode "r" causes an error. It can't create new files.

f=open("ourfile2.txt", "w")
f.write("Hello, World!\n")

f=open("ourfile2.txt", "a")
f.write("Hello again, World!\n")
f.close()

# Write doesn't add a new line when you write something else like print. You
# need to put \n for a new line.

# You can write lists to a file, but you still need the \n.

l=["Hello, World!\n", "Here are some lines...\n", "...to write.\n"]
f=open("ourfile3.txt","w")
f.writelines(l)
f.close()

# You can read entire files as well

f = open("ourfile3.txt","r")
s = f.read()
f.close()

# s now contains the entire contents of the file f, newlines and all.

print(s)

# More often, we want to work with a file line-by-line. There are two good ways
# to do this. One is to read the whole file into a list:

f = open("ourfile3.txt","r")
l = f.readlines()
f.close()

# l now contains the contents of f, line by line.

for s in l:
    print(s)

# The newlines are still there. We can get rid of them as we process...

for s in l:
    s = s.strip("\r\n") #strip all DOS and UNIX newline characters
    print(s)

# ...or in memory.

for i in range(len(l)):
    l[i] = l[i].strip("\r\n")

for s in l:
    print(s)

# The second and final way to read input is to simply iterate over the FILE
# ITSELF. If you're going strictly line by line, then in Python, this is a
# very fast and efficient way of reading a file.

f = open("ourfile3.txt", "r")

for line in f:
    line = line.strip("\r\n")
    print(line)
f.close()

