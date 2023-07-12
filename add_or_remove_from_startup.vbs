Dim fso, file
Set fso = CreateObject("Scripting.FileSystemObject")
file = "startup.py"

If fso.FileExists(file) Then
	Set oShell = CreateObject ("Wscript.Shell") 
	Dim strArgs
	strArgs = "python startup.py"
	oShell.Run strArgs, 1, true
Else
    MsgBox("Unable to find startup.py, (make sure you're running the this file from the same directory as startup.py)")
End If