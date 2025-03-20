text = "I love chocolate very much"
words = text.split()

with open("output.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

