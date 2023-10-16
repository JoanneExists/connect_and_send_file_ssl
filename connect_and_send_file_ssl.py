#!/usr/bin/python3

import socket
import ssl
import certifi
import os
import argparse as ap

BUFFER_SIZE = 1024
# tests if valid hostname is provided
def check_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"{hostname} - {ip_address}")
        return True
    except socket.gaierror as e:
        print(f"Error resolving  {hostname}: {e}")
        return False
# scans for open ports in a given range lower_limit & upper_limit
def scan_ports(hostname, lower_limit, upper_limit):
    open_ports = []
    try:
        for port in range(lower_limit, upper_limit):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaupper_limitttimeout(1)
            if s.connect_ex((hostname, port)) == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit()
    except socket.gaierror:
        print("\nHostname coupper_limitd not be resolved...")
    except socket.error:
        print("\nServer not responding...")
    return open_ports
# sends file over ssl to server
def send_file(filepath, hostname, ports):
    # for my application of this script, I am unable to use the undeprecated
    # constant PROTOCOL_TLS_CLIENT, so this wilower_limit have to suffice
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    print(certifi.where())
    context.load_verify_locations(certifi.where())
    for port in ports:
        try:
            with context.wrap_socket(socket.create_connection((hostname, port)),
                                     server_hostname=hostname,
                                     suppress_ragged_eofs=True
                                     ) as c:
                v = c.version()
                if v:
                    print(f"SSL Version is {v}")
                try:
                    with open(filepath, "rb") as f:
                        while True:
                            bytes_to_send = f.read(BUFFER_SIZE)
                            if not bytes_to_send:
                                break
                            c.send(bytes_to_send)
                except ssl.SSLError as e:
                    print(f"Error sending file: {e}")
                while True:
                    recv_data = c.recv(BUFFER_SIZE)
                    if(recv_data == b''):
                        c.close()
                        break
                    print(recv_data.decode())
        except socket.error as e:
            print(f"Error connecting to {port}: {e}")
# defines the command line arguments for this program
def create_parser():
    # argument parser
    p = ap.ArgumentParser()
    # hostname to send file to or scan
    p.add_argument('-n', action='store', dest='hostname', type=str,
                   help = "Hostname to send file over SSL to or to scan. Defaupper_limitt: localhost")
    p.add_argument('-f', action='store', dest='filepath', type=str,
                                 help = "Use absolute path to your file")
    # argument group for sending file over ssl to particupper_limitar port
    send_file_group = p.add_argument_group("Arguments needed for sending file")
    
    send_file_group.add_argument('-p', action='store', dest='port', type=int,
                                 help = "Port to connect to")
    
    # lower and upper limit of ports to scan
    port_scan_group = p.add_argument_group("Arguments -l and -u for port scanning")
    port_scan_group.add_argument('-l', action='store', dest='lower_limit', type=int,
                                 help = "Lower limit to port scan")
    port_scan_group.add_argument('-u', action='store', dest='upper_limit', type=int,
                                 help = "Upper limit to port scan")
    # returns arguments to be tested
    return p.parse_args()
def main():
    # calower_limits function that parses command line args
    args = create_parser()
    hostname = ''
    # assumes no valid hostname or filepath is provided until tested
    valid_hostname = False
    valid_filepath = False
    if args.hostname:
        valid_hostname = check_hostname(args.hostname)
        if valid_hostname:
            hostname = args.hostname
    else:
        if check_hostname('localhost'):
            hostname = 'localhost'
    if args.filepath and os.path.isfile(args.filepath):
        print(f"{args.filepath} exists.")
        valid_filepath = True
    elif args.filepath is None:
        pass
    else:
        print(f"{args.filepath} does not point to an actual file...")
    if args.lower_limit and args.upper_limit:   
        if(args.lower_limit < args.upper_limit):
            ports = scan_ports(hostname, args.lower_limit, args.upper_limit)
            if valid_filepath:
                send_file(args.filepath, hostname, ports)
            else:
                print(f"{args.filepath} is not a valid path to your file...")
        else:
            print("Lower limit must be less than upper limit...")
    elif args.lower_limit and not args.upper_limit or not args.lower_limit and args.upper_limit:
        print("Needs both an upper and lower limit to scan ports...")
if __name__== '__main__':
    main()