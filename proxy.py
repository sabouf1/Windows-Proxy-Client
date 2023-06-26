import ctypes
import keyboard
import os
import subprocess
import sys
import time

def enable_system_proxy(proxy_ip, proxy_port):
    # Set system proxy settings
    subprocess.run(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings', '/v', 'ProxyEnable', '/t', 'REG_DWORD', '/d', '1', '/f'])
    subprocess.run(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings', '/v', 'ProxyServer', '/t', 'REG_SZ', '/d', f'{proxy_ip}:{proxy_port}', '/f'])

def disable_system_proxy():
    # Disable system proxy settings
    subprocess.run(['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings', '/v', 'ProxyEnable', '/t', 'REG_DWORD', '/d', '0', '/f'])

def close_connection():
    # Close the connection
    ctypes.windll.user32.PostQuitMessage(0)

def main():
    # Get proxy IP and port from user
    proxy_ip = input("Enter proxy IP: ")
    proxy_port = input("Enter proxy port: ")

    # Enable system proxy
    enable_system_proxy(proxy_ip, proxy_port)

    # Register the "Escape" key to close the connection
    keyboard.on_press_key("esc", lambda _: close_connection())

    # Keep the program running until the connection is closed
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
