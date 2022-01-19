## Learning Objectives  
   
- General  
   
## Requirements  
   
- Allowed Editors: `vi`, `vim`, `emacs`  
- All your files will be interpreted on Ubuntu 20.04 LTS  
- All your files should end with a new line  
- A `README.md` file, at the root of the folder of the project, is mandatory  
- All your Bash script files must be executable  
- You are not allowed to use `awk`  
- Your Bash script must pass `Shellcheck` (version `0.7.0`) without any error  
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`  
- The second line of all your Bash scripts should be a comment explaining what the script is doing  
   
## Tasks  
   
- `1-for_best_school`: write a bash script that displays `Best School` 10 times  
	- you must use the `for` loop (`while` and `until` are forbidden)  
- `2-while_best_school`: write a bash script that displays `Best School` 10 times  
	- you must use the `while` loop (`for` and `until` are forbidden)  
- `3-until_best_school`: write a bash script that displays `Best School` 10 times  
	- you must use the `until` loop (`for` and `while` are forbidden)  
- `4-if_9_say_hi`: write a bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` *and then* `Hi` on a new line  
	- you must use the `while` loop (`for` and `until` are forbidden)  
	- you must use the `if` statement  
- `5-4_bad_luck_8_is_your_chance`: write a bash script that loops from 1 to 10 and displays `bad luck` for the 4th loop iteration, and displays `good luck` for the 8th loop iteration, and displays `Best School` for the other iterations  
	- you must use the `while` loop (`for` and `until` are forbidden)  
	- you must use the `if`, `elif`, and `else` statements  
- `6-superstitious_numbers`: write a bash script that displays numbers from 1 to 20 and displays `4` *and then* `bad luck from China` for the 4th loop iteration, and displays `9` *and then* `bad luck from Japan` for the 9th loop iteration, and displays `17` *and then* `bad luck from Italy` for the 17th loop iteration   
	- you must use the `while` loop (`for` and `until` are forbidden)  
	- you must use the `case` statement  
- `7-clock`: write a bash script that displays the time for 12 hours and 59 minutes and display hours from 0 to 12, and display minutes from 1 to 59  
	- you must use the `while` loop (`for` and `until` are forbidden)  
- `8-for_ls`: write a bash script that displays the content of the current directory in a list format, where only part of the name after the first dash is displayed  
	- you must use the `for` loop (`while` and `until` are forbidden)  
	- do not display hidden files  
- `9-to_file_or_not_to_file`: write a bash script that gives you information about the `school` file  
	- you must use `if` and `else` (`case` is forbidden)  
	- your bash script should check if the files exists and print `school file exists` if the file exists and `school file does not exist` if the file does not exist  
	- if the file exists, print: `school file is empty` if the file is empty, `school file is not empty` if the file is not empty, and `school is a regular file` if the file is regular file, (nothing) if the file is not a regular file   
- `10-fizzbuzz`: write a bash script that displays numbers from 1 to 100 in a list format 
	- displays `FizzBuzz` when the number is a multiple of 3 and 5  
	- displays `Fizz` when the number is a multiple of 3  
	- displays `Buzz` when the number is a multiple of 5  
	- otherwise, displays the number
