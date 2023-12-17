import threading
import random
import time
import string


def generate_random_strings():
    while True:
        random_string = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
        with lock:
            my_list.append(random_string)
        time.sleep(3)


def print_list():
    while True:
        with lock:
            print(my_list)
        time.sleep(3)


def sort_and_save_list():
    while True:
        with lock:
            my_list.sort()
            with open("list.txt", "w") as file:
                for item in my_list:
                    file.write(f"{item}\n")
        time.sleep(5)

my_list = []

lock = threading.Lock()

main = threading.Thread(target=generate_random_strings)
view_list = threading.Thread(target=print_list)
sort_and_save_list_file = threading.Thread(target=sort_and_save_list)

main.start()
view_list.start()
sort_and_save_list_file.start()
