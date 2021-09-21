'''
Oppgave 4: Å telle bokstaver og ord
'''

#4.1
def char_count(word):
    '''
    Fungerer kun med enkeltord, ikke setninger.
    '''
    return len(word.strip())

#4.2
def word_dict(sentence):
    words = dict()
    sentence = sentence.strip().lower().split()
    word_amount = len(sentence)
    for word in sentence:
        words[word] = 0
        for repeated_word in sentence:
            if repeated_word == word:
                words[word] += 1   
        
    return words, word_amount

#4.3
def main():
    user_in = input("Skriv en setning: ")

    words, word_amount = word_dict(user_in)

    print(f"Det er {word_amount} ord i setningen din.")

    for key, val in words.items():
        chars = char_count(key)

        print(f"Ordet \"{key}\" forekommer {val} ganger, og har {chars} antall bokstaver.")

    
main()