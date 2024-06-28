def checkVowel(char):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return char in vowels
def counVowelAndConsonant(string):
    countV = 0
    countC = 0
    i = 0
    if string == '': return 0
    for i in string:
        if i.islower(): return 0
    for i in range(len(string)):
        if string == '':
            break
        for j in range(i, len(string)):
            if checkVowel(string[i]):
                countV += 1
            else:
                countC += 1
    return max(countV, countC)
def main():
    string = input('Enter a string: ')
    print(counVowelAndConsonant(string))
main()