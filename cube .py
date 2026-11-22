import math
import time
import os

A, B, C = 0, 0, 0
width, height = 60, 28
GREEN = "\033[92m"
RESET = "\033[0m"

def calculate_x(i, j, k):
    return (j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) +
            j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C))

def calculate_y(i, j, k):
    return (j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) -
            j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) -
            i * math.cos(B) * math.sin(C))

def calculate_z(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    z_buffer = [0] * (width * height)
    buffer = [' '] * (width * height)
    cube_width = 12
    
    for cube_x in range(-cube_width, cube_width, 1):
        for cube_y in range(-cube_width, cube_width, 1):
            for surface, ch in [((cube_x, cube_y, -cube_width), '@'), ((cube_width, cube_y, cube_x), '$'),
                                ((-cube_width, cube_y, -cube_x), '~'), ((-cube_x, cube_y, cube_width), '#'),
                                ((cube_x, -cube_width, -cube_y), ';'), ((cube_x, cube_width, cube_y), '+')]:
                x = calculate_x(*surface)
                y = calculate_y(*surface)
                z = calculate_z(*surface) + 60
                ooz = 1 / z
                xp = int(width / 2 + 30 * ooz * x * 2)
                yp = int(height / 2 + 30 * ooz * y)
                idx = xp + yp * width
                if 0 <= idx < width * height and ooz > z_buffer[idx]:
                    z_buffer[idx] = ooz
                    buffer[idx] = ch

    print(GREEN + '\n'.join([''.join(buffer[i:i+width]) for i in range(0, len(buffer), width)]) + RESET)
    A += 0.08
    B += 0.08
    C += 0.04
    time.sleep(0.03)
