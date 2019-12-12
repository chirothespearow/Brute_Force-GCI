from zipfile import ZipFile
name=input('Please enter the name of the zip file (with .zip extension):\n')
passfile=input('Please enter the name of the file containing passwords (including extension):\n')
f=open(passfile,'r')
txt=f.read()
l=txt.split()

with ZipFile(name,'r') as file:
    for i in l:
        try:
            file.extractall(pwd = bytes(i, 'utf-8'))
            print('\nMatch Found:',i,'\n')
            print('Files have been extracted')
            break
        except:
            continue
    else:
        print('\nUnable to crack')
file.close()
f.close()
