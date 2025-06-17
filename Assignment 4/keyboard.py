import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import math

# This is to take the python file called "layout.py" as refrence for the keyboard
import layout


# Given a character, it returns the coordinates of the keys to be pressed
def get_coordinates(char):
    coords = []
    buttons = layout.characters[char]
    for button in buttons:
        coords.append(layout.keys[button]["pos"])
    return coords


# Calculates the total distance fingers have to move to press a certain character
def calc_distance(char):
    buttons = layout.characters[char]
    dist = 0
    for button in buttons:
        movement = layout.keys[button]
        start_key = movement["start"]
        pos_start = layout.keys[start_key]["pos"]
        pos_end = movement["pos"]
        dist += math.dist(pos_start, pos_end)
    return dist


# Taking input string
para = input("Enter Paragraph:")

char_freq = defaultdict(int)
for char in para:
    if char != ' ':
        char_freq[char] += 1

# Total distance calculation
tot_dist = 0
for char in char_freq:
    tot_dist += calc_distance(char) * char_freq[char]
print("Total finger distance travelled:", tot_dist)


# Creating a sort of histogram for the heatmap
coord_freq = defaultdict(int)
for char in char_freq:
    coordinates = get_coordinates(char)
    for coordinate in coordinates:
        coord_freq[coordinate] += char_freq[char]


# Defining the bounds of the keyboard
x_max = max(value["pos"][0] for value in layout.keys.values())
x_min = min(value["pos"][0] for value in layout.keys.values())
y_max = max(value["pos"][1] for value in layout.keys.values())
y_min = min(value["pos"][1] for value in layout.keys.values())


# Required to get a proper looking plot
resolution = 0.5
buffer = 1
x_coords = np.arange(x_min - buffer, x_max + buffer + resolution, resolution)
y_coords = np.arange(y_min - buffer, y_max + buffer + resolution, resolution)

# Creating a frequency grid which is used to make the heatmap
grid = np.zeros((len(y_coords), len(x_coords)))

for (x, y), freq in coord_freq.items():
    x_idx = np.abs(x_coords - x).argmin()
    y_idx = np.abs(y_coords - y).argmin()
    grid[y_idx, x_idx] = freq


plt.figure(figsize=(10, 5))

# Assuming the inter key spacing is at least 1x1
key_width = 0.9
key_height = 0.9

# Creating an object for each key
for key in layout.keys:
    x, y = layout.keys[key]["pos"]
    if x is not None and y is not None:
        rect = plt.Rectangle(
            (x - key_width / 2, y - key_height / 2),
            key_width,
            key_height,
            edgecolor="black",
            facecolor="none",
        )
        plt.gca().add_patch(rect)
        if key in [
            "`",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "_",
            "+",
            "[",
            "]",
            "{",
            "}",
            ":",
            "'",
            '"',
            "<",
            ">",
            "?",
        ]:
            plt.text(
                x - key_width / 4,
                y + key_height / 4,
                key,
                fontsize=8,
                ha="center",
                va="center",
            )
        else:
            plt.text(x, y, key, fontsize=10, ha="center", va="center")

# Making the Heatmap
plt.imshow(
    grid,
    cmap="jet",
    interpolation="bilinear",
    extent=[x_min - 1, x_max + 1, y_min - 1, y_max + 1],
    origin="lower",
    alpha=0.5,
)
plt.colorbar(label="Frequency")

# Finally Plotting
plt.xlim(x_min - buffer, x_max + buffer)
plt.ylim(y_min - buffer, y_max + buffer)
plt.title("Keyboard with Heatmap Overlay")
plt.xticks([])
plt.yticks([])
plt.savefig("keyboardHeatmap.jpg")