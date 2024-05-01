import tkinter as tk
import subprocess
import ctypes
import sys

# Publisher information
COMPANY_NAME = "R4V3N-J3R0N"
FILE_DESCRIPTION = "Internet disable and enable"
LEGAL_COPYRIGHT = "Copyright (C) 2024 J3R0N"


def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

# Call the function to request admin privileges
run_as_admin()

# Your main script code here...


def enable_internet():
    subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "enabled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["netsh", "interface", "set", "interface", "WiFi", "enabled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def disable_internet():
    subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "disabled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["netsh", "interface", "set", "interface", "WiFi", "disabled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

root = tk.Tk()
root.title("Internet Control")
root.configure(bg="black")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))



center_window(root, 50, 80)
root.grab_set()


enable_button = tk.Button(root, text="Enable Internet", command=enable_internet, bg="green")
enable_button.pack(pady=5)

disable_button = tk.Button(root, text="Disable Internet", command=disable_internet, bg="green")
disable_button.pack(pady=5)


root.mainloop()
