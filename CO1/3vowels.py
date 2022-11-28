list_words = ["red", "green", "yellow", "blue", "orange", "purple", "black", "white", "brown", "pink"]
list_vowels = [i for x in list_words for i in x if i in "aeiou"]
print("All words ", list_words)
print("Vowel words ", list_vowels)