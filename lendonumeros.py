# Solicitar ao usuário que insira um número entre 0 e 9999
num = int(input('Informe um número: '))
n = str(num).zfill(4)  # Garantir que o número tenha 4 dígitos, completando com zeros à esquerda, se necessário

# Exibir o número analisado
print('Analisando o número {}'.format(n))

# Exibir cada um dos dígitos separados

print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

num = int(input('Informe um número: '))

u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
