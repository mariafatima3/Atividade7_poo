# 2) Validador de Senha com raise Objetivo: Praticar o uso de raise para aplicar regras de negócio.
# Enredo: Você está implementando o back-end de um formulário de cadastro. A função validar_senha deve garantir que a senha fornecida atende aos critérios mínimos de segurança.
# Tarefa: Crie uma função validar_senha(senha). Dentro da função, verifique as seguintes regras de negócio: 
# Se len(senha) < 8, levante (raise) um ValueError com a mensagem "A senha deve ter pelo menos 8 caracteres."
# Se a senha não contiver nenhum número (use any(c.isdigit() for c in senha)), levante (raise) um ValueError com a mensagem "A senha deve conter pelo menos um número."
# Se a senha passar por todas as validações, a função deve imprimir "Senha válida e cadastrada!"
# Fora da função, crie um loop while True que pede ao usuário para digitar uma senha.
# Chame validar_senha() dentro de um bloco try...except ValueError as e.
# Se um ValueError for capturado, imprima a mensagem de erro específica (print(e)) e o loop continua.
# Se a validação for bem-sucedida (sem exceções), imprima a mensagem de sucesso da função e quebre o loop (break).

def validar_senha(senha):
    
    if len(senha) < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")

    
    if not any(c.isdigit() for c in senha):
        raise ValueError("A senha deve conter pelo menos um número.")

    print("Senha válida e cadastrada!")


while True:
    senha = input("Digite uma senha: ")

    try:
        validar_senha(senha)
        break  
    except ValueError as e:
        print(e) 