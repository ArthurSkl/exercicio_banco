
class ValidarDados:

    def __init__(self) -> None:
        pass
        
    def validar_cpf(cpf):
        cpf = cpf.replace(".", "").replace("-", "")  # Remover pontos e traços
        if not cpf.isdigit() or len(cpf) != 11:  # Verificar se o CPF contém apenas números e tem 11 dígitos
            return False

        # Calcular o primeiro dígito verificador
        soma = 0
        peso = 10
        for i in range(9):
            soma += int(cpf[i]) * peso
            peso -= 1
        primeiro_digito = 11 - (soma % 11)
        if primeiro_digito > 9:
            primeiro_digito = 0

        # Calcular o segundo dígito verificador
        soma = 0
        peso = 11
        for i in range(10):
            soma += int(cpf[i]) * peso
            peso -= 1
        segundo_digito = 11 - (soma % 11)
        if segundo_digito > 9:
            segundo_digito = 0

        # Verificar se os dígitos verificadores calculados são iguais aos dígitos fornecidos
        if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
            return True
        return False

    def validar_rg(rg): 
        
        rg = rg.replace(".", "").replace("-", "")
        
        if(rg.isdigit() and len(rg) >= 5):
            
            return True
        else:
            print("invalido")
            return False
    
    

    