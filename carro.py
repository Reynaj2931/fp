class carro:
    color="negro"
    marca="civic"
    año="20221"
    cilindro="3 cilindro"
    transicion="automatico"
    alarma="true"

    def prendercarro(self):
        print("el carro esta encendido")
    def apagarcarro(self):
        print("el carro esta apagado")
    def avanzacarro(self):
        print("este carro avanza")
   

carroreyna = carro()
carroreyna.prendercarro()
carroreyna.apagarcarro()
carroreyna.avanzacarro()

