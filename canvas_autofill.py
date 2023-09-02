from pyautogui import press, typewrite, hotkey
from pynput import keyboard
import time

print("""
Hello please enter all the answers, in sequntial order
if you don't know answer just hit enter
once you are done type # and hit enter
when you are ready to input your answers into canvas
click on the answer section of the first quesiton 
and hit the '+' key""")

ans = []

answer_file_path="/path/to/your/answers/file"

'''
answer file saves answers as one line entry for each question
'''

def take_new_input():
    inp = ""
    c = 1
    inp = input("enter ans for qn 1: ")
    while inp != "#":
        ans.append(inp)
        c += 1
        inp = input(f"enter ans for qn {c}: ")


def type_answers(ans):
    press('backspace')      # remove the '+' that was just typed
    for x in ans:
        typewrite(x)
        press('tab')
        time.sleep(0.1)
        press('tab')
        time.sleep(0.1)


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char
    except:
        k = key.name 
    if k == "+":
        type_answers(ans)


load_from_file = input("load answers from file? 1 for yes 0 for no: ")

if load_from_file == "1":

    with open(answer_file_path, "r") as old_file:
        dirty_ans = old_file.readlines()
        ans = [x[:-1] for x in dirty_ans]    # remove the newline character

else:
    take_new_input()
    with open(answer_file_path, "w") as new_file:
        for x in ans:
            new_file.write(x+"\n")

print("Done loading answers!")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
