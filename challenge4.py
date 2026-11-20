user_input = input("Enter a sentence: ")
words = user_input.split()
print("Number of words", len(words))

reverse_sentence = " ".join(reversed(words))
print("Reversed sentence:", reverse_sentence)

user_input = user_input.replace(" ", "-")
print("Modified sentence:", user_input)
