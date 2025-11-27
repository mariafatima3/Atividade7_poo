# 3) Simulador de API (Exceção Customizada)
# Enredo: Você está consumindo uma API externa que pode falhar. Para tornar seu código robusto, você quer criar uma exceção específica para quando a API estiver fora do ar.
# Tarefa: Crie sua Exceção: Defina uma nova classe chamada ApiForaDoArError que herda de Exception. (Pode ser simples: class ApiForaDoArError(Exception): pass).
# Crie o Simulador: Crie uma função buscar_dados_usuario(id_usuario).
# Dentro dela, simule uma falha. Se o id_usuario == 0, levante (raise) a sua exceção customizada: raise ApiForaDoArError("A API parece estar offline.")
# Se o id_usuario for qualquer outro, retorne um dicionário simulado: {'id': id_usuario, 'nome': 'Usuário Teste'}.
# Crie o Tratador: No código principal, peça ao usuário um id.
# Chame a função buscar_dados_usuario() dentro de um bloco try.
# Adicione um except ApiForaDoArError as e que imprima: f"Erro de Conexão: {e}. Por favor, tente mais tarde."
# Adicione um bloco else que imprima os dados do usuário caso a busca seja bem-sucedida.


class ApiForaDoArError(Exception):
    pass

def buscar_dados_usuario(id_usuario):
    if id_usuario == 0:
        raise ApiForaDoArError("A API parece estar offline.")
    return {'id': id_usuario, 'nome': 'Usuário Teste'}

entrada = input("Digite o ID do usuário: ")

try:
    id_input = int(entrada)
    dados = buscar_dados_usuario(id_input)
except ValueError:
    print("Entrada inválida! Digite um número inteiro.")
except ApiForaDoArError as e:
    print(f"Erro de Conexão: {e}. Por favor, tente mais tarde.")
else:
    print(f"Dados do usuário encontrados: {dados}")

