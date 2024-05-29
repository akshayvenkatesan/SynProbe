Run Instructions:
- sudo python3 synprobe.py <target address> -p <port_number>     (Port number is an optional parameter)

Program explaination:
1. The main function takes in the input arguments for target address and port. If port number is not specified, then based out of a list of given ports as per the task, the check is done for open ports
2. Firstly, the check is done for TLS and a TLS server can also techincally a TCP server. The checks are done for the given categories 1-6 (Server inititated, GET request and Generic request) and then the response is given along with the category. (Perfomed by port_scan)
3. The first 1024 characters are returned. (Retuned by probe_port function)


Sample outputs:
┌──(kali㉿kali)-[~]
└─$ sudo python3 testprobe.py smtp.mail.yahoo.com -p 587
Checking for ports: [587]
Currently open ports: [587]

Testing port 587...
Port 587 Type 1: 220 smtp.mail.yahoo.com ESMTP ready

                                                                                                   
┌──(kali㉿kali)-[~]
└─$ cd Downloads
                                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo python3 synprobe.py ftp.dlptest.com -p 21      
Scanning ftp.dlptest.com on ports: [21]
Open ports: [21]

Testing port 21...
Port 21 Type 1: 220 Welcome to the DLP Test FTP Server

                                                                                                   
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo python3 synprobe.py www.cs.stonybrook.edu       
Scanning www.cs.stonybrook.edu on ports: [21, 22, 23, 25, 80, 110, 143, 443, 587, 853, 993, 3389, 8080]
Open ports: [80, 443]

Testing port 80...
Port 80 Type 3: HTTP/1.1 404 Unknown site
Connection: close
Content-Length: 566
Retry-After: 0
Server: Pantheon
Cache-Control: no-cache, must-revalidate
Content-Type: text/html; charset=utf-8
X-pantheon-serious-reason: The page could not be loaded properly.
Date: Sat, 04 May 2024 04:27:54 GMT
X-Served-By: cache-lga21955-LGA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1714796875.609041,VS0,VE28
Vary: Cookie
Age: 0
Accept-Ranges: bytes
Via: 1.1 varnish

<!DOCTYPE HTML>
      <html>
        <head>
          <title>404 - Unknown site</title>
        </head>
        <body style="font-family:Arial, Helvetica, sans-serif; text-align: center">
          <div style='padding-block: 180px'>
            <h1>
              <div style='font-size: 180px; font-weight: 700'>404</div>
              <div style='font-size: 24px; font-weight: 700'>Unknown site</div>
            </h1>
            <p style="font-size: 16px; font-weight: 400">The page could not be loaded properly.</p>
          </div>
        </body>
      </html>

Testing port 443...
Port 443 Type 4: HTTP/1.1 404 Unknown site
Connection: close
Content-Length: 566
Retry-After: 0
Server: Pantheon
Cache-Control: no-cache, must-revalidate
Content-Type: text/html; charset=utf-8
X-pantheon-serious-reason: The page could not be loaded properly.
Date: Sat, 04 May 2024 04:27:57 GMT
X-Served-By: cache-lga21925-LGA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1714796878.703481,VS0,VE24
Vary: Cookie
Age: 0
Accept-Ranges: bytes
Via: 1.1 varnish
