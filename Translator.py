import googletrans
from googletrans import Translator


translator = Translator()

phase = """
How to win friends and influence people - Dale Carnigie 

You can Negotiate Anything - Herb Cohen 

The Millionare next door - Tomas J Stanly

Predictably Irrational - Dan Ariely 

Tough Time Never Last But Tough People Do - Robert Schuller 

Think and Grow Rich - Napoleon Hill 

7 Habits of Highly Effective People - Stephen Covey 

Why you act the way you do - Tim Lahaye 

Rich Dad Poor Dad - Robert Kiyosaki 

The Richest Man in Babylon - George S Clason 
"""

result = translator.translate(phase, dest='japanese')
print(result.text)


""" Examples for Applications of the above liabrary """
"""
print(googletrans.LANGUAGES)
print(result.src)
print(result.dest)
print(result.origin)

print(result.pronunciation)

print()
Phrase = 'Abhay is a good person'
result = translator.translate(Phrase, dest='fr')
print(result.text)
result = translator.translate('Abhay est une personne formidable', dest='en')
print(result.text)
"""