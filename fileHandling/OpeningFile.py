
f = open('myData.txt', 'r')
# print(f.read())  # to print entire content of file
# print(f.readline())  # to print first line
# print(f.readline())  # to print second line also prints next line
print(f.readline(50))   # Read up to 50 characters from the current line.

f1 = open('data.txt', 'w')  # to write into a file and will also create a new file if not existing in a package
f1.write("something")   # to write into a new file
f1.write("\n")  # space/newline between
f1.write("Laptop")

f1 = open('data.txt', 'w')  # opening a file again with write option will rewrite the content from scratch
f1.write("something again") # previous content will be replaced by "something again"

f1 = open('data.txt', 'a') # appending a file
f1.write(("now append"))



# f = open('myData.txt', 'r')
# f1 = open('data.txt' 'w')

for data in f:   # for loop to read everything in f basically myData.txt
    f1.write(data)    # it will print everything from myData.txt and print in f1(data.txt)

f2 = open('IMG.JPG', 'rb')  #read binary; if we had jpg file in our package
for i in f:
    print(i)

f2 = open('IMG.JPG', 'rb')
f3 = open('myPic.JPG', 'wb') # write binary (copying from f2 to f3)

for i in f2:  #copy paste from f2 to f3
    f3.write(i)

# FOR AI/ML standard, below is the best way to read file and store it as "text" and then close the file automatically using "with"
#  with block automatically closes the file when the block ends; you do not need to remember f.close()
with open("myData.txt", 'r', encoding="utf-8") as f:  #ython should read the file using UTF-8 text encoding. This helps correctly read normal English text, symbols, many Indian-language characters, etc.
    text = f.read()    # Open the file myData.txt, read all its content, store that content inside variable text, and then automatically close the file.

# Open myData.txt > Call it f temporarily > Read all content from f > Store content in text > Close the file automatically