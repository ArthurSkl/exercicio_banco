from Cliente import * 




x=Cliente()




x.cadastrar("arthur","08396158177","456123")
# c=int(input("Deseja cadastrar outro cliente ? 1 - pra sim \n 2 - pra nao \n"))

while True:
    c=int(input("Deseja cadastrar outro cliente ? 1 - pra sim \n 2 - pra nao \n"))
    if(c == 1):
        x.cadastrar("jao","14278145896","485297")
        
        
        # x.cadastrar("pedro","47710546226","556297")
        
    else:    

        x.listar_clientes()

        
        break

cpf = "08396158177"

x.depositar(cpf,50000)

x.depositar(cpf,25000)

x.sacar(cpf,50000)

x.transferir(cpf,"14278145896",10000)

x.listar_clientes()

# y=Conta()

      
    