paragraph = """Every day brings new opportunities to learn, improve, and grow into a better 
version of yourself. Stay focused on the goals you set, trust the process, 
and believe in the strength you carry within. The journey may feel challenging,
but the effort you put in shapes the future you desire. Keep moving forward with
patience, embrace the lessons along the way, and remember that the smallest steps
can lead to the biggest achievements over time."""
para_list = paragraph.lower().split(" ")
char_count = 0
for word in para_list:
    if word == "the":
        char_count += 1
print(f"The word 'the' appears {char_count} times in the paragraph.")