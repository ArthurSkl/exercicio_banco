from ValidarDados import *


clientes = []

cliente = {}


class Cliente:

    def __init__(self):
        pass
        
    def cadastrar(self, nome, cpf, rg):
        validar = ValidarDados
        
        while True:
            p = validar.validar_rg(rg)
            if p:
                self.rg = rg 
                break
            else:
                print("RG INVÁLIDO!")
                rg = input("Informe um RG válido: ")
            
        while True:
            if validar.validar_cpf(cpf):
                
                self.cpf = cpf 
                break
            else:
                print("CPF inválido")
                cpf = input("Informe seu CPF: ")
            
        saldo = 0
        
        while True:
            try:
                conta = int(input("Qual o tipo da conta, digite o número correspondente?\n1 - para conta poupança!\n2 - para conta corrente! "))
                if conta == 1:
                    print("Você escolheu conta poupança.")
                    conta = "poupança"
                    break
                elif conta == 2:
                    print("Você escolheu conta corrente.")
                    conta = "corrente"
                    break
                else:
                    print("Opção inválida. Por favor, escolha 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")          
        
        self.conta = conta
        self.nome = nome 
        self.saldo = saldo  
        self.rg = rg
        self.cpf = cpf
        
        novo_cliente = {
            self.cpf: {
                "Tipo Conta": self.conta,
                "Nome": self.nome,
                "RG": self.rg,
                "CPF": self.cpf,
                "Saldo": self.saldo
            }
        }
        
        clientes.append(novo_cliente)
        
        return print("Cliente cadastrado com sucesso! :)")
        
        
        
    def listar_clientes (self):    
        
        # for i in range (len(clientes)): 
        #     for chave, valor in cliente.items():
        #         return(f"Chave: {chave}, Valor: {valor} \n")
        
        # return(clientes)
        
        print(clientes)
        
    
    
    
    def depositar(self, cpf, valor):
        for cliente in clientes:
            if cpf in cliente:
                dados_cliente = cliente[cpf]
                print("Informações do cliente:")
                print("Tipo Conta:", dados_cliente["Tipo Conta"])
                print("Nome:", dados_cliente["Nome"])
                print("RG:", dados_cliente["RG"])
                print("CPF:", dados_cliente["CPF"])
                saldo_atual = dados_cliente["Saldo"]
                print("Saldo atual:", saldo_atual)
                
                try:
                    valor = float(valor)
                    if valor > 0:
                        novo_saldo = saldo_atual + valor
                        dados_cliente["Saldo"] = novo_saldo
                        print("Depósito realizado com sucesso.")
                        print("Novo saldo:", novo_saldo)
                    else:
                        print("Valor de depósito inválido. Deve ser maior que 0.")
                except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número.")
                
                break  
        else:
            print("Cliente não encontrado.")
        
        
    def sacar(self, cpf, valor):
        for cliente in clientes:
            if cpf in cliente:
                dados_cliente = cliente[cpf]
                print("Informações do cliente:")
                print("Tipo Conta:", dados_cliente["Tipo Conta"])
                print("Nome:", dados_cliente["Nome"])
                print("RG:", dados_cliente["RG"])
                print("CPF:", dados_cliente["CPF"])
                saldo_atual = dados_cliente["Saldo"]
                print("Saldo atual:", saldo_atual)
                
                try:
                    valor = float(valor)
                    if valor > 0 and valor <= saldo_atual:
                        novo_saldo = saldo_atual - valor
                        dados_cliente["Saldo"] = novo_saldo
                        print("Saque realizado com sucesso.")
                        print("Novo saldo:", novo_saldo)
                    else:
                        print("Valor de saque inválido.")
                        if valor <= 0:
                            print("O valor deve ser maior que 0.")
                        else:
                            print("Saldo insuficiente.")
                except ValueError:
                    print("Valor inválido. Certifique-se de inserir um número.")
                
                break  
        else:
            print("Cliente não encontrado.")        
    
    
    
    
    def transferir(self, cpf_origem, cpf_destino, valor):
        cliente_origem = None
        cliente_destino = None
        
        
        for cliente in clientes:
            if cpf_origem in cliente:
                cliente_origem = cliente
            elif cpf_destino in cliente:
                cliente_destino = cliente
            
            if cliente_origem and cliente_destino:
                break
        
        if cliente_origem is None:
            print("Cliente de origem não encontrado.")
            return
        
        if cliente_destino is None:
            print("Cliente de destino não encontrado.")
            return
        
        dados_cliente_origem = cliente_origem[cpf_origem]
        saldo_origem = dados_cliente_origem["Saldo"]
        
        if dados_cliente_origem["Tipo Conta"] != "corrente":
            print("Apenas contas correntes podem fazer transferências.")
            return
        
        dados_cliente_destino = cliente_destino[cpf_destino]
        
        try:
            valor = float(valor)
            if valor > 0 and valor <= saldo_origem:
                saldo_origem -= valor
                dados_cliente_origem["Saldo"] = saldo_origem
                
                saldo_destino = dados_cliente_destino["Saldo"]
                saldo_destino += valor
                dados_cliente_destino["Saldo"] = saldo_destino
                
                print("Transferência realizada com sucesso.")
                print("Novo saldo da conta de origem:", saldo_origem)
                print("Novo saldo da conta de destino:", saldo_destino)
            else:
                print("Valor de transferência inválido.")
                if valor <= 0:
                    print("O valor deve ser maior que 0.")
                else:
                    print("Saldo insuficiente.")
        except ValueError:
            print("Valor inválido. Certifique-se de inserir um número.")
            
            