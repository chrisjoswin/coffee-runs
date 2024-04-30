# coffee-runs
The Coffee Payment Decider is a command-line application built using Python and to help coworkers at the office decide who should pay for coffee each day. It allows users to create and manage a list of group members, their favorite coffee orders, and tracks who is responsible for paying for the coffee each day.

## Installation

## Running the Application

## Setting Up AWS
If you would like to retrieve the menu from the AWS S3 bucket you will need to add the ```AWS_ACCESS_KEY_ID``` and ```AWS_SECRET_ACCESS_KEY``` to your ```~/.bashrc``` file
1. Open Terminal on your Mac (command + spacebar). Type Terminal and click on application
2. Type ```vi ~/.bashrc``` and then hit return(enter)
3. Use the arrow keys to navigate to the end of the last line in the file
4. type `i` for insert and move cursor to the right and then return(enter) to create a new line
5. paste this for the new line, be sure to replace YOUR_ACCESS_KEY_ID and YOUR_SECRET_ACCESS_KEY with aws credentials
```
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
```
6. then hit ```esc``` key and then type ```:wq``` to exit out of insert mode and save our changes (write quit)


