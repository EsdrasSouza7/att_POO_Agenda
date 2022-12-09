test = {'a': '1', 'b': '2'}
if 'a' in test:
    print(test['a'])
else:
    print('NO')
test['Esdras'] = '7'
test['Paulo'] = '8'
test['Palito'] = '9'
expressao = '7'
# for palavra in list(test.keys()):
#     T = len(palavra)
#     N = len(expressao)
#     for letras in range(len(palavra)):
#         if (len(palavra) - letras) < len(expressao):
#             break
#         else:
#             a = palavra[letras:letras+N]
#             if a == expressao:
#                 pass
for contatos in list(test.values()):
    T = len(contatos)
    N = len(expressao)
    for numeros in range(len(contatos)):
        if (len(contatos) - numeros) < len(expressao):
            break
        else:
            a = contatos[numeros:numeros+N]
            if a == expressao:
                pass



