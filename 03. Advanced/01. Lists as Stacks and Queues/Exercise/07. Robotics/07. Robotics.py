from collections import deque


def time_plus_one_second(some_timer):
    seconds = int(some_timer[2])
    minutes = int(some_timer[1])
    hours = int(some_timer[0])
    seconds += 1
    if seconds == 60:
        seconds = "00"
        minutes += 1
    if 0 < int(seconds) < 10:
        seconds = "0" + f"{seconds}"
    if minutes == 60:
        minutes = "00"
        hours += 1
    if minutes == 0:
        minutes = "00"
    if 0 < int(minutes) < 10:
        minutes = "0" + f"{minutes}"
    return [hours, minutes, seconds]


def calculate_available_at(some_timer, robots_proc_time):
    seconds = int(some_timer[2])
    minutes = int(some_timer[1])
    hours = int(some_timer[0])
    seconds += robots_proc_time
    if seconds >= 60:
        if seconds == 60:
            seconds = "00"
            minutes += 1
        else:

    if 0 < int(seconds) < 10:
        seconds = "0" + f"{seconds}"
    if minutes == 60:
        minutes = "00"
        hours += 1
    if minutes == 0:
        minutes = "00"
    if 0 < int(minutes) < 10:
        minutes = "0" + f"{minutes}"
    return [hours, minutes, seconds]


robots = input().split(';')
robots_queue = deque([])
robots_dict = {}
for robot in robots:
    name, processing_time = robot.split("-")
    robots_queue.append((name, processing_time))
    robots_dict[name] = {}
    robots_dict[name]["pt"] = int(processing_time)
    robots_dict[name]["is_busy"] = False
    robots_dict[name]["product"] = ""
    robots_dict[name]['free_at'] = ''

timer = input().split(":")

product = input()

products_list = deque([])
while product != "End":
    timer = time_plus_one_second(timer)
    current_name, current_proc_time = robots_queue.popleft()
    if not robots_dict[current_name]['is_busy']:
        robots_dict[current_name]['free_at'] = 0
        robots_dict[current_name]['is_busy'] = True
    else:
        pass

    product = input()
