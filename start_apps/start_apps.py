#!/usr/bin/env python3
"""
Script to automate opening applications, websites, and folders on Windows.

Author: Omar Tarek
Last Updated: 2024-09-03
Programming Language: Python

Description:
This script uses the pyautogui and subprocess modules to automate:
1. Opening specified applications.
2. Opening a list of websites in the default web browser.
3. Opening specified folders in Windows File Explorer.

Dependencies:
- pyautogui
- subprocess
- webbrowser
- time

Usage:
Run this script using PyInstaller with the `--onefile` option to package it into a standalone executable. 

Notes:
 - check ReadME file to know the steps of how to create a shortcut and executable file to your script  
 - "pyinstaller --onefile start_apps.py" => this command to recreate file.exe if you update the script
"""

import pyautogui
import time
import webbrowser
import subprocess

# List of applications to open
app_list = [
    "vscode",  # Visual Studio Code
    "git bash"  # Git Bash
]

# List of websites to open in the default web browser
websites_list = [
    "https://github.com/Omartarek876",
    "https://chatgpt.com/",
    "https://drive.google.com/drive/u/2/my-drive",
    "https://mail.google.com/mail/u/2/#inbox"
]

# List of folders to open in Windows File Explorer
folders_list = [
    "D:\\4th_year\\3_Graduation_project\\" , 
    "D:\\courses\\Embedded_Linux\\01-Python\\"
]

def open_chrome_with_url(url):
    """
    Open a URL in the default web browser.
    
    Args:
        url (str): The URL to open.
    """
    webbrowser.open(url, new=2)  # Open URL in a new tab of the default web browser
    time.sleep(1)

def navigate_to_app(app_name):
    """
    Open an application using the Windows start menu.
    
    Args:
        app_name (str): The name of the application to open.
    """
    pyautogui.hotkey('win')  # Open the Start menu
    time.sleep(1)
    pyautogui.write(app_name)  # Type the application name
    time.sleep(1)
    pyautogui.hotkey('enter')  # Press Enter to open the application
    time.sleep(1)
    pyautogui.hotkey('win', 'left')  # Snap the window to the left side of the screen
    time.sleep(2)
    close_current()  # Minimize all windows to show the desktop

def open_folder_windows(folder_path):
    """
    Open a folder in Windows File Explorer.
    
    Args:
        folder_path (str): The path of the folder to open.
    """
    subprocess.run(['explorer', folder_path], shell=True)  # Open the folder
    time.sleep(1)
    # Optionally, you can close the current window after opening the folder
    # close_current()

def close_current():
    """
    Minimize all windows to show the desktop.
    """
    pyautogui.hotkey('win', 'd')  # Show the desktop
    time.sleep(1)

def main():
    """
    Main function to execute the automation tasks.
    """
    close_current()  # Minimize all windows to show the desktop
    
    # Open specified applications
    for app in app_list:
        navigate_to_app(app)
    
    # Open specified websites
    for site in websites_list:
        open_chrome_with_url(site)
    
    close_current()  # Minimize all windows to show the desktop
    
    # Open specified folders
    for folder in folders_list:
        open_folder_windows(folder)

if __name__ == "__main__":
    main()
