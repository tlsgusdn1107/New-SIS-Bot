# New SIS Bot (Updated) #

This is an updated version of yzhan289's selenium bot to register for classes on SIS:
https://github.com/yzhan289/New-SIS-Bot

The old repository is updated to work with chromedriver and extend the bot's applicability to non-Mac users.

### UPDATE: Make sure you have the most updated version of Selenium: ###
```
pip install -U selenium
```

This selenium bot allows you to register for classes on the Johns Hopkins SIS portal right at 7:00 AM, virtually guaranteeing a spot in all of your classes. This will also automatically sign you up for any waitlisted classes.

## General Setup (For both Mac and non-Mac users) ##
First, make sure all of the classes you want to register for are in your cart on SIS.

```
git clone https://github.com/tlsgusdn1107/New-SIS-Bot
cd New-SIS-Bot
pip install -r requirements.txt
brew install chromedriver
```

## Option A: For both Mac and non-Mac Users ##

### Running Instructions ###
Begin running at least a minute before 7:00 AM. The program will wait/keep running until 7:00 AM to register you for your classes. 
```
python bot-automatic.py SIS_UserID SIS_Password
```


## Option B: For Mac Users only ##

SIS uses the naval observatory clock to determine time. Therefore, your system must be synced to this clock to ensure the bot does not click too early or too late. On Mac OS, it is really easy to change your default. 

1. Navigate to System Preferences and click Date and Time. 
2. Click the lock on the bottom left of your window and enter your password. 
3. Change "Apple Americas/U.S. (time.apple.com.)" to "tick.usno.navy.mil"
4. Click the lock again to save your changes. 

![time instructions](https://github.com/nkrishn9/SIS-Bot/blob/master/time_instruct.png "Logo Title Text 1")


### Running Instructions ###
Begin running at least a minute before 7:00 AM. The program will wait/keep running until 7:00 AM to register you for your classes. 
```
python bot-original.py SIS_UserID SIS_Password
```

## Final Words ##

That's all you need to do! The bot will open a new window and sign in to your SIS account. At 7am it will click register to make sure you get the classes you want!
