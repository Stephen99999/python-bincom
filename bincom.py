import re
import random
import psycopg2
import numpy as np
import requests

# Send a GET request to the webpage no webpage in the question though just an example
response = requests.get("https://example.com/page_with_colors")

# Check if the request was successful
if response.status_code == 200:
    # Extract the content of the webpage
    webpage_content = response.text
    # Now you have the webpage content, you can proceed to extract the colors using regular expressions or any other method.
else:
    print("Failed to fetch webpage:", response.status_code)

# Sample data for demonstration purposes
#would have usd webpage content but no webpage
sample_data = """
Monday: red, blue, green
Tuesday: green, yellow, blue
Wednesday: red, red, red
Thursday: blue, blue, yellow
Friday: green, green, blue
"""

# Extract colors from the sample data
colors = re.findall(r"\b\w+\b", sample_data.lower())


# Function to calculate mean color
def mean_color(colors):
    color_counts = {color: colors.count(color) for color in set(colors)}
    total_count = sum(color_counts.values())
    mean_color = max(color_counts, key=lambda x: color_counts[x] / total_count)
    return mean_color


# Function to calculate mode (most frequent color)
def mode_color(colors):
    color_counts = {color: colors.count(color) for color in set(colors)}
    mode_color = max(color_counts, key=color_counts.get)
    return mode_color


# Function to calculate median color
def median_color(colors):
    color_counts = {color: colors.count(color) for color in set(colors)}
    sorted_colors = sorted(color_counts, key=lambda x: (color_counts[x], x))
    median_index = len(sorted_colors) // 2
    median_color = sorted_colors[median_index]
    return median_color


# Bonus: Calculate variance of colors
def color_variance(colors):
    color_counts = {color: colors.count(color) for color in set(colors)}
    frequencies = list(color_counts.values())
    variance = np.var(frequencies)
    return variance


# Bonus: Calculate probability of choosing red color
def red_probability(colors):
    red_count = colors.count('red')
    total_count = len(colors)
    probability = red_count / total_count
    return probability


# Save colors and their frequencies to PostgreSQL database
def save_to_database(colors, color_counts=None):
    conn = psycopg2.connect(
        database="your_database",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()

    for color, count in color_counts.items():
        cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, count))

    conn.commit()
    conn.close()


# Bonus: Recursive searching algorithm
def recursive_search(lst, num, index=0):
    if index >= len(lst):
        return False
    if lst[index] == num:
        return True
    return recursive_search(lst, num, index + 1)


# Function to generate random 4-digit number of 0s and 1s and convert to base 10
def generate_and_convert():
    random_binary = ''.join([str(random.randint(0, 1)) for _ in range(4)])
    decimal = int(random_binary, 2)
    return random_binary, decimal


# Function to sum the first 50 Fibonacci sequences
def sum_fibonacci():
    fib_sequence = [0, 1]
    for i in range(2, 50):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return sum(fib_sequence)


# Testing the functions
print("Mean Color:", mean_color(colors))
print("Mode Color:", mode_color(colors))
print("Median Color:", median_color(colors))
print("Color Variance:", color_variance(colors))
print("Probability of Choosing Red Color:", red_probability(colors))
save_to_database(colors)
print("Recursive Search:", recursive_search([1, 2, 3, 4, 5], 3))
print("Random Binary Number and its Decimal Equivalent:", generate_and_convert())
print("Sum of First 50 Fibonacci Sequences:", sum_fibonacci())
