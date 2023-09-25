Nome = input('Digite seu nome')
Nome = Nome.lower()
Nome = Nome.title()
print(Nome)

idade = int(input('Digite sua idade'))
print (idade)

prova1 = int(input('digite a nota da prova 01'))
prova2= int(input('digite a nota da prova 02'))

if (prova1+prova2)/2 >= 6 and idade >= 18:
    print('Parabens {x}, voce passou'.format(x=Nome))
else:
    print('Parabens {x}, voce reprovou'.format(x=Nome))