import sqlite3

con = sqlite3.connect("conta_pessoal.db")
cursor = con.cursor()

# Criação da seguintes tabelas: cadastro_pessoas, tipo_transacoes e transacoes

cadastro_pessoas = '''CREATE TABLE IF NOT EXISTS cadastro (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    sobrenome TEXT NOT NULL
                )'''
cursor.execute(cadastro_pessoas)

transacoes = '''CREATE TABLE IF NOT EXISTS transacoes (
                    id INTEGER PRIMARY KEY,
                    pessoa_id INTEGER NOT NULL,
                    descricao TEXT NOT NULL,
                    valor REAL NOT NULL,
                    FOREIGN KEY (pessoa_id) REFERENCES cadastro (id)
                )'''

cursor.execute(transacoes)

tipo_transacoes = '''CREATE TABLE IF NOT EXISTS tipo_transacoes (
                    id INTEGER PRIMARY KEY,
                    descricao TEXT NOT NULL
                )'''

cursor.execute(tipo_transacoes)

# Inserindo a tabela tipo_transacoes e seus valores chaves.

insert_name_sobrename = '''INSERT INTO cadastro (nome, sobrenome) VALUES ("Wilson", "Lacerda")'''

cursor.execute(insert_name_sobrename)

values_descricao = '''INSERT INTO tipo_transacoes (descricao) VALUES ("Salário", "Bolsa", "Gorjeta", "PIX Misterioso")'''

cursor.execute(values_descricao)

con.commit()

# Inserindo valores ficticios (ID DO USER, DESCRICAO, VALOR) Uma lista de Tupla

insere_salario = '''INSERT INTO transacoes (pessoa_id, descricao, valor) VALUES (1, "Salário", 17500.0))'''

cursor.execute(insere_salario)

insere_bolsa = '''INSERT INTO transacoes (pessoa_id, descricao, valor) VALUES (1, "Bolsa", 500.0))'''

cursor.execute(insere_bolsa)

insere_gorjeta = '''INSERT INTO transacoes (pessoa_id, descricao, valor) VALUES (1, "Gorjeta", 15.0))'''

cursor.execute(insere_gorjeta)

insere_pix = '''INSERT INTO transacoes (pessoa_id, descricao, valor) VALUES (1, "PIX Misterioso", 1500.0))'''

cursor.execute(insere_pix)

con.commit()

#Despesas

insere_conta = '''INSERT INTO transacoes (pessoa_id, descricao, valor) VALUES (1, "conta de luz", -100.0))'''

cursor.execute(insere_conta)

insere_fralda = '''INSERT INTO transacoes (pessoa_id, descricao, valor) VALUES (1, "fralda do bebê", -50.0))'''

cursor.execute(insere_fralda)

con.commit()

con.close()