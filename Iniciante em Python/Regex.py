import re

Musica = '''
Hey Travis Scott, h-h-hey Trav
You know what the fuck up, nigga
Know what I'm talkin' bout?
Nigga, one thing for sure
Two things for certain, nigga
We gon' keep drinking this motherfucking lean, nigga
And wearin' these motherfuckin' rockstar jeans, nigga
They want what a nigga can't stand

I know what they can't stand
I know why they mad, nigga
Know what I'm talkin' 'bout
But we don't give a fuck
We gon' keep this big ass Mac 11 on deck
If any fuck nigga get out of line
If any fuck nigga want do somethin' nigga we can do it nigga
Know what I'm talkin' 'bout

Coordinate the tan with the beans in my Rockstar skinnies
I'ma need some more, need some more, if I really wanna feel it
Yah, yah, yah, yah, yah
Spend that money fast if I have to
Make that money back if I had you

Coordinate the tan with the beans in my Rockstar skinnies (straight up!)
Coordinate the xan with the lean in my Rockstar skinnies (yeah, yeah)
Coordinate the tan with the beans in my Rockstar skinnies (yeah, yeah)
Yah, yah, yah, yah, yah '''

# Crie um REGEX para contar quantas vezes o caracter 'Coordinate' aparece na música.

results = r"\bCoordinate\b"
chamadas = len(re.findall(results, Musica, re.IGNORECASE))
print(f"A palavra 'Coordinate' aparece {chamadas} vezes na música.")

# Crie um REGEX para contar quantas vezes a palavra skinnies aparece na música.

results2 = re.findall(r"\ skinnies\b", Musica)
contador = len(results2)
print("A palavra 'skinnies' aparece", contador, "vezes na música")

# Crie um REGEX para extrair as palavras seguidas por  ( , )

padr = r"\b\w+(?=,)"
expres = re.findall(padr, Musica)
print(expres)

