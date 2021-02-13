import socket
import sys

# defining the port scanner function
def scan_ports(remote_ip):
    remote_server_ip = socket.gethostbyname(remote_ip)

    # print a little banner on which ip we are scanning
    print("-" * 60)
    print("Please wait while {} is being scanned...".format(remote_ip))
    print("-" * 60)
    print("")

    # looping through top 1024 common ports and attempting to connect to the looped ports
    try:
        for port in range(1, 1025):
            my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = my_sock.connect_ex((remote_server_ip, port))     
            if result == 0:
                print("Port {:>4} is open!".format(port))
            my_sock.close()
    except KeyboardInterrupt:
        sys.exit()
    except socket.gaierror:
        print("Host name could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

    print("\nScan complete.")

# creating the command line args and a little help section
if len(sys.argv) > 1:
        if sys.argv[1] == '--ip':
            ip = str(sys.argv[2])
            scan_ports(ip)
else:
    print('\n')
    print('=' * 45)
    print("\t\tUsage Section")
    print('\n')
    print('--ip\t ip address to scan')
    print('=' * 45)
    print('\n')
    