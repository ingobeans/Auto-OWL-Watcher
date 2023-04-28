Dim fso, file
Set fso = CreateObject("Scripting.FileSystemObject")
file = "main.py"

If fso.FileExists(file) Then
	Set oShell = CreateObject ("Wscript.Shell") 
	Dim strArgs
	strArgs = "python main.py"
	oShell.Run strArgs, 0, false

	msgbox("Successfully started Auto-OWL-Watcher, running in background now :)")
Else
    MsgBox("Unable to find main.py, (make sure you're running the this file from the same directory as main.py)")
End If