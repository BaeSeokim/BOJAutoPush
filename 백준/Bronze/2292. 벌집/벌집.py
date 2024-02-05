n = int(input())

if n == 1:
    print(1)
else:
    layer = 1
    room_count = 1
    while n > room_count:
        room_count += 6 * layer
        layer += 1

    print(layer)
