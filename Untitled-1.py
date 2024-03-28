print("bem vindo ao quiz")
answer_user = input("quer começar S/N ")

if answer_user != "S":
    quit()

print("Começando...")
print("Quem é o Rei do futebol? \n (A) Pelé \n (B) maradona \n (C) garrincha \n (D) zico \n")
answer_1 = input("Resposta: ")
if answer_1 == "A":
   print("Correto!")
else:
   print("Incorreto!")

print("Quem é o melhor jogador de futebol argentino ? \n (A) Riquelme \n (B) Maradona \n (C) Messi \n (D) Batistuta" )
answer_2 = input(" Resposta: ")
if answer_2 == "C":
   print("Correto")
else:
   print("Incorreto")   

   print("Quem atacou a Ucrania ? \n (A) Alemanha \n (B) USA \n (C) China \n (D) Russia  ")
answer_3 = input("Resposta")
if answer_3 == "D":
   print("Correto")
else:
   print("Incorreto")      
