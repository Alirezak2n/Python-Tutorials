original = input("please insert a sentence: ").lower().strip()
words = original.split() #split joda konande kalamat az ham dar list

new_words=[]

for w in words:
    if w[0] in "aeiou":
        new_word=w+ "yay" #ye bakhsh be kalame ezafe mikone
        new_words.append(new_word) #kalame jadid ro mibare tu list
    else:
        vowel_pos=0
        for letter in w:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break  #mindaze az loop birun
                continue #vel mikone edame loop ro va mire az bala
        cons = w[:vowel_pos]
        the_rest=w[vowel_pos:]
        new_word= the_rest + cons + "ay"
        new_words.append(new_word)
        
        
print(" ".join(new_words)) #join kalamat ro be ham michasbune
