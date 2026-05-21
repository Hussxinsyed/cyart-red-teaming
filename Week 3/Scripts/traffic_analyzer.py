from collections import Counter
from scapy.all import rdpcap
import matplotlib.pyplot as plt

# Load captured packets
packets = rdpcap("capture.pcap")

packet_sizes = []
source_ips = []

# Read packet information
for packet in packets:
    packet_sizes.append(len(packet))

    if packet.haslayer("IP"):
        source_ips.append(packet["IP"].src)

# Count source IPs
ip_count = Counter(source_ips)

print("Packet Count by Source IP:")
for ip, count in ip_count.items():
    print(f"{ip}: {count}")

# Create bar chart
plt.bar(range(len(packet_sizes)), packet_sizes)

plt.xlabel("Packet Number")
plt.ylabel("Packet Size (Bytes)")
plt.title("Packet Size Distribution")

plt.show()
