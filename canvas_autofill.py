from pyautogui import press, typewrite, hotkey
from pynput import keyboard
import time
ans = []


def take_new_input():
    global ans
    file_path = get_ans_file_path()

    inp = ""
    c = 0
    while inp != "#":
        c += 1
        inp = input(f"enter ans for qn {c}: ")
        ans.append(inp)

    ans.pop()   # remove the # from the list of answers

    with open(file_path, "w") as new_file:
        for x in ans:
            new_file.write(x+"\n")
    return ans


def get_ans_file_path():
    answer_folder = "/home/antimony/school/"
    default_file_name = "canvas_answers"

    file_name = input(
        "enter the name of the file where you want to save\nthese answers hit enter to use the default file: ")

    if file_name:
        file_path = answer_folder+file_name

    else:
        file_path = answer_folder+default_file_name

    return file_path


def type_answers():
    global ans
    press('backspace')      # remove the '+' that was just typed
    for x in ans[:-1]:      # loop until the second last element
        typewrite(x)
        press('tab')
        time.sleep(0.01)
        press('tab')
        time.sleep(0.1)

    typewrite(ans[-1])      # type the last element


def load_ans():

    load_from_file = input("load answers from file? 1 for yes 0 for no: ")
    if load_from_file == "1":
        file_path = get_ans_file_path()
        answers = load_a_from_file(file_path)
    else:
        answers = take_new_input()

    print("Done loading answers!")
    return answers


def load_a_from_file(file_path):

    with open(file_path, "r") as old_file:
        file_lines = old_file.readlines()
        # remove the newline character
        answers = [x[:-1] for x in file_lines]
    return answers


def on_press(key):
    if key == keyboard.Key.esc:
        return False        # stop listener
    try:
        k = key.char
    except:
        k = key.name
    if k == "+":
        type_answers()


def main():
    print("""
Hello, please enter all the answers in sequntial order
if you don't know answer for a question just hit enter and
continue to the next question once you are done type # 
and hit enter. When you are ready to input your answers
into canvas got the canvas quiz page, and click on the 
answer field for the first question and hit the '+' key
the script will now automatically type the answers in
---press the esc key to kill the script---
    """)
    global ans
    ans = load_ans()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()


if __name__ == "__main__":
    main()
