import sys
import socket
import ssl
import argparse
from scapy.all import sr1, IP, TCP
import select


def syn_scan(host, port_range):
   open_ports = []
   for port in port_range:
       packet = IP(dst=host)/TCP(dport=port, flags='S')
       response = sr1(packet, timeout=1, verbose=0)
       if response and response.haslayer(TCP) and response.getlayer(TCP).flags & 0x12:
           open_ports.append(port)
           sr1(IP(dst=host)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
   return open_ports


def probe_port(host, port, use_tls=False):
   type_of_server = []
   responses = []
   try:
       s = socket.create_connection((host, port), timeout=3)
       if use_tls:
           context = ssl.create_default_context()
           s = context.wrap_socket(s, server_hostname=host)


       # Checking for server-initiated responses
       s.settimeout(3)
       try:
           initial_data = s.recv(1024)
           if initial_data:
               type_of_server.append((2 if use_tls else 1, initial_data.decode('utf-8', 'replace')[:1024]))
               return type_of_server
       except socket.timeout:
           initial_data = None


       # Checking GET requests
       http_get_request = b"GET / HTTP/1.0" + b"\r\n\r\n"
       s.sendall(http_get_request)
       try:
           http_response = s.recv(1024)
           if http_response:
               type_of_server.append((4 if use_tls else 3, http_response.decode('utf-8', 'replace')[:1024]))
               return type_of_server
       except socket.timeout:
           pass


       # Checking generic requests
           generic_request = b"\r\n\r\n\r\n\r\n"
           s.sendall(generic_request)
     
       try:
           generic_response = s.recv(1024)
           if generic_response:
               type_of_server.append((6 if use_tls else 5, generic_response.decode('utf-8', 'replace')[:1024]))
               return type_of_server
       except socket.timeout:
           pass


   except Exception as e:
       responses.append(f"Error on port {port} with {'TLS' if use_tls else 'TCP'}: {str(e)}")
   finally:
       s.close()


   return type_of_server


def main():
   parser = argparse.ArgumentParser(description='TCP Service Fingerprinting Tool')
   parser.add_argument('-p', '--ports', help='Range of ports to scan (e.g., 80-90 or 80)', required=False)
   parser.add_argument('target', help='IP address of the target host')
   args = parser.parse_args()


   target = args.target
   if args.ports:
       if '-' in args.ports:
           start_port, end_port = map(int, args.ports.split('-'))
           port_range = range(start_port, end_port + 1)
       else:
           port_range = [int(args.ports)]
   else:
       default_ports = [21, 22, 23, 25, 80, 110, 143, 443, 587, 853, 993, 3389, 8080]
       port_range = default_ports


   print(f"Scanning {target} on ports: {list(port_range)}")
   open_ports = syn_scan(target, port_range)
   print("Open ports:", open_ports)


   for port in open_ports:
       print(f"\nTesting port {port}...")
       tcp_results = []
       tls_results = probe_port(target, port, use_tls=True)
       #Checking TLS first
       if not tls_results:
           tcp_results = probe_port(target, port)
       
       for result in tcp_results + tls_results:
           print(f"Port {port} Type {result[0]}: {result[1]}")


if __name__ == "__main__":
   main()



