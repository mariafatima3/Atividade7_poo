# 1) Calculadora de Média Robusta: # Enredo: Você está criando um script que calcula a média de notas de um aluno. O usuário deve digitar duas notas (N1 e N2). 
# Tarefa: Peça ao usuário que digite duas notas (valores de 0 a 10). Use um bloco try para converter as entradas em float.
# Se a conversão falhar (ex: usuário digitou "cinco"), capture o ValueError e mostre a mensagem: "Erro: As notas devem ser valores numéricos." 
# No mesmo bloco try, calcule a média (n1 + n2) / 2. Adicione um bloco else que será executado apenas se o try for bem-sucedido. 
#  Este bloco deve imprimir a média calculada (ex: "A média é 7.5"). Desafio (opcional): Adicione uma validação dentro do try para verificar se as notas estão entre 0 e 10. 
# Se não estiverem, use raise ValueError("A nota deve estar entre 0 e 10.") e veja como o seu except captura esse erro. 

while True:
    n1 = input("Digite a primeira nota (0 a 10): ")
    n2 = input("Digite a segunda nota (0 a 10): ")

    try:
        n1 = float(n1.replace(",", "."))
        n2 = float(n2.replace(",", "."))

        if not (0 <= n1 <= 10) or not (0 <= n2 <= 10):
            raise ValueError("As notas devem estar entre 0 e 10.")

        media = (n1 + n2) / 2

    except ValueError as e:
        print("Erro:", e)
        print("Tente novamente.\n")
        continue  

    else:
        print(f"A média é {media}")
        break  
