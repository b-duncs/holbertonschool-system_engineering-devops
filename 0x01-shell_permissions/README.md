## Learning Objectives  
   
- Permissions  
- Other Man Pages  
   
## Requirements  
   
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)  
- All your files should end with a new line  
- The first line of your files should be exactly `#!/bin/bash`  
- A `README.md` file, at the root of the folder of the project, describing what each script is doing  
- You are not allowed to use backticks, `&&`, `||`, or `;`  
- Al your files must be executable  
   
## Tasks  
   
- `0-iam_betty`: create a script that switches the current user to the user `betty`  
- `1-who_am_i`: write a script that prints the effective username of the current user  
- `2-groups`: write a script that prints all the groups the current user is part of  
- `3-new_owner`: write a script that changes the owner of the file `hello` to the user `betty`  
- `4-empty`: write a script that creates an empty file called `hello`  
- `5-execute`: write a script that adds execute permission to the owner of the file `hello`  
- `6-multiple_permissions`: write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`  
- `7-everybody`: write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`  
- `8-James_Bond`: write a script that sets the permission to the file `hello` as follows: owner-no permission at all, group-no permission at all, other users-all the permissions  
- `9-John_Doe`: write a script that sets the mode of the file `hello` to this: `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`  
- `10-mirror_permissions`: write a script that sets the mode of the file `hello` the same as `olleh`'s mode  
- `11-directories_permissions`: create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner, and ll other users  
- `12-directory_permissions`: create a script that creates a directory called `my_dir` with permissions 751 in the working directory  
- `13-change_group`: write a script that changes the group owner to `school` for the file `hello`  
