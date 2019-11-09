from scapy.all import wrpcap, Ether, IP, UDP, TCP

packet1 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet2 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet3 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet4 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet5 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet6 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet7 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet8 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet9 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet10 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet11 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet12 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet13 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet14 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet15 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet16 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet17 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet18 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)
packet19 = Ether() / IP(dst="1.2.3.4") / UDP(dport=123)
packet20 = Ether() / IP(dst="1.2.3.4") / TCP(dport=1234)

array = [packet1, packet2, packet3, packet4, packet5, packet6, packet7, packet8, packet9, packet10, packet11, packet12 \
			, packet13, packet14, packet15, packet16, packet17, packet18, packet19, packet20]

wrpcap('foo.pcap', array)


