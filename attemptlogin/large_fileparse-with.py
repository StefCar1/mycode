#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            IP = line.split(" ")[-1]
            print(f"Failed log in originated from IP address: {IP}")
        if "-] Authorization failed" in line:
            loginsuccess += 1
print(f"The number of failed log in attempts is {loginfail} and successful log in attempts is { loginsuccess}.")

