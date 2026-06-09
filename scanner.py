
import nmap
import sys

def test_nmap_installation():
  try:
     nm = nmap.portScanner()
print(f"[+] Nmap successfully initialized. Version: {nm.nmap_version_string()}")
    except nmap.PortScannerError:
print("[-] Nmap not found in system path. Please ensure Nmap is installed.")
        sys.exit(1)
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
      print("[*] Starting Network Scanner Project...")
    test_nmap_installation()
"""Scans the target subnet for live hosts and common open ports
"""
nm = nmap.PortScanner()
    print(f"[*] Scanning subnet: {target_subnet}...")

