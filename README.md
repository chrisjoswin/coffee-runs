# coffee-runs
The Coffee Payment Decider is a command-line application built using Python and to help coworkers at the office decide who should pay for coffee each day. It allows users to create and manage a list of group members, their favorite coffee orders, and tracks who is responsible for paying for the coffee each day.

## Quick Start
1. Download main.exe file
2. 
## Pre-Requisites
If you choose to run this program without the executable you will need a few things. If you just want to run the executable then go to the next section
1. Download Python3.x https://www.python.org/downloads/
2. We will need to install openpyxl to use excel sheets. In terminal run   ```pip3 install openpyxl```
3. We will need to install boto3 to access AWS. In terminal run  ```pip3 install boto3```

## Setting Up AWS
If you would like to retrieve the menu from the AWS S3 bucket you will need to add the ```AWS_ACCESS_KEY_ID``` and ```AWS_SECRET_ACCESS_KEY``` to your ```~/.bashrc``` file. If you do not do this, it is completely fine and the menu will be retrieved from a local excel file. Skip to the next section if you would like to retrieve the menu locally
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

## Getting Application Started
1. In terminal run ```git clone https://github.com/chrisjoswin/coffee-runs.git``` to 
2. 
3. run ```python3 main.py```

## Assumptions
1. Made some assumptions about input values. When prompted for Menu options, the input must be exactly as printed
2. This is used for groups and not everyone will want coffee every time or will not be present at the office
3. The price of any one coffee is not more that 5 dollars than any other coffee

## Author
[Christopher Erattuparambil](https://github.com/chrisjoswin)





