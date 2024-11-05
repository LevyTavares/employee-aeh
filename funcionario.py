# Isaías Levi Tavares da Silva

# Matrícula: 37023010

# 04/11/2024


# criando uma classe funcionário

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def aumentar_salario(self, valor):
        if valor > 0:
            self.__salario += valor
        else:
            print("Valor de aumento inválido.")

# criando uma classe gerente que herda de funcionário

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome, cargo, salario)

    def aumentar_salario(self, valor):
        if valor > 0:
            super().aumentar_salario(valor)  # Usa o método da superclasse para aumentar o salário
        else:
            print("Valor de aumento inválido.")

# código de teste

funcionario = Funcionario("João", "Desenvolvedor", 5000)
gerente = Gerente("Maria", "Gerente", 8000)

funcionario.aumentar_salario(500)
gerente.aumentar_salario(1000)

print(f"Salário do funcionário: {funcionario.get_salario()}")
print(f"Salário do gerente: {gerente.get_salario()}")
