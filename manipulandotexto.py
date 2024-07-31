# Solicitar ao usuário que insira seu nome
nome = input('Qual é o seu nome? ').strip()

# Exibir informações sobre o nome
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

# Dividir o nome em palavras e contar as letras do primeiro nome
primeiro_nome = nome.split()[0]
print('Seu primeiro nome é "{}" e ele tem {} letras'.format(primeiro_nome, len(primeiro_nome)))

cidade = str(input('Em qual cidade você nasceu?'))

if cidade == 'Mossoró':
    print('EAE MEU PATRÃO')
else:
    print(cidade[0:5] == 'Santo')
#outra maneira de fazer o código para verificar se a cidade em q nasceu começa com Santo

cid = str(input('Onde nasceu? ')).strip()
print(cid[:8].upper() == 'MOSSORÓ')

#Verificando se existe o nome Rebouças em qualquer lugar no nome

name = str(input('Qual o seu nome? ')).strip()
print('Seu nome tem Rebouças? {}'.format('REBOUÇAS' in name.upper()))

######################Contagem de letras A numa frase de formas diferentes

# Solicitar ao usuário que insira uma frase
frase = str(input('Digite uma frase: ')).strip()

# Converter a frase para minúsculas para garantir que todas as letras 'a' sejam contadas, independentemente de maiúsculas ou minúsculas
frase_lower = frase.lower()

# Contar quantas vezes a letra 'a' aparece na frase
contagem_a = frase_lower.count('a')

# Encontrar a posição da primeira ocorrência da letra 'a'
pos_primeira_a = frase_lower.find('a') + 1  # Adiciona 1 para converter de índice para posição

# Encontrar a posição da última ocorrência da letra 'a'
pos_ultima_a = frase_lower.rfind('a') + 1  # Adiciona 1 para converter de índice para posição

# Exibir os resultados
print(f"A letra 'A' aparece {contagem_a} vezes na frase.")
print(f"A primeira letra 'A' aparece na posição {pos_primeira_a}.")
print(f"A última letra 'A' aparece na posição {pos_ultima_a}.")

######################Segunda forma

# Solicitar ao usuário que insira uma frase
frase = str(input('Digite uma frase: ')).strip()

# Converter a frase para minúsculas para garantir que todas as letras 'a' sejam contadas, independentemente de maiúsculas ou minúsculas
frase_lower = frase.lower()

# Contar quantas vezes a letra 'a' aparece na frase
contagem_a = frase_lower.count('a')

# Encontrar a posição da primeira ocorrência da letra 'a'
pos_primeira_a = frase_lower.find('a')

# Encontrar a posição da última ocorrência da letra 'a'
pos_ultima_a = frase_lower.rfind('a')

# Exibir os resultados
print(f"A letra 'A' aparece {contagem_a} vezes na frase.")
print(f"A primeira letra 'A' aparece na posição {pos_primeira_a}.")
print(f"A última letra 'A' aparece na posição {pos_ultima_a}.")

# Solicitar ao usuário que insira uma frase
frase = str(input('Digite uma frase: ')).strip()

# Remover espaços da frase
frase_sem_espacos = frase.replace(' ', '')

# Converter a frase para minúsculas para garantir que todas as letras 'a' sejam contadas, independentemente de maiúsculas ou minúsculas
frase_lower = frase_sem_espacos.lower()

# Contar quantas vezes a letra 'a' aparece na frase
contagem_a = frase_lower.count('a')

# Encontrar a posição da primeira ocorrência da letra 'a'
pos_primeira_a = frase_lower.find('a')

# Encontrar a posição da última ocorrência da letra 'a'
pos_ultima_a = frase_lower.rfind('a')

# Exibir os resultados
print(f"A letra 'A' aparece {contagem_a} vezes na frase.")
print(f"A primeira letra 'A' aparece na posição {pos_primeira_a}.")
print(f"A última letra 'A' aparece na posição {pos_ultima_a}.")

# Solicitar ao usuário que insira seu nome completo
nomecompleto = str(input('Digite seu nome completo: ')).strip()

# Dividir o nome completo em uma lista de palavras
nomes = nomecompleto.split()

# Exibir o primeiro e o último nome
print('Prazer em conhecê-lo {}'.format(nomecompleto))
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu último nome é: {}'.format(nomes[-1]))










