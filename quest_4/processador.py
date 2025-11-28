# 4) Processador de Pedidos de E-commerce. Enredo: Em um sistema de e-commerce, uma função processar_pedido verifica o estoque antes de confirmar um pedido. 
# Uma exceção customizada deve ser usada para estoque insuficiente, e um finally deve registrar um log da tentativa.
# Tarefa: Crie a Exceção: Defina uma classe EstoqueInsuficienteError(Exception). Crie a Função: Defina processar_pedido(item_id, quantidade_pedida).
# Simule um estoque: estoque_atual = {'item1': 10, 'item2': 5}. Verifique se item_id existe no estoque. Se não, raise KeyError(f"Item {item_id} não encontrado.").
# Verifique se quantidade_pedida > estoque_atual[item_id]. Se sim, raise EstoqueInsuficienteError(f"Estoque insuficiente para {item_id}.").
# Se passar, imprima: "Pedido Aprovado! Estoque atualizado." Crie o Tratador: Chame processar_pedido('item1', 15) (para forçar o erro de estoque) dentro de um try.
# Capture KeyError e imprima: "Erro de Pedido: Item não cadastrado." Capture EstoqueInsuficienteError e imprima: "Erro de Lógica: {e}"
# Capture Exception genérico para outros problemas. Adicione um finally que sempre imprima: "LOG: Tentativa de processar pedido finalizada." 
# (Simulando um log que sempre deve ocorrer).

class EstoqueInsuficienteError(Exception):
    """Exceção customizada para estoque insuficiente."""
    pass

estoque_atual = {'item1': 10, 'item2': 5}

def processar_pedido(item_id, quantidade_pedida):
    """
    Processa um pedido, verificando o estoque e levantando exceções se necessário.
    """
    if item_id not in estoque_atual:
        raise KeyError(f"Item {item_id} não encontrado.")

    if quantidade_pedida > estoque_atual[item_id]:
        raise EstoqueInsuficienteError(
            f"Estoque insuficiente para {item_id}. "
            f"Pedido de {quantidade_pedida}, disponível: {estoque_atual[item_id]}"
        )

    print("Pedido Aprovado! Estoque atualizado.")

print("\n--- Testando cenário de estoque insuficiente ---")
try:
    processar_pedido('item1', 15)  
except KeyError as e:
    print(f"Erro de Pedido: Item não cadastrado. {e}")
except EstoqueInsuficienteError as e:
    print(f"Erro de Lógica: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("LOG: Tentativa de processar pedido finalizada.")

print("\n--- Testando cenário de item não encontrado ---")
try:
    processar_pedido('item3', 1)  
except KeyError as e:
    print(f"Erro de Pedido: Item não cadastrado. {e}")
except EstoqueInsuficienteError as e:
    print(f"Erro de Lógica: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("LOG: Tentativa de processar pedido finalizada.")

print("\n--- Testando cenário de pedido aprovado ---")
try:
    processar_pedido('item2', 3) 
except KeyError as e:
    print(f"Erro de Pedido: Item não cadastrado. {e}")
except EstoqueInsuficienteError as e:
    print(f"Erro de Lógica: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("LOG: Tentativa de processar pedido finalizada.")
