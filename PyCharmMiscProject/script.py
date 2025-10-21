

print("Val de cutremure de suprafata in Romania:8 seisme in cateva zile.S-a auzit un zgomot puternic, ca de explozie.Ce spun specialistii. ")
text= "Val de cutremure de suprafata in Romania:8 seisme in cateva zile.S-a auzit un zgomot puternic, ca de explozie.Ce spun specialistii. "
import string
jumatate = len(text)//2
prima_jumatate=text[:jumatate].strip().upper()
a_doua_jumatate=text[jumatate:].capitalize()[::-1]
a_doua_jumatate:"-a auzit un zgomot puternic, ca de explozie.ce spun specialistii."
fara_punctuatie = ''.join(ch for ch in a_doua_jumatate if ch not in string.punctuation)

a_doua_jumatate = fara_punctuatie

print(a_doua_jumatate)

print("Prima jumatate:",prima_jumatate)
print("A doua jumatate:",a_doua_jumatate)
rezultat=prima_jumatate+a_doua_jumatate
print(rezultat)




