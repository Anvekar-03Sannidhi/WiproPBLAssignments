file = open("sample.txt", "r")

lines = file.readlines()

line_count = len(lines)

# Find meeting time
if line_count <= 12:
    print("Meeting time:", line_count, "AM")
else:
    print("Meeting time:", line_count - 12, "PM")


file.seek(0)
text = file.read()

text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.replace("(", " ")
text = text.replace(")", " ")
text = text.replace("-", " ")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

max_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        max_word = word

print("Meeting place:", max_word + " Street")

file.close()