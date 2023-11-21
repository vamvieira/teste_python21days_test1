import sqlite3

from Class.conta_pessoal import ContaPessoal

conta_wilson = ContaPessoal("Wilson", "Lacerda")
conta_vitor = ContaPessoal("Vitor", "Magalhães")

con = sqlite3.connect("DB/conta_pessoal.db")
cursor = con.cursor()

#"cursor.fetchall" retorna todas as linhas da descricao onde as trasacoes sejam do user de id 1, no caso Wilson
cursor.execute("SELECT descricao, valor FROM transacoes WHERE pessoa_id = 1")
transacoes = cursor.fetchall()

# Para cada transacao em trasacoes as descriçao e o valor equivale a transação, ou seja transacao recebe as duas variáveis.
for transacao in transacoes:
    tipo, valor = transacao
    if valor > 0:
        conta_wilson.adicionar_renda(tipo, valor)
    else:
        conta_wilson.adicionar_despesa(tipo, valor)

print(conta_wilson.cadastrar_transacoes())

con.close()