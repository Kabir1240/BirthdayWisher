# Automated Birthday Wisher (AWB)  
-> Download the rar file and run the exe.  
-> When you run this program, it will automatically send emails to everyone who has birthdays on that day.  
-> Add birthdays to data/birthdays.csv  
-> When you run for the first time, you'll be asked to create an account. Store your name and email here, for the password, do not use your regular password. Go to your google accounts, set up 2FA, open App Passwords and generate a password from there, use that.  
-> You will not be asked to do this every time. In the future, you can edit this directly from the data/user_account.json. You can delete it and run the program to enter it again via GUI.  
-> You can add more templates, but you would have to modify the source code. Just increase NUMBER_OF_TEMPLATES to the new amount. You can also edit existing templates.  

  # Bugs  
-> The only problem is, you can only use this program if your email is an @gmail.com account (receiver email doesn't matter). Because it connects to the gmail server by default. Sadly, you can only fix this by modifying the source code.  
-> Sometimes your ISP may block the connection. You might have to try changing the port numbers in the source code. You could also try using a VPN, hotspot or another ISP.  
