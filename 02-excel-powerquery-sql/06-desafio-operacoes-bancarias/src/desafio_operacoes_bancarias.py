entrada = input().strip()


def descrever_uso(nome):
    if nome == "Relatorio de juros em planilha Excel":
        return "Calculo de juros sobre saldos usando colunas da planilha"

    elif nome == "Tabela de clientes com limite de credito":
        return "Lista dados de clientes e campo com limite de credito"

    elif nome == "Consulta SQL de saldo por cliente":
        return "Filtra tabela de contas para mostrar saldo de cada cliente"

    elif nome == "Consulta SQL de historico de transacoes":
        return "Usa SQL para buscar transacoes antigas de uma conta"

    else:
        return "Tecnica desconhecida"


print(descrever_uso(entrada))