
import random

pedra_papel_tesoura = (1,"Pedra", "Papel", "Tesoura")

def validar_jogada_do_usuario():
  
  global jogada_do_usuario
  
  while not type(jogada_do_usuario) == int: 
    try:
      jogada_do_usuario = int(jogada_do_usuario)
      break
    except:
      print("\nDigite um dos valores abaixo pfv\n")
      jogada_do_usuario = input("Para sair digite 4\nEscolha pedra (1), papel (2) ou tesoura (3): ")
  print()

def compara_jogadas_imprime_resultados():
  
  global jogada_do_usuario, jogada_da_maquina

  if jogada_do_usuario == jogada_da_maquina:
    print(f"Os dois jogaram {pedra_papel_tesoura[jogada_da_maquina].upper()}\n\ndeu EMPATE")

  else:

    if jogada_do_usuario == 1 and jogada_da_maquina == 3:
      jogada_do_usuario += 3

    if jogada_da_maquina == 1 and jogada_do_usuario == 3:
      jogada_da_maquina +=3

    indice_para_format_usuario = 1 if jogada_do_usuario == 4 else jogada_do_usuario 

    indice_para_format_maquina = 1 if jogada_da_maquina == 4 else jogada_da_maquina 

    if jogada_do_usuario > jogada_da_maquina:
      
      print("Você jogou {},\nO adversario jogou {}".format(

        pedra_papel_tesoura[indice_para_format_usuario].upper(),

        pedra_papel_tesoura[indice_para_format_maquina].upper()

      ))

      print("{} ganha de {},\n\nVocê Ganhou".format(
        
        pedra_papel_tesoura[indice_para_format_usuario],
        
        pedra_papel_tesoura[indice_para_format_maquina]))

    else:

      print("Você jogou {},\nO adversario jogou {}".format(

        pedra_papel_tesoura[indice_para_format_usuario].upper(),

        pedra_papel_tesoura[indice_para_format_maquina].upper()

      ))

      print("{} ganha de {},\n\nVocê Perdeu".format(
        
        pedra_papel_tesoura[indice_para_format_maquina],

        pedra_papel_tesoura[indice_para_format_usuario]))

  print("---------------------------------\n")


while True:
  
  jogada_da_maquina = random.randint(1,3)

  jogada_do_usuario = input("Para sair digite 4\nEscolha pedra (1), papel (2) ou tesoura (3): ")
  
  validar_jogada_do_usuario()

  if jogada_do_usuario == 4: break

  compara_jogadas_imprime_resultados()

print("\nJogo fechado.")

# usei espaços um tanto quanto desnecessariamente grandes para que ficasse mais claro de ler ja que eu estava me confundino demais