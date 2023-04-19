agenda = {}
agenda['marcos']=32112232
agenda['fabio']=988887788
agenda['maria']=44554455 

def consulta(agenda, nome):
    if nome in agenda:
        return agenda[nome]
    return "Nome não encontrado na agenda."

print(consulta(agenda, 'marcos'))


def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone
    return agenda

print(adiciona(agenda, 'lucas', 44554466))


def verificaNome(pessoa, agenda):
    if pessoa in agenda.keys():
        return True
    else:
        return False

print('maria esta na agenda?')
print(verificaNome("maria", agenda))

print('damiao esta na agenda?')
print(verificaNome("damiao", agenda))

pessoa = 'marcos'
print('a string da variavel pessoa é uma chave da agenda?')
print(verificaNome(pessoa, agenda))


def conta_letras(palavra):
    contagens = {}
    for letra in palavra:
        if letra not in contagens:
            contagens[letra] = 1
        else:
            contagens[letra] += 1
    return contagens

print(conta_letras('abacaxi'))

agenda_melhorada = {
        'Andreia': {
            'email': 'andreia.gusmao@faculdadeimpacta.com.br',
            'telefones': [11999999999, 11888888888]
        }, 
        'Maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
        },
        'Arthur': {
            'telefones':[11999999999]     
        }
}

def email(agenda, nome):
    if "email" in agenda[nome]:
        return agenda[nome]["email"]
    else:
        return f'{nome} não tem email!'
            

print(email(agenda_melhorada, 'Maria'))

def telefonePrincipal(agenda, nome):
    return agenda[nome]["telefones"][0]

print(telefonePrincipal(agenda_melhorada, "Andreia"))

def semEmail(agenda):
    arr = []
    for pessoa in agenda.keys():
        if "email" not in agenda[pessoa]:
            arr.append(pessoa)
    return arr

print(semEmail(agenda_melhorada))