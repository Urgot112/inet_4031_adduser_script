#!/usr/bin/python3

# INET4031
# Nicholas Le
# Date Created: 09/30/2025
# Date Last Modified: 10/30/2025

import os       # Used to execute system commands like adduser and passwd
import re       # Used to detect comment lines using regular expressions

def main():
    # Prompt the user to choose dry-run mode
    # If the user types 'Y', the script will simulate the process without making any system changes
    # If the user types 'N', the script will run normally and create users on the system
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == "Y"

    # Prompt the user to enter the input filename
    # This allows the script to read user data from a file instead of using stdin
    filename = input("Enter the input filename: ").strip()

    try:
        with open(filename, 'r') as file:
            for line in file:
                match = re.match("^#", line)
                fields = line.strip().split(':')

                # In dry-run mode, print skipped comment lines and formatting errors
                if match:
                    if dry_run:
                        print("==> Skipping line (comment):", line.strip())
                    continue
                if len(fields) != 5:
                    if dry_run:
                        print("==> Error: Line does not have 5 fields:", line.strip())
                    continue

                username = fields[0]
                password = fields[1]
                gecos = "%s %s,,," % (fields[3], fields[2])
                groups = fields[4].split(',')

                print("==> Creating account for %s..." % (username))
                cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

                # In dry-run mode, show the command instead of running it
                # In normal mode, actually run the command to create the user
                if dry_run:
                    print("[Dry-run] Would run:", cmd)
                else:
                    os.system(cmd)

                print("==> Setting the password for %s..." % (username))
                cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

                # In dry-run mode, show the password command
                if dry_run:
                    print("[Dry-run] Would run:", cmd)
                else:
                    os.system(cmd)

                for group in groups:
                    if group != '-':
                        print("==> Assigning %s to the %s group..." % (username, group))
                        cmd = "/usr/sbin/adduser %s %s" % (username, group)

                        # In dry-run mode, show the group assignment command
                        if dry_run:
                            print("[Dry-run] Would run:", cmd)
                        else:
                            os.system(cmd)

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")

# This ensures the script only runs when executed directly
if __name__ == '__main__':
    main()
