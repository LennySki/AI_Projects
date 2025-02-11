with open ("pride_and_prejudice.txt", "r") as file:
	text = file.read().lower()
words = text.split()
love_count = words.count("love")
print(f"The word 'love' appears {love_count} times.")
