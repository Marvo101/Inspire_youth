f = open('C:\Users\User\Documents\inspire_Youth_In_STEM\Week-4\test.txt')

print(f.readline())

filename='C:\Users\User\Documents\inspire_Youth_In_STEM\Week-4\test.txt'
try:
    for file in filename:
      with open(filename,'r+w',encoding=None) as f_obj:
        contents =f_obj.read()
        print(contents)
except FileNotFoundError:
    msg="sorry the file" + filename + "doesn't exist."
    print(msg)#



f =open("C:\Users\User\Documents\inspire_Youth_In_STEM\Week-4\test.txt","r+w")

print(filename.readlines())