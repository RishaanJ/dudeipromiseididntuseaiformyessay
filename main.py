import tkinter as tk
import pyautogui
import time
import re

def save_input():
    user_input = entry.get()
    if user_input:
        result_label.config(text=f"I'll type it with human-like edits in 3 seconds...")
        root.after(3000, lambda: startTyping(user_input))
    else:
        result_label.config(text="Nothing entered.")

def startTyping(text):
    root.iconify()
    root.after(500, lambda: humanTyping(text))

def humanTyping(text):
    sentences = re.split(r'(?<=[.!?])\s*', text)
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # type the sentence slowly
        pyautogui.write(sentence, interval=0.07)
        time.sleep(0.45)

        # figure out the last word (keeps punctuation attached)
        words = sentence.split()
        if len(words) > 0:
            last_word = words[-1]
            # delete only the characters of the last word
            for _ in range(len(last_word)):
                pyautogui.press("backspace")
                time.sleep(0.05)

            # short pause then retype the last word
            time.sleep(0.25)
            pyautogui.write(last_word, interval=0.07)

        # add a space after the sentence so sentences do not glue together
        pyautogui.write(" ")
        time.sleep(0.6)

root = tk.Tk()
root.title("Typer")
root.geometry("400x300")

label = tk.Label(root, text="What do you want me to type?")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=save_input)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()
