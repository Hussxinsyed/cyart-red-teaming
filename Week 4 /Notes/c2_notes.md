# Advanced C2 Notes

C2 stands for Command and Control.

A C2 framework enables communication between an operator and a compromised system.

Beaconing refers to repeated communication between a host and a remote server for instructions.

HTTPS traffic is commonly used because encrypted communication blends into normal network traffic.

MITRE ATT&CK:
T1071 - Application Layer Protocol

Practical Observation:

Wireshark was used to observe encrypted TLS communication. Metadata such as packet timing, source IP addresses, destination IP addresses, and packet lengths remained visible even though payload contents were encrypted.
