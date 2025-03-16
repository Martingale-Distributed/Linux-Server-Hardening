import os   
import sys
import subprocess
import datetime
import time


# Check if running as root
if os.getuid() != 0
    print("Please run as a root user. DOn't run ON root.")
    sys.exit(1)
    
    
    
    class ServerHardening:
        def __init__(self):
            basic_commands= [
                
                "dnf update -y", 
                "dnf upgrade -y",
                "dnf install -y auditd fail2ban git nodejs npm python3 python3-pip",
                "systemctl enable --now auditd",
                "systemctl enable --now fail2ban",
            ]
            print("Initializing package install and updastes complete.. moving onto next install processes and config ")
            
            ## WIP