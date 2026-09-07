from tkinter import *
import requests

pontos = 0
janela = Tk()
janela.title("CHECKLIST DO DIA")
texto_saudações = Label(janela, text="0lá, como você está?")
texto_saudações.grid(column=0, row=0)

print("====CHECKLIST DO DIA ====")

Saudações = "0lá, como você está?"
Saudações = input(Saudações).strip().lower()


if Saudações == "bem":
    print("Ótimo, vamos ás perguntas de hoje.")
else:
    print("Que pena, espero que tudo melhore, vamos ás perguntas de hoje")
    


pergunta_1 = "Você tomou café da manhã hoje?"
pergunta_1 = input(pergunta_1).strip().lower()


if pergunta_1 == "sim":
    print("Parabéns, vamos para a próxima pergunta.")
else:
    print("Que pena, vamos tentar recuperar na próxima")
if pergunta_1 == "sim":
    pontos += 1


pergunta_2 = "Você almoçou hoje?"
pergunta_2 = input(pergunta_2).strip().lower()


if pergunta_2 == "sim":
    print("É isso aí, saco vazio não para em pé! Vamos para a próxima pergunta.")
else:
    print("Cuidado em, não é recomendado ficar mutias horas sem comer, vamos tentar recuperar na próxima")
if pergunta_2 == "sim":
    pontos +=1


pergunta_3 = "Você fez o lanche da tarde hoje?"
pergunta_3 = input(pergunta_3).strip().lower()


if pergunta_3 == "sim":
    print("Muito bem, essa refeição da tarde é essencial para o dia.")
else:
    print("Que pena, vamos tentar recuperar na próxima.")
if pergunta_3 == "sim":
    pontos +=1



pergunta_4 = "Você jantou hoje?"
pergunta_4 = input(pergunta_4).strip().lower()


if pergunta_4 == "sim":
    print("Boa!! É muito importante a janta para a saúde alimentar.")
else:
    print("Atenção em!! A janta é muito importante, cuidado nos próximos dias")
if pergunta_4 == "sim":
    pontos +=1




pergunta_7 = "Você furou a dieta hoje?"
pergunta_7 = input(pergunta_7).strip().lower()
if pergunta_7 == "não":
        pontos +=1
if pergunta_7 == "sim":
    pergunta_8 = "O que você errou?"
    pergunta_8 = input(pergunta_8).strip().lower()



pergunta_4_5 = "Hoje era dia de treino?"
pergunta_4_5 = input(pergunta_4_5).strip().lower()


if pergunta_4_5 == "sim":
    pergunta_5 = "Você treinou hoje?"
    pergunta_5 = input(pergunta_5).strip().lower()

    if pergunta_5 == "sim":

        pergunta_5_1 = "Você correu ou foi treinar?"
        pergunta_5_1 = input(pergunta_5_1).strip().lower()

        if pergunta_5_1 == "corri":
            pergunta_6_1 = "Quanto tempo correndo?"
            pergunta_6_1 = float(input(pergunta_6_1,))

            pergunta_6 = "Quantos km você correu?"
            pergunta_6 = float(input(pergunta_6))

            pergunta_5_4 = "Quantas calorias você queimou?"
            pergunta_5_4 = int(input(pergunta_5_4))

        elif pergunta_5_1 == "treinei":
            pergunta_5_2 = "Qual foi o seu treino hoje?"
            pergunta_5_2 = input(pergunta_5_2).strip().lower()

            pergunta_5_3 = "Quanto tempo durou o seu treino?"
            pergunta_5_3 = float(input(pergunta_5_3))

            pergunta_5_4 = "Quantas calorias você queimou?"
            pergunta_5_4 = int(input(pergunta_5_4))

    elif pergunta_5 == "não":
        print("Cuidado, faltar treinos pode fazer falta lá na frente.")    
elif pergunta_4_5 == "não":
    print("Aí sim, hoje foi dia de descanso.")


if pergunta_4_5 == "sim":
    pontos +=1




porcentagem = (pontos / 6) * 100




print("====Resumo do dia====")

print("                ")

print("Você teve", porcentagem, "de acertos no seu dia")

print("                ")

if pergunta_4_5 == "não":
    print("Sem treinos hoje.")

elif pergunta_4_5 == "sim":

    if pergunta_5 == "não":
        print("Você não treinou hoje.")
    elif pergunta_5 == "sim":
        if pergunta_5_1 == "corri":
            print(f"O treino de hoje foi uma corrida de {pergunta_6} km")
        elif pergunta_5_1 == "treinei":
            print(f"O treino do dia foi de {pergunta_5_2}")

if pergunta_7 == "sim":
    print("Erros do dia:", pergunta_8)
elif pergunta_7 == "não":
    print("Parabéns!!Você não furou a dieta")





janela.mainloop()
