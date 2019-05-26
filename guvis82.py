s=input()
vowel=set('aeiou')
if not vowel.isdisjoint(s):
    print("yes")
else:
    print("no")