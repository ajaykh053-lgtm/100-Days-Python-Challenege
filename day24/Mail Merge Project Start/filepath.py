#File Path

# / root 
# /work
#/work/report.doc
#/work/project
#/wprk/priect/talk.ppt

# sreach in current file

#./talk.ppt
# ..//report.doc



# # opening and closing the file 
# file = open("example.txt")
# content= file.read()
# print(content)
# file.close()


# #Opening the file but the closing the file is automatic
# with open("example.txt") as file :
#     content=file.read()
#     print(content)

#writing into the file
with open("newfile.txt",mode="w") as file :
    file.write("New text .")

#appending the text to the file 
with open("newfile.txt",mode="a") as file :
    file.write("\nNew text .")