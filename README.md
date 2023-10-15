# connect_and_send_file_ssl
A script I wrote that connects to an ssl-enabled port, sends a file, and receives back data. Can scan for and attempt to connect to open ports or connect to a specified port.
## Setup
```
$ git clone https://github.com/JoanneExists/connect_and_send_file_ssl.git
$ cd connect_and_send_file_ssl/
$ chmod +x connect_and_send_file_ssl.py
$ ./connect_and_send_file_ssl -h
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
