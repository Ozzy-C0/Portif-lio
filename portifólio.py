# UNIP ADS : python aula 1 ( essa aula insina o uso de variaveis e o uso do input e print, e formatações como "\n" e f" ' )
'
nome = input("escreva seu nome: ")
print("olá ", nome)
'

# UNIP ADS : python aula 2 ( essa aula ensinou a usar laços de repetição como while e for tambem usando if elif e else )
'
while True:
  saida = input("agora estamos em loop oque vc acha ?: ")
  if saida != "dahora":
    print("SIM!")
    
  else:
    break
'

# UNIP ADS : Pyton aula 3 ( essa aula e o uso e criação de listas )

'
lista = []
while True:
  item = input("agora temos uma lista, deseja adicionar algo ?\n ou escreva sair: ")
  
  if item.lowwer() == "sair":
    break

  elif item:
    lista.append(item)
    print(f"item adicionado a lista '{item}'")

  else:
    print("não digitou nada ?")

print(f"'{lista}' aqui esta sua lista final")
'
