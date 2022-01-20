## Learning Objectives  
   
- General  
   
## Requirements  
   
- Allowed editors: `vi`, `vim`, `emacs`  
- All your files will be interpreted on Ubuntu 20.04 LTS  
- All your files should end with a new line  
- A `README.md` file, at the root of the folder of the project, is mandatory  
- All your Bash script files must be executable  
- Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error  
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`  
- The second line of all your Bash scripts should be a comment explaining what is the script doing  
   
## Tasks  
   
- `0-what-is-my-pid`: write a bash script that displays its own PID  
- `1-list_your_processes`: write a bash script that displays a list of currently running processes  
- `2-show_your_bash_pid`: using your previous exercise command, write a bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your bash process  
- `3-show_your_bash_pid_made_easy`: write a bash script that displays the PID, along with the process name, of processes whose names contain the word `bash`  
- `4-to_infinity_and_beyond`: write a bash script that displays `To infinity and beyond` indefinitely  
- `5-dont_stop_me_now`: write a bash script that stops `4-to_infinity_and_beyond` process  
- `6-stop_me_if_you_can`: write a bash script that stops `4-to_infinity_and_beyond` process  
- `7-highlander`: write a bash script that displays `To infinity and beyond` indefinitely, with a `sleep 2` in between each iteration, and `I am invincible!!!` when receiving a `SIGTERM` signal  
- `8-beheaded_process`: write a bash script that kills the process `7-highlander`
