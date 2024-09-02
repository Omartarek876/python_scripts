# python_scripts


# how to create a shortcut for the script 
    - Create a Batch File (.bat):
        - Open Notepad or any text editor.
        - Write the following code, replacing the paths with the path to your Python executable and your Python script:
                " @echo off
                   "path to file.exe" "path to script.py"
                   pause
                "
        - Save this file with a .bat extension

    - Create a Shortcut to the .bat File:
        -  Right-click on the .bat file you created.
        - Select "Create shortcut."
        - Optionally, you can move this shortcut to your desktop or any other convenient location. 

 >>>> Now, you can double-click the shortcut to run the Python script. The command prompt will open, run the script, and stay open until you press any key (because of the pause command) <<<<



 # how to create a file.exe 
   - you need to install PyInstaller : pip install pyinstaller
   - Once PyInstaller is installed, you can create an executable from your Python script. Open your command prompt, navigate to the directory   containing your Python script, and run: 
         - pyinstaller --onefile "path to script.py"
   - After running the command, PyInstaller will generate several files and directories. The executable will be located in the dist folder inside the directory where you ran the command : 
         - path to dist\file.exe
   - You can now double-click the .exe file to run your script. The script will run independently of Python.

