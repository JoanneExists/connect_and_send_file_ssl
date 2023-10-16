# connect_and_send_file_ssl
A script I wrote that connects to an ssl-enabled port, sends a file, and receives back data. Can scan for and attempt to connect to open ports or connect to a specified port.
## Setup
```
$ git clone https://github.com/JoanneExists/connect_and_send_file_ssl.git
$ cd connect_and_send_file_ssl/
$ chmod +x connect_and_send_file_ssl.py
$ ./connect_and_send_file_ssl -h
usage: connect_and_send_file_ssl.py [-h] [-n HOSTNAME] [-f FILEPATH] [-p PORT] [-l LOWER_LIMIT] [-u UPPER_LIMIT]

options:
  -h, --help      show this help message and exit
  -n HOSTNAME     Hostname to send file over SSL to or to scan. Defaupper_limitt: localhost
  -f FILEPATH     Use absolute path to your file

Arguments needed for sending file:
  -p PORT         Port to connect to

Arguments -l and -u for port scanning:
  -l LOWER_LIMIT  Lower limit to port scan
  -u UPPER_LIMIT  Upper limit to port scan
```
This will call the script with the 'help' flag for info on how to use the script.
If you need the required packages installed, then run in the same directory as the script:
```
$ pip install pipreqs
$ pipreqs .
$ pip install -r requirements.txt
```
If you need to install pip on Ubuntu, run:
```
$ sudo apt install python3-pip
```
