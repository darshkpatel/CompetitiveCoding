import random
doors = [1,2,3]
door_1 = random.choice(doors)
print(door_1)
doors.remove(door_1)
door_host = int(input(''))
doors.remove(door_host)
print(doors[0])
