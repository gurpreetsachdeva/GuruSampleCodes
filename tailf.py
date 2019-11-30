
import os
find_str = "ERROR"
error = False
print(os.getcwd())
# Open file with 'b' to specify binary mode
with open('my_log.txt', 'rb') as file:
    file.seek(-10*10, os.SEEK_END)  # Note minus sign
    line=file.readline()
    while(line):
        print(line)
        line=file.readline()




