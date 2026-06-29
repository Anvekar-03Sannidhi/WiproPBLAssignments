def ispalindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False


def count_the_vowels(name):
    count = 0

    for ch in name:
        if ch.lower() in "aeiou":
            count = count + 1
    return count


def frequency_of_letters(name):
    freq = {}

    for ch in name:
        if ch != " ":
            if ch in freq:
                freq[ch] = freq[ch] + 1
            else:
                freq[ch] = 1
    return freq