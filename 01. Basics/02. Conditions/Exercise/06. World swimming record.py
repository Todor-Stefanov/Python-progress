import math

record_sec = float(input())
distance_meters = float(input())
meter_per_sec = float(input())

overall_secs = distance_meters * meter_per_sec
added_sec = distance_meters / 15


added_sec = math.floor(added_sec) * 12.5

overall_time = overall_secs + added_sec


if overall_time >= record_sec:
    print(f'No, he failed! He was {overall_time - record_sec:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {overall_time:.2f} seconds.')
