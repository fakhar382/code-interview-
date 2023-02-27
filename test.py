# Define the list of colors for each day of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
colors = [
    ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
]


all_colors = [color for day in colors for color in day]


def variance(colors):
    mean = sum(colors) / len(colors)
    variance = sum((x - mean) ** 2 for x in colors) / len(colors)
    return variance



# Count the number of occurrences of each color
color_counts = {}
for color in all_colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1
most_common_color = max(color_counts, key=color_counts.get)

for i, day in enumerate(colors):
    # Count the number of occurrences of each color for the current day
    color_counts = {}
    for color in day:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    # Calculate the mean color for the current day
    total_count = sum(color_counts.values())
    
    
    max_frequency = 0
    mean_color = ''
    for color, count in color_counts.items():
        frequency = count / total_count     
        if frequency > max_frequency:
            max_frequency = frequency
            mean_color = color

    # Find the median color for the current day
    sorted_colors = sorted(set(day))
    num_colors = len(sorted_colors)
    if num_colors % 2 == 0:
        median_color = sorted_colors[num_colors // 2 - 1]
    else:
        median_color = sorted_colors[num_colors // 2]
        # convert colors to numerical values using a dictionary
    color_values = {'GREEN': 1, 'YELLOW': 2, 'BROWN': 3, 'BLUE': 4, 'PINK': 5, 'ORANGE': 6, 'CREAM': 7, 'RED': 8, 'WHITE': 9, 'ARSH': 10, 'BLEW': 11, 'BLACK': 12}
    numerical_colors = [color_values[color] for color in day]
    day_variance = variance(numerical_colors)

    color_counts = {'MONDAY': {}, 'TUESDAY': {}, 'WEDNESDAY': {}, 'THURSDAY': {}, 'FRIDAY': {}}
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


    # Print the results for the current day
    print(f"{days[i]}:")
    print("Mean color:", mean_color)
    print("Median color:", median_color)
    print("Variance: ",day_variance)
    print(f"The probability of red color on {day} is: {red_prob:.2f}")
 
    print()  # Add a blank line between days
print("Most Common color throughout the week is :", most_common_color)
print()  # Add a blank line between days



    


    



