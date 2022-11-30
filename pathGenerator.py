import random


class PathGenerator:
    directions = ["up", "down", "left", "right", "forward",
                  "backward", "clockwise", "counter-clockwise"]

    steps = int(input("How many steps do you want: ")) + 1

    print("Step 0: Go up for {:d} inches.".format(random.randint(20, 40)))

    for i in range(1, steps):
        direction = random.choice(directions)

        if direction in ["clockwise", "counter-clockwise"]:
            unit = "degrees"
            magnitude = random.randint(0, 720)
        else:
            unit = "inches"
            magnitude = random.randint(0, 20)

        print("Step {:d}: Go {:s} for {:d} {:s}.".format(
            i, direction, magnitude, unit))

    print("Step {:d}: land".format(steps))
