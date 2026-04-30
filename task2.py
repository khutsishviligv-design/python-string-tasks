#დავალების აღწერა:
#1. ინიციალების ამომღები (Initials Extractor) მომხმარებელს სთხოვე სრული სახელი (მაგალითად: "Ada Lovelace"). ამოიღე სახელის პირველი ასო და გვარის პირველი ასო. დაბეჭდე ისინი დიდი ასოებით (uppercase) f-string-ის გამოყენებით, მაგალითად: "Your initials are: A. L." 2. სიტყვის შემობრუნება (Reverse Word) მომხმარებელს სთხოვე ერთი სიტყვა. დაბეჭდე ეს სიტყვა შებრუნებულად slicing-ის გამოყენებით: word[::-1]. 3. მომხმარებლისგან მიიღე წინადადება (input()-ით). ასევე სთხოვე ორი სიტყვა: რომელი სიტყვა უნდა შეიცვალოს რით უნდა შეიცვალოს გამოიყენე .replace() მეთოდი, რომ წინადადებაში პირველი სიტყვა შეცვალო მეორეთი. დაბეჭდე განახლებული წინადადება.#



# 1. Initials Extractor
full_name = input("Enter your full name: ") #magalitad. ada lovelave
parts = full_name.split()

first_initial = parts[0][0].upper()
last_initial = parts[-1][0].upper()

print(f"Your initials are: {first_initial}. {last_initial}.")

# 2. Reverse Word
word = input("Enter a word: ")
print("Reversed word:", word[::-1])

# 3. Sentence Replace
sentence = input("Enter a sentence: ")
old_word = input("Which word should be replaced? ")
new_word = input("What should it be replaced with? ")

updated_sentence = sentence.replace(old_word, new_word)
print("Updated sentence:", updated_sentence)

