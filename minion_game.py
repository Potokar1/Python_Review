# Note: string s will only contain uppercase letters]
# This is a sub-string counting game.
# The perfect stdlib method for this is count(substring) -> returns number of occurences

# examines every substring of string, giving points to stuart or kevin based on ruleset.


def minion_game(string):
    a = 'Stuart'
    b = 'Kevin'
    a_score = 0
    b_score = 0
    str_len = len(string)
    for starting_letter in range(str_len):
        for last_letter in range(starting_letter, str_len):
            # print(starting_letter, last_letter) -> used to debug my program, found I was not increasing my end index each repetition string[2:0] = error!
            # print(string[starting_letter:last_letter+1])
            substr = string[starting_letter:last_letter+1]
            # print(is_vowel(substr[0]))
            if(is_vowel(substr[0])):
                b_score += 1
            else:
                a_score += 1
    if a_score > b_score:
        print(a, a_score)
    elif b_score > a_score:
        print(b, b_score)
    else:
        print('Draw')


def is_vowel(string):
    is_vowel = False
    if string == 'A' or string == 'E' or string == 'I' or string == 'O' or string == 'U':
        is_vowel = True
    return is_vowel


str = 'BANANANAAAS'
#str = str(input())
minion_game(str)
