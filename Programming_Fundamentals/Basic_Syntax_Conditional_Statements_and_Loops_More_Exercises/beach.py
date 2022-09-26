word = input()
substrings_counter = 0
word_lower = word.lower()

substrings_counter += word_lower.count("fish")
substrings_counter += word_lower.count("sun")
substrings_counter += word_lower.count("sand")
substrings_counter += word_lower.count("water")

print(substrings_counter)