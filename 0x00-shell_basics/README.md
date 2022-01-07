## Learning Objectives  

- General  
- What is the Shell  
- Navigation  
- Looking Around  
- Manipulating Files  
- Working with Commands  
- Reading Man Pages  
- Keyboard Shortcuts for Bash  
- LTS  

---  

## Requirements  

- Allowed editors: `vi`, `vim`, `emacs`  
- All your scripts will be tested on Ubuntu 20.04 LTS  
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)  
- All your files should end with a new line  
- The first line of all your files should be exactly `#!bin/bash`  
- A `README.md` file at the root of the repo, containing a description of the repository  
- A `README.md` file at the root of the folder of *this* project, describing what each script is doing  
- You are not allowed to use backticks, `&&`, `||`, or `;`  
- All your scripts must be executable, to make your file executable, use the `chmod` command: `chmod u+x file`    
  
---  
  
## Tasks  

- `0-current_working_directory`: write a script that prints the absolute path name of the current working directory  
- `1-listit`: display the contents list of the current directory  
- `2-bring_me_home`: write a script that changes the working directory to the user's home directory  
- `3-listfiles`: display current directory contents in long format  
- `4-listmorefiles`: display current directory contents, including hidden files (starting with `.`)  
- `5-listfilesdigitonly`: display current directory contents  
- `6-firstdirectory`: create a script that creates a directory named `my_first_directory` in the `/tmp/` directory  
- `7-movethatfile`: move the file `betty` from `/tmp/` to `/tmp/my_first_directory`  
- `8-firstdelete`: delete the file `betty`  
- `9-firstdirdeletion`: delete the directory `my_first_directory` that is in the `/tmp` directory  
- `10-back`: write a script that changes the working directory to the previous one  
- `11-lists`: write a script that lists all files in the current directory and the parent of the working directory and the `/boot` directory  
- `12-file_type`: write a script that prints the type of the file named `iamafile`  
- `13-symbolic_link`: create a symbolic link to `/bin/ls` named `_ls_`  
- `14-copy_html`: create a script that copies all the HTML files from the current working directory to the parent of the working directory  
