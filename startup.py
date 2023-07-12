import os
import win32com.client

def create_shortcut(source_path, shortcut_path):
    #chatgpt created function btw
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = source_path
    shortcut.WorkingDirectory = os.path.dirname(source_path)
    shortcut.IconLocation = source_path
    shortcut.save()


current_dir = os.getcwd()
startup_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
file_path = os.path.join(startup_path,"AutoOWL.lnk")

is_installed = os.path.exists(file_path)

print(f"AutoOWL is currently {'added to startup' if is_installed else 'not added to startup'}")
i = input("What do you want to do? Type 'add' to add AutoOWL to startup, type 'remove' to remove AutoOWL from startup\n\n: ")

if i == "add":
    main_path = os.path.join(current_dir,"launch headless.vbs")
    create_shortcut(main_path,file_path)
    print("Successfully added AutoOWL to startup")
elif i == "remove":
    os.system(f"del /q {file_path}")
else:
    print("Unknown input.")


os.system("pause")