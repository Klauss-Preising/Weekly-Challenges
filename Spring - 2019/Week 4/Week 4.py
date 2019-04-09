"""
Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

How many lights are on?
"""

lights = [[0 for i in range(1000)]for i in range(1000)]

fh = open("input.txt", "r")
instructions = [i.replace("\n", "").split() for i in fh.readlines()]
fh.close()


def turn(on, pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] = 1 if on else 0


def toggle(pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] = 1 if lights[i][j] == 0 else 0


for i in instructions:
    if i[0] == "turn":
        pos1 = [int(i) for i in i[2].split(",")]
        pos2 = [int(i) for i in i[4].split(",")]
        turn(i[1] == "on", pos1, pos2)
    else:
        pos1 = [int(i) for i in i[1].split(",")]
        pos2 = [int(i) for i in i[3].split(",")]
        toggle(pos1, pos2)


answer = 0

for i in lights:
    answer += sum(i)

print(answer)
