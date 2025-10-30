#!/usr/bin/python3

# INET4031
# Nicholas Le
# Data Created: 09/30/2025
# Date Last Modified: 09/30/2025

import os       #Used to execute system commands like adduser and passwd
import re       #Used to detect comment lines using regular expressions
import sys      #Used to read input from stdin like input file


def main():
    for line in sys.stdin:

         # Check if the line starts with '#' — used to skip comment lines in the input file
        match = re.match("^#",line)

        # Remove trailing newline and split the line into fields using ':' as delimiter
        fields = line.strip().split(':')

        # Skip the line if it's a comment or doesn't have exactly 5 fields (invalid format)
        if match or len(fields) != 5:
            continue

        # Extract user information: username, password, and GECOS field for full name
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the group field into a list of groups (comma-separated)
        groups = fields[4].split(',')

        # Print message indicating user account creation
        print("==> Creating account for %s..." % (username))
        # Build command to create user with disabled password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd
        os.system(cmd)

        # Print message indicating password setup
        print("==> Setting the password for %s..." % (username))
        # Build command to set the user's password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        
        #print cmd
        os.system(cmd)

        for group in groups:
            # Loop through each group and assign the user if the group is not '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
