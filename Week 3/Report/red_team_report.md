# Red Team Report

## Executive Summary

This report summarizes the practical and theoretical activities performed during the Red Team learning tasks. The objective was to understand reconnaissance techniques, initial access methods, exploitation concepts, lateral movement, persistence methods, and reporting practices within a controlled lab environment.

Different tools and methodologies were reviewed to understand how attackers gather information, identify targets, and simulate attack workflows ethically.

---

## Findings

### Reconnaissance

Recon-ng and Shodan were explored to understand information gathering techniques.

Reconnaissance helps collect publicly available information and identify potential targets before further actions.

Shodan was used to search exposed services and observe internet-facing systems.

---

### Network Scanning

Nmap was used to identify open ports and running services on the target machine.

The command used:

```bash
nmap -sV 192.168.78.128
