File i/o : file handling output


File Modes : 

  'r'	Read mode (default). Opens for reading only; raises error if the file doesn't exist.
  'w'	Write mode. Opens for writing, overwriting the file if it exists, or creating a new one if it doesn't.
  'a'	Append mode. Opens for writing, adding new data to the end of the file without deleting existing content.
  'b'	Binary mode. Used with other modes (e.g., 'rb', 'wb') for non-text files like images or executables.
  '+'	Update mode. Opens a file for both reading and writing (e.g., 'r+', 'w+').
  


# sorted keyword for sorting

# ###################################
Method 1 ( Most basic format )



names=[]
n=int(input('Define total No. :'))
for _ in range(n):
    names.append(input('Candidate Name : '))

for name in sorted(names):
    print(f'hello {name}\n')



# ######################################
Method 2



names=[]
with open('names.txt', 'r') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f'hello {name}')



# ==============================================
Method 3 (Optimized)



with open('names.txt','r') as file:
    for line in sorted(file):
        print(f'hello {line.rstrip()}')



# ############################################

Method 3 : Reverse sorting, printing file name in Decesding order sorted(iterable, key=None, reverse=False)


with open('names.txt','r') as file:
    for line in sorted(file, reverse=True):
        print(f'hello {line.rstrip()}')



