import socket

def scan_ports(target, ports):
    print(f"\nScanning target: {target}\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is closed")

            sock.close()

        except socket.error:
            print("Could not connect to server")

target = input("Enter target IP address: ")

common_ports = [21, 22, 23, 25, 53, 80, 110, 443]

scan_ports(target, common_ports)
