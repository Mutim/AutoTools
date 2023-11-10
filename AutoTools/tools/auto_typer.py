import pyautogui
import time
import random
import keyboard


# Auto Typer tool
class AutoTyper:
    def __init__(self, options: dict):
        self.options = options

        self.text: str = options["text"]
        # self.text: str = options["text"][:-1]
        self.initial_sleep: int = options["initial_sleep"] / 10
        self.amount_repeat: int = options["amount_repeat"]
        self.time_sleep: int = options["time_sleep"] / 100
        self.random_wait: bool = options["random_wait"]
        self.random_time_min: int = options["random_time_min"] / 100
        self.random_time_max: int = options["random_time_max"] / 100
        self.send_enter: bool = options["send_enter"]

    def log_write(self):
        print(self.options)
        print(f'''
    Text: {self.text}
    Initial Sleep: {self.initial_sleep}s
    Amount Repeat: {self.amount_repeat} Times
    Time Sleep: {self.time_sleep}s
    Random Wait: {"True" if self.random_wait else "False"}
    Pressing Enter: {"True" if self.send_enter else "False"}
    Wait Time Min/Max: {self.random_time_min}s / {self.random_time_max}s
    ''')

    def typer(self):
        print(f'  Session Statistics:\n\t> Sleeping for: {self.initial_sleep} Seconds')
        time.sleep(self.initial_sleep)

        counter = 0
        while counter < self.amount_repeat and not keyboard.is_pressed('f7'):
            print(f'\n\t> Type Count: {counter + 1}\n\t> Sleeping for: {self.time_sleep} Seconds')
            time.sleep(self.time_sleep)
            print(f'\t> Typing Text: {self.text}')
            pyautogui.typewrite(self.text)

            if self.random_wait:
                print(f'\t> Choosing Time between {self.random_time_min} and {self.random_time_max}')
                random_time_to_sleep = round(random.uniform(self.random_time_min, self.random_time_max), 2)
                print(f'\t> Randomly Sleeping for: {random_time_to_sleep}')
                time.sleep(random_time_to_sleep)

            if self.send_enter:
                print(f'\t> Pressing Enter')
                # pyautogui.keyDown('enter')
                time.sleep(0.4)
                # pyautogui.keyUp('enter')
                pyautogui.press('enter', interval=0.1)
            counter += 1
        print(f'  Session Finished')

        