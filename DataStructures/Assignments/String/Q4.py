# Given a string, if the first or last character is 'x', return the string without those 'x'
# character, else return the string unchanged. If the input is "xHix", then output is "Hi".

text = "xHix"
if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]
print(text)
