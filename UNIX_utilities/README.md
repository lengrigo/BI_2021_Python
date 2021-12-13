# Description
 
 There are several python programs that immitates basic UNIX utilities.

 Each program immitates one utility and all of them uses python from active enviroment. For input they can take arrguments as well as work in pipelines.
 For example these two lines will give the same output:
 - `cat file | ./wc.py -l`
 - `./wc.py -l file`
---
## Before rumming programs:
 1. Cloone this repo:  
 ``` git clone```  
 After that you will have all the programs in folder called **UNIX utilities**.
 Each utility have the same name as the unix-command and called <utlity-name>.py  
  

 2. Before running program put the next command for each of them to give permissions:  
 ```chmod +x <utility-name>.py```
---
## Utilities description  
###`ls.py`
list directory contents

usage: ls.py [-h] [-a] [directory ...]

positional arguments:  
&emsp;directory

optional arguments:  
&emsp;-h,&emsp;--help&emsp;show this help message and exit  
&emsp;-a,&emsp;--all&emsp;do not ignore entries starting with .

**example:**   
`./ls`- print the content of current directory without entries starts with .
`./ls -a dir1 dir2` - in one output print the content of directories dir1 and dir2 with files that names start with .
###`wc.py`
print newline, word, and byte counts for each file  

usage: wc.py [-h] [-l] [-w] [-c] [file ...]  

positional arguments:  
&emsp;file  

optional arguments:  
&emsp;-h,&emsp;--help&emsp;show this help message and exit  
&emsp;-l,&emsp;--lines&emsp;print the newline counts  
&emsp;-w,&emsp;--words&emsp;print the word counts  
&emsp;-c,&emsp;--bytes&emsp;print the byte counts  

**example:**   
`./wc.py -l -w file.txt` - print the number of lines and words in file.txt

###`sort.py`
sort lines of text files  

usage: sort.py [file ...]  

**example:**  
`ls | ./sort.py` - print current directory content sorted by name
`./sort.py file.txt` - sort and print all limes in file.txt
###`rm.py`
remove files or directories  
usage: rm.py [-h] [-r] [path ...]  
positional arguments:  
&emsp;path

optional arguments:  
&emsp;-h,&emsp;--help&emsp;show this help message and exit  
&emsp;-r,&emsp;-R&emsp;--recursive&emsp;removes directories recursively

**example:**  
`./rm.py file.txt` - remove file.txt  
`./rm.py -r dir1 dir2` - remove directories dir1 and dir2 
###`ln.py`
create a link to *target* with the name *link_name* (without optional arguments makes hard link)  

usage: ln.py [-h] [-s] [target] [link_name]

positional arguments:  
&emsp;target  
&emsp;link  

optional arguments:  
&emsp;-h,&emsp;--help&emsp;show this help message and exit  
&emsp;-s,&emsp;--symbolic&emsp;make symbolic link

**example:**  
`./ln.py -s ../file.txt link_to_file` - creates soft link that is named *link_to_file* to *../file.txt* in current directory 
###`cat.py`
concatenate files and print on the standard output  

usage: cat.py [-h] [file ...]  

positional arguments:  
&emsp;file

optional arguments:  
&emsp;-h,&emsp;--help&emsp;show this help message and exit

**example:**  
`./cat.py file.txt` - print the content of file.txt