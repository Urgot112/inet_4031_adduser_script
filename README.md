# inet_4031_adduser_script

Program Description:
This Python script helps automate the process of adding users to a Linux system. Instead of manually typing out commands like adduser, passwd, and assigning users to groups one by one, this script reads from a formatted input file and does all of that for you. It uses the same system commands you'd normally run in the terminal, but wraps them in Python so everything happens in one go. This saves time and makes it easier to manage multiple accounts.

Program User Operation:
The script reads each line from an input file and uses that information to create user accounts, set their passwords, and add them to groups. You’ll need to run the script with root privileges to make changes to the system. The comments in the code explain how each part works, but here’s what you need to know to get started.

Input File Format:
Each line in the input file should include five parts separated by colons: the username, password, last name, first name, and a list of groups. If you want to skip a line, just start it with a #. If the user shouldn’t be added to any groups, use a dash (-) in the group field.

Command Execution:
Before running the script, make sure it is executable:
chmod +x create-user.py
Then run it like this:
sudo ./create-user.py < create-user.input
After this command it will read the input file and create the users listed in it. 

Dry Run:
Before making real changes I did a dry run. This lets me test the script without actually adding users. In dry-run mode, the script prints out the commands it would run, skips invalid lines, and shows you any formatting issues. To do a dry run I commented out the os.system(cmd) lines in the script and run:
./create-user.py < create-user.input
Then you will see the output showing which users would be created and which lines were skipped.
