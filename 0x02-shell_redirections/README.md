## Learning Objectives  
   
- Shell, I/O Redirection  
- Special Characters  
- Other Man Pages  
   
## Requirements  
   
- Allowed editors: `vi`, `vim`, `emacs`  
- All your scripts will be tested on Ubuntu 20.04 LTS  
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)  
- All your files should end with a new line  
- The first line of all your files should be exactly `#!/bin/bash`  
- A `README.md` file, at the root of the folder of the project, describing what each script is doing  
- You are not allowed to use backticks, `&&`, `||`, `;`  
- All your files must be executable  
- You are not allowed to use `sed` or `awk`  
   
## Tasks  
   
- `0-hello_world`: write a script that prints "Hello, World", followed by a new line to the standard output  
- `1-confused_smiley`: write a script that displays a confused smiley "(Ôo)"  
- `2-hellofile`: display the content of the `/etc/passwd` file  
- `3-twofiles`: display the content of `/etc/passwd` and `/etc/hosts`   
- `4-lastlines`: display the last 10 lines of `/etc/passwd`  
- `5-firstlines`: display the first 10 lines of `/etc/passwd`  
- `6-third_line`: write a script that displays the third line of the file `iacta`  
- `7-file`: write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line  
- `8-cwd_state`: write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`  
- `9-duplicate_last_line`: write a script that duplicates the last line of the file `iacta`  
- `10-no_more_js`: write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders  
- `11-directories`: write a script that counts the number of directories and sub-directories in the current directory  
- `12-newest_files`: create a script that displays the 10 newest files in the current directory  
- `13-unique`: create a script that takes a list of words as input and prints only words that appear exactly once  
- `14-findthatword`: display lines containing the pattern "root" from the file `/etc/passwd`  
- `15-countthatword`: display the number of lines that contain the pattern "bin" in the file `/etc/passwd`  
- `16-whatsnext`: display lines containing the pattern "root" and 3 lines after them in the file `/etc/passwd`  
- `17-hidethisword`: display all the lines in the file `/etc/passwd` that do not contain the pattern "bin"  
- `18-letteronly`: display the lines of the file `/etc/shh/sshd_config` starting with a letter  
- `19-AZ`: replace all characters `A` and `c` from input to `Z` and `e` respectively  
- `20-hiago`: create a script that removes all letters `c` and `C` from input  
- `21-reverse`: write a script that reverse its input  
- `22-users_and_homes`: write a script that displays all users and their home directories, sorted by users  
