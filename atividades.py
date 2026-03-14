"""
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Classe Carro herdando de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, combustivel, portas):
        super().__init__(marca, modelo, ano)
        self.combustivel = combustivel
        self.portas = portas

    def exibir_especificacoes(self):
        print("=== Carro ===")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Combustível:", self.combustivel)
        print("Número de portas:", self.portas)
        print()

# Classe Motocicleta herdando de Veiculo
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, partida):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
        self.partida = partida

    def exibir_especificacoes(self):
        print("=== Motocicleta ===")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Cilindradas:", self.cilindradas)
        print("Tipo de partida:", self.partida)
        print()

# Cadastro de veículos
veiculos = []

carro1 = Carro("Toyota", "Corolla", 2022, "Flex", 4)
moto1 = Motocicleta("Honda", "CG 160", 2023, 160, "Elétrica")

veiculos.append(carro1)
veiculos.append(moto1)

# Exibir especificações
for v in veiculos:
    v.exibir_especificacoes() """

class Funcionario:
    def __init__(self, nome, email, salario):
        self.nome = nome
        self.email = email
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Salário: {self.salario}")


class Desenvolvedor(Funcionario):
    def __init__(self, nome, email, salario, linguagens):
        super().__init__(nome, email, salario)
        self.linguagens = linguagens

    def exibir_linguagens(self):
        print("Linguagens:", ", ".join(self.linguagens))


class Gerente(Funcionario):
    def __init__(self, nome, email, salario, departamento):
        super().__init__(nome, email, salario)
        self.departamento = departamento

    def exibir_departamento(self):
        print("Departamento:", self.departamento)


class Mentor:
    def __init__(self, horas_disponiveis):
        self.horas_disponiveis = horas_disponiveis

    def mentorear(self):
        print(f"Disponível para mentoria por {self.horas_disponiveis} horas.")



class DesenvolvedorMentor(Desenvolvedor, Mentor):
    def __init__(self, nome, email, salario, linguagens, horas_disponiveis):
        Desenvolvedor.__init__(self, nome, email, salario, linguagens)
        Mentor.__init__(self, horas_disponiveis)


class GerenteMentor(Gerente, Mentor):
    def __init__(self, nome, email, salario, departamento, horas_disponiveis):
        Gerente.__init__(self, nome, email, salario, departamento)
        Mentor.__init__(self, horas_disponiveis)



dev = DesenvolvedorMentor(
    "Ana",
    "ana@email.com",
    8000,
    ["Python", "JavaScript"],
    5
)

ger = GerenteMentor(
    "Carlos",
    "carlos@email.com",
    12000,
    "TI",
    3
)

print("=== Desenvolvedor Mentor ===")
dev.exibir_dados()
dev.exibir_linguagens()
dev.mentorear()

print("\n=== Gerente Mentor ===")
ger.exibir_dados()
ger.exibir_departamento()
ger.mentorear()