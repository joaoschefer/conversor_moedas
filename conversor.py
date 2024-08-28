import requests
import psycopg2

def obter_precos():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados["rates"]

def converter_moedas(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem in taxas and moeda_destino in taxas:
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valor_em_usd = valor / taxa_origem
        valor_convertido = valor_em_usd * taxa_destino
        return valor_convertido
    else:
        return None

def salvar_conversao(valor, moeda_origem, moeda_destino, valor_convertido):
    try:
        conn = psycopg2.connect(
            dbname="python_cotacoes",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO conversoes (valor, moeda_origem, moeda_destino, valor_convertido)
            VALUES (%s, %s, %s, %s)
        """, (valor, moeda_origem, moeda_destino, valor_convertido))
        conn.commit()
        cur.close()
        conn.close()
        print("Informações salvas com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar informações: {e}")

def exibir_historico():
    try:
        conn = psycopg2.connect(
            dbname="python_cotacoes",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM conversoes")
        conversoes = cur.fetchall()
        if conversoes:
            print("\nHistórico de Conversões:")
            for conversao in conversoes:
                print(f"Valor: {conversao[1]} {conversao[2]} -> {conversao[4]} {conversao[3]}")
        else:
            print("Nenhuma conversão encontrada.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao recuperar histórico: {e}")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Converter moedas")
        print("2. Verificar histórico de conversões")
        print("3. Sair")
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            taxa_de_cambio = obter_precos()
            valor = float(input("Qual o valor a ser convertido? "))
            moeda_origem = input("Qual a moeda de origem? ").upper()
            moeda_destino = input("Qual a moeda de destino? ").upper()

            valor_convertido = converter_moedas(valor, moeda_origem, moeda_destino, taxa_de_cambio)

            if valor_convertido is not None:
                print(f"\n{valor:.2f} {moeda_origem} é equivalente a {valor_convertido:.2f} {moeda_destino}")
                salvar_conversao(valor, moeda_origem, moeda_destino, valor_convertido)
            else:
                print("Moedas não encontradas ou inválidas.")
        
        elif escolha == '2':
            exibir_historico()

        elif escolha == '3':
            print("Saindo...")
            break

        else:
            print("Escolha inválida. Tente novamente.")

# Iniciar o menu
menu()
