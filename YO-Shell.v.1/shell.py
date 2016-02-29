"""
@Program Name: Yo-Shell V1 Starter Code
@Author:Tejaswi Prakhya
@Description:
    This code is a barebones snippet to get your shell up and running. It provides the following classes 
          historyManager - manages a history of commands
          parserManager - handles parsing of commands into command , arguments, flags
          commandManager - gets commands parsed and then runs appropriate functions for command
          driver - drives the entire shell
"""
import os
import sys
import subprocess
import shutil
import time

"""
@Name: historyManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@functions:
    push_command - add command to history
    get_commands - get all commands from history
    number_commands - get number of commands in history
"""
class historyManager(object):
    def __init__(self):
        self.command_history = []
    """
    @Name: push_command
    @Description:
        Add command to history
    @Params:
        cmd (string) - Command added to history
    @Returns: None
    """
    def push_command(self,cmd):
        self.command_history.append(cmd)
    """
    @Name: get_commands
    @Description:
        get all commands from history
    @Params: None
    @Returns: None
    """
    def get_command(self):
        return self.command_history
    """
    @Name: number_commands
    @Description:
        get number of commands in history
    @Params: None
    @Returns: 
        (int) - number of commands
    """
    def number_commands(self):
        return len(self.command_history)
"""
@Name: parserManager
@Description:
    Handles parsing of commands into command , arguments, flags.
@functions:
    parse - does actual parsing of command
"""
class parserManager(object):
    def __init__(self):
            self.parts = []
    """
    @Name: parse
    @Description:
        Parses command into a list (right now). 
    @Params: 
        cmd (string) - The command to be parsed
    @Returns: 
        (int) - number of commands
    """
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
"""
@Name: commandManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@functions:
    run_command - Runs a parsed command
    ls - Directory_listing
    cat - File dump
"""
class commandManager(parserManager):
    def __init__(self):
        self.command = None
    """
    @Name: run_command
    @Description:
        Runs a parsed command
    @Params: 
        cmd (string) - The command
    @Returns: 
        (list) - With the command parts (It shouldn't return the list, it should RUN the appropriate command from this function.
    """
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command
    """
    @Name: ls
    @Description:
        Does a directory listing
    @Params: 
        dir (string) - The directory to be listed
    @Returns: None
    """
    def ls(dir):
        print('$ ls')
        print('File listing')
        print('-----------------')
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname,subdirname))

        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))

        print('-----------------')
    """
    @Name: ls_f
    @Description:
        Used this function to store the file attributes in a list, to access in other defined functions for ease of access.
    @Params: 
        dir (string) - The directory to be listed
    @Returns: f_files(list)
    """   
    def ls_f(dir):
        
        f_files = []
        
        for dirname, dirnames, filenames in os.walk('.'):
            for subdirname in dirnames:
                print(os.path.join(dirname,subdirname))

        for filename in filenames:
            #A list created to store the file attributes 
            files = []
            path = os.path.join(dirname, filename)
            #Appends filename,size of file,permission levels,acess time of file,modified time of file and created time of file to the 'files' list respectively.
            files.append(os.path.join(dirname, filename))
            files.append(os.path.getsize(path))
            files.append(oct(os.stat(path).st_mode)[4:])
            files.append(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(os.path.getatime(path))))
            files.append(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(os.path.getmtime(path))))
            files.append(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(os.path.getctime(path))))
            #Appends the list(which stores the file attributes) to the 'f_files' list and returns it.
            f_files.append(files)
            
        return f_files
    """
    @Name: ls_l
    @Description:
        Displays the long listing of files in the directory.
    @Params: 
        f(list)
    @Returns: None
    """ 
    def ls_l(self,f):
        print('$ ls -l')
        print('File Name\t\t   Size\t\t       Permissions\t\t  Accessed\t\t    Modified\t\t   Crteate')
        print('----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------')
        for file in f:
            for x in file:
                print(x,end="\t\t ")
            print()
    """
    @Name: ls_s
    @Description:
        Displays the long listing of files in the directory based on the file size in ascending order.
    @Params: 
        f(list)
    @Returns: None
    """ 
    def ls_s(self,f):
        print('$ ls -s')
        print('File Name\t\t   Size\t\t       Permissions\t\t  Accessed\t\t    Modified\t\t   Crteate')
        print('----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------')
        #Invoked the pre-defined function Sorted(list name(f),key=lambda,index of coloumn to be sorted)
        f=sorted(f,key=lambda l:l[1])
        for file in f:
            for x in file:
                print(x, end="\t\t ")
            print()
    """
    @Name: ls_a
    @Description:
        Displays the long listing of files in the directory based on the last access time of files.
    @Params: 
        f(list)
    @Returns: None
    """         
    def ls_a(self,f):
        print('$ ls -a')
        print('File Name\t\t   Size\t\t       Permissions\t\t  Accessed\t\t    Modified\t\t   Crteate')
        print('----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------')
        f=sorted(f,key=lambda l:l[3])
        for file in f:
            for x in file:
                print(x,end="\t\t ")
            print()
    """
    @Name: ls_m
    @Description:
        Displays the long listing of files in the directory based on the last modified time of files.
    @Params: 
        f(list)
    @Returns: None
    """ 
    def ls_m(self,f):
        print('$ ls -m')
        print('File Name\t\t   Size\t\t       Permissions\t\t  Accessed\t\t    Modified\t\t   Crteate')
        print('----------\t\t----------\t\t----------\t\t----------\t\t----------\t\t----------')
        f=sorted(f,key=lambda l:l[4])
        for file in f:
            for x in file:
                print(x,end="\t\t ")
            print()
    """
    @Name: ls_c
    @Description:
        Displays the long listing of files in the directory based on the creation date of files.
    @Params: 
        f(list)
    @Returns: None
    """ 
    def ls_c(self,f):
        print('$ ls -')
        print('File Name\t\t   Size\t       Permissions\t  Accessed\t    Modified\t   Crteate')
        print('----------\t\t----------\t----------\t----------\t----------\t----------')
        f=sorted(f,key=lambda l:l[5])
        for file in f:
            for x in file:
                print(x,end="      ")
            print()        
              
    """
    @Name: cat
    @Description:
        Dumps a file
    @Params: 
        file (string) - The file to be dumped
    @Returns: None
    """   
    def cat(self,file):
        f = open(file,'r')
        print(f)
        print('======================================')
        print(f.read())
        f.close()
        print('======================================')
    """
    @Name: chmod
    @Description:
        Changes the permission level(User, Group, Others) of files
    @Params: 
        path(String) - filename for which the permission level must be modified.
        mode(int) - Octal number to set permission for the user given file (Ex : 777)
    @Returns: None
    """ 
    def chmod(self,path,mode):
        os.chmod( path,mode )   #chmod() built in function is used to change the permission levels of a file
    """
    @Name: cd
    @Description:
        Changes to the directory which is given by the user.
    @Params: 
        path(String) - The required path to be parsed.
    @Returns: None
    """ 
    def cd(self,path):
        os.chdir(path)          #chdir() built-in function is used to change one directory from another directory
        pwd=os.getcwd()         #getcwd() function is used to know the current working directory
        print(pwd)
    """
    @Name: cd_b
    @Description:
        It moves to previous directory(one level upper) from currrent directory.
    @Params: 
        None
    @Returns: None
    """ 
    def cd_b(self):
        os.chdir('..')
        pwd = os.getcwd()
        print(pwd)
    """
    @Name: cd_h
    @Description:
        It parses to home directory from current directory.
    @Params: 
        None
    @Returns: None
    """ 
    def cd_h(self):
        os.chdir('/home')
        pwd = os.getcwd()       
        print (pwd)
    """
    @Name: cp
    @Description:
        Copies  source file to destination file.
    @Params: 
        o_f(String) - Path of source file.
        n_f(String) - Path of destination file.
    @Returns: None
    """ 
    def cp(self,o_f,n_f):
        #Built-in function to copy souce to destination. Imported "shutil" library to use its built-in functions. 
        shutil.copy(o_f,n_f)
        print('Copy Successful.')
    """
    @Name: mv
    @Description:
        It cuts the source file and pastes in destination file.
    @Params: 
        old(String) - Path of source file that to be renamed/cut.
        new (String) - Path of destination file where the source file gets pasted.
    @Returns: None
    """ 
    def mv(self , old , new):
        shutil.move(old,new)
        print('Move Successful.')
    """
    @Name: rm
    @Description:
        Removes the file in the directory which is passed as an argument.
    @Params: 
        f_name(string) - Path of file to be removed that is given as argument.
    @Returns: None
    """ 
    def rm(self , f_name):
        #Removes the file which is passed as parameter.
        os.remove(f_name)
        print('File Removed Sucessfully.')
    """
    @Name: wc
    @Description:
        Gives the total number of words in a file that is given as input.
    @Params: 
        name(string) - Path of file for which number of words to be counted.
    @Returns: None
    """
    def wc(self , name):
        f=open(name,'r')
        wordcount=0
        for lines in f:
            #Splitting the words in a file and storing the sum in wordcount
            f1=lines.split()
            wordcount=wordcount+len(f1)
        f.close()
        print ('Number of words : ', str(wordcount))
    """
    @Name: wc_l
    @Description:
        Gives the total number of lines in a file that is given as input.
    @Params: 
        file(string) - Path of file for which number of lines to be counted.
    @Returns: None
    """
    def wc_l(self , file):
        #Opening the file for which the number of lines to be counted.
        with open(file) as f:
            print ('Number of lines : ',sum(1 for _ in f))
        
    """
    @Name: history
    @Description:
        Gives the history of commands that has been executed in the shell of that particular user from day one.
    @Params: 
        None
    @Returns: None
    """
    def history(self):
        #Opening the default file where the history will be stored.
        for history in open('/home/prakhyat/.bash_history'):
            print(history, end='')
