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
    def __init__(self, item_id, quantidade_pedida):
        self.item_id = item_id
        self.quantidade_pedida = quantidade_pedida
        super().__init__(f" ")

    