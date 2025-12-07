 File i/o : File Handling in Python

 File I/O (Input/Output) in Python involves reading data from and writing data to files on your system, allowing data to persist after a program finishes running. The primary built-in function for file handling is open(). 

# ###########################
 The open() Function :
Before any operation, a file must be opened using the open() function, which returns a file object (or "handle"). 

        >>>>>>>>>>>  file_object = open(filename, mode, encoding="utf-8")

# filename: A string representing the path to the file.
# mode: A string indicating the purpose (read, write, etc.).
# encoding: Recommended to specify, usually "utf-8", for handling text files consistently across platforms. 


# ######################
File Modes : Common modes are specified as the second argument to open(). 
Mode 	Description
'r'	Read mode (default). Opens for reading only; raises error if the file doesn't exist.
'w'	Write mode. Opens for writing, overwriting the file if it exists, or creating a new one if it doesn't.
'a'	Append mode. Opens for writing, adding new data to the end of the file without deleting existing content.
'b'	Binary mode. Used with other modes (e.g., 'rb', 'wb') for non-text files like images or executables.
'+'	Update mode. Opens a file for both reading and writing (e.g., 'r+', 'w+').

# ##############################################3

Best Practice: The with Statement

 # #########################################################
Method 1 (Optimal)
 
names=[]
names=input('Candidate Name : ')
# with : with keyword open and closes file automatically
with open('names.txt', 'a') as file:
    file.write(f'{names}\n')



# ==================================================
Method 2 
 
names=input("Candidate Name : ")
file=open('name.txt', 'a')
file.write(f'{names}\n')
file.close()