"""
@Name: driver
@Description:
    Drives the entire shell environment
@functions:
    run_shell - Loop that drives the shell environment
"""                
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
    """
    @Name: runShell
    @Description:
        Loop that drives the shell environment
    @Params: None
    @Returns: None
    """ 
    def runShell(self):
        number_commands = 0
        i = 0
        while True:
            self.input = input("parser-$")
            self.history.push_command(self.input)
            parts = self.commands.run_command(self.input)
            for x in parts:
                #checking for 'ls' command in command line arguments if given by the user
                if x == 'ls':
                    i = parts.index('ls')
                    c = len(parts)
                    i+=1
                    if i >= c:
                        self.commands.ls()
                    else:
                        f = parts[i]
                        if f == '-l':
                            file = self.commands.ls_f()
                            self.commands.ls_l(file)
                        else:
                            if f == '-s':
                                file = self.commands.ls_f()
                                self.commands.ls_s(file)
                            else:
                                if f == '-m':
                                    file = self.commands.ls_f()
                                    self.commands.ls_m(file)
                                else:
                                    if f == '-a':
                                        file = self.commands.ls_f()
                                        self.commands.ls_a(file)
                                    else:
                                        if f == '-c':
                                            file = self.commands.ls_f()
                                            self.commands.ls_c(file)
                                        else:
                                            self.commands.ls()
                else:
                    if x == 'cat':                                                             #checking for 'cat' command in command line arguments if given by the user
                        i = parts.index('cat')
                        i+=1
                        var = parts[i]
                        self.commands.cat(var)
                    else:
                        if x == 'chmod':                                                       #checking for 'chmod' command in command line arguments if given by the user
                            i = parts.index('chmod')
                            i+=1
                            per  = parts[i]
                            per = int(per,8)                                                   #converting sting to octal format of integer 
                            i+=1
                            file= parts[i]
                            self.commands.chmod(file ,per)
                        else:
                            if x == 'cd':                                                      #checking for 'cd' command in command line arguments if given by the user                 
                                i=parts.index('cd')
                                i+=1
                                dire = parts[i]
                                self.commands.cd(dire)
                            else:
                                if x == 'cp':                                                  #checking for 'cp' command in command line arguments if given by the user
                                    i = parts.index('cp')
                                    i+=1
                                    old = parts[i]
                                    i+=1
                                    new = parts[i]
                                    self.commands.cp(old,new)
                                else:
                                    if x == 'mv':                                              #checking for 'mv' command in command line arguments if given by the user
                                        i = parts.index('mv')
                                        i+=1
                                        o_file = parts[i]
                                        i+=1
                                        n_file = parts[i]
                                        self.commands.mv(o_file , n_file )
                                    else:
                                        if x == 'rm':                                          #checking for 'rm' command in command line arguments if given by the user
                                            i = parts.index('rm')
                                            i+=1
                                            name = parts[i]
                                            self.commands.rm(name)
                                        else:
                                            if x == 'wc':                                      #checking for 'wc' command in command line arguments if given by the user
                                                i = parts.index('wc')
                                                i+=1
                                                file = parts[i]
                                                if file != '-l':
                                                    self.commands.wc(file)
                                                else:
                                                    i+=1
                                                    fname = parts[i]
                                                    self.commands.wc_l(fname)
                                            else:
                                                if x == 'history':                             #checking for 'history' command in command line arguments if given by the user
                                                    self.commands.history()
                                                else:
                                                    if x == 'cd..':                            #checking for 'cd..' command in command line arguments if given by the user
                                                        self.commands.cd_b()
                                                    else:
                                                        if x == 'cd~':                         #checking for 'cd~' command in command line arguments if given by the user
                                                            self.commands.cd_h()
                                                        else:
                                                            print(x + "Command Not Found")
            print(parts)

if __name__=="__main__":
    d = driver()
    d.runShell()    

