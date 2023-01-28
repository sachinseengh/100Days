import random
word_list=["sachin","kumar","singh"]

choosen_word=random.choice(word_list)
length_of_choosen_word=len(choosen_word)


guess=input("Enter your guess\n").lower()


for n in choosen_word:
    if(n== guess):
        print("its present in choosen word")

# Watch it later 