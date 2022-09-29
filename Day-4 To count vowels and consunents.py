def vowelsConsonants(string):
   vowels = [each for each in string if each in "aeiouAEIOU"]
   print('Number of vowels:',vowels)
   consonants = [each for each in string if each not in "aeiouAEIOU "]
   print('Number of consonants:',consonants)
string = input('Enter any string: ')

vowelsConsonants(string)
