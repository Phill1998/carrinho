class Carro:
    def __init__(self, cor, modelo, marca, motor=False, movimento=False):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.motor = motor
        self.movimento = movimento

    
    def ligar(self):
        if self.motor == False:
            self.motor = True
            
    def desligar(self):
            if self.motor == True:
                self.motor = False
                print('Você desligou o motor')
            
    def andar(self):
            if self.movimento == False:
                self.movimento = True
            
    def parar(self):
        if self.movimento == True:
            self.movimento = False
            print('Você desligou o carro')
            
    def status(self):
        if self.motor == False:
            return 'O carro está parado e motor está desligado'
        elif self.motor == True and self.movimento == False:
            return 'O motor está ligado mas o carro está parado'
        elif self.motor == False and self.movimento == True:
            return 'O motor não está ligado, então o carro não pode andar'
        elif self.motor == True and self.movimento == True:
            return 'O carro agora está felizmente andando'
            
            
meu_carro = Carro('Rosa', 'RX7', 'Mazda')

print (meu_carro.cor)
print (meu_carro.marca)
print (meu_carro.modelo)

print (meu_carro.status())

meu_carro.ligar()
print (meu_carro.status())

meu_carro.andar()
print (meu_carro.status())

meu_carro.parar()
print (meu_carro.status())

meu_carro.desligar()
print (meu_carro.status())