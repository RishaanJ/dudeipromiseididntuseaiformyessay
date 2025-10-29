# dudeIPROMISEididntuseai

This is a Python application built with Tkinter and PyAutoGUI that simulates human-like typing (so u don't get caught using ai). Users can enter any text in the GUI, and the program will type it out automatically, adding small pauses, sentence-by-sentence typing, and subtle “edits” to mimic natural typing behavior.

Features

GUI Input: Enter the text you want typed in a simple Tkinter window.

Human-like Typing: Types text slowly, pauses between sentences, and retypes the last word of each sentence for realism.

Automatic Execution: Minimizes the window while typing so it can type anywhere on your screen.

How it Works

User inputs text into the Tkinter entry field.

After a short delay, the program minimizes the window and begins typing.

Each sentence is typed slowly, the last word is backspaced and retyped, then a space is added before moving to the next sentence.

Requirements

Python 3.x

Tkinter (usually included with Python)

PyAutoGUI (pip install pyautogui)
