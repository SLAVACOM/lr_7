import string
import random
import threading
import time


def random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def main_thread(list_data, event):
    while True:
        new_string = random_string()
        list_data.append(new_string)
        print(list_data)
        time.sleep(1)

def viewer_thread(list_data, event):
    while True:
        print(list_data)
        time.sleep(5)
def sorter_thread(list_data, event):
    while True:
        time.sleep(5)
        sorted_list = sorted(list_data)
        with open("list.txt", "w") as file:
            for item in sorted_list:
                file.write(item + "\n")
shared_list = []
event = threading.Event()

producer = threading.Thread(target=main_thread, args=(shared_list, event))
view = threading.Thread(target=viewer_thread, args=(shared_list, event))
sorter = threading.Thread(target=sorter_thread, args=(shared_list, event))

producer.start()
view.start()
sorter.start()