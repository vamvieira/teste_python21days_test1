"""Crie uma classe chamada "ContaPessoal". Ela possui as propriedades "nome", "sobrenome", 
"receita" e "despesas", e também possui os métodos "renda_total", "despesa_total",
"informacao_conta", "adicionar_renda", "adicionar_despesa"  e "saldo_conta". 
"Receita" é o dinheiro recebido e pode ter descrições (exemplo: salario, bolsa, gorjeta, etc.). 
O mesmo se aplica às despesas.
A aplicação deve conter 3 tabelas (banco de dados local): um de cadastro da pessoa, outra de transações, e outra de tipo de transações."""

#squlite é uma biblioteca que podemos criar um BD, craindo um arquivo pequeno, para rodar em aplicações.

class ContaPessoal:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.transacoes = []
        self.receita = []
        self.despesas = []
        self.saldo = 0

#Minha ideia é criar uma função chamada adicionar renda onde o cliente consegue entrar 
# e escolher qual o tipo da renda ele deseja colocar, para filtrar depois onde ele ganhou mais dinheiro

    def cadastrar_transacoes(conta):
        while True:
            print("\n1. Adicionar Renda")
            print("2. Adicionar Despesa")
            print("3. Mostrar Transações")
            print("4. Mostrar Saldo")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                valor = float(input("Digite o valor da sua Renda: "))
                conta.adicionar_renda("Renda", valor)
                print("Salário adicionado com sucesso!")
            elif escolha == '2':
                valor = float(input("Digite o valor da despesa: "))
                conta.adicionar_despesa('despesa', valor)
                print("Despesa adicionada com sucesso!")
            elif escolha == '3':
                conta.saldo_conta()
            elif escolha == '4':
                conta.mostrar_saldo()
            elif escolha == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def adicionar_renda(self, tipo, valor):
        self.transacoes.append((tipo, valor))
        if tipo == 'Salario':
            self.saldo += valor (input("Digite o valor da sua Renda: "))
            ContaPessoal.adicionar_renda('Salario', valor)
        elif tipo == 'Gorjeta':
            self.saldo += valor (input("Digite o valor da sua Renda: "))
            ContaPessoal.adicionar_renda('Gorjeta', valor)
        elif tipo == 'Pix Misterioso':
            self.saldo += valor (input("Digite o valor da sua Renda: "))
            ContaPessoal.adicionar_renda('PIX Misterioso', valor)
        elif tipo == 'Bolsa':
            self.saldo += valor (input("Digite o valor da sua Renda: "))
            ContaPessoal.adicionar_renda('Bolsa', valor)
        return 
    

    def adicionar_despesa(self, tipo, valor):
        self.transacoes.append((tipo, valor))
        if tipo == 'Fralda':
            self.saldo -= float (valor (input("Digite o valor da sua Despesa: ")))
            ContaPessoal.adicionar_despesa('Fralda', valor)
        elif tipo == 'Conta de Luz':
            self.saldo -= float (valor (input("Digite o valor da sua Despesa: ")))
            ContaPessoal.adicionar_despesa('Conta de Luz', valor)

    def saldo_conta(self):
        return self.renda_total() - self.despesa_total()

    def renda_total(self):
        print(f"Transações para a conta de {self.nome}:")
        [print(f"Tipo: {tipo}, Valor: {valor}") for tipo, valor in self.transacoes]

    def mostrar_saldo(self):
        print(f"Saldo atual para a conta de {self.nome}: {self.saldo}")

    def despesa_total(self):
            return sum(transacao[1] for transacao in self.despesas)