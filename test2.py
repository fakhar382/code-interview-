colors = [
    ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
]

# Create a dictionary to store the count of each color for each day
color_counts = {'MONDAY': {}, 'TUESDAY': {}, 'WEDNESDAY': {}, 'THURSDAY': {}, 'FRIDAY': {}}

# Loop through each day and count the occurrences of each color
for i, day in enumerate(color_counts.keys()):
    for color in colors[i]:
        if color in color_counts[day]:
            color_counts[day][color] += 1
        else:
            color_counts[day][color] = 1

# Calculate the probability of red color for each day and print the results
for day, counts in color_counts.items():
    total_colors = sum(counts.values())
    red_count = counts.get('RED', 0)
    red_prob = red_count / total_colors
    print(f"The probability of red color on {day} is: {red_prob:.2f}")


