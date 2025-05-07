from pickle import FALSE


class Pessoa():
    def __init__(self,nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.dormindo=False
        self.comendo=False
        self.falando=False

    def dormir(self):
        if self.falando==True:
            print(f"{self.nome},esta falando, ele nao pode dormir!")

        elif self.comendo==True:
            print(f"{self.nome}, esta comendo, ele nao pode dormir!")
        elif self.dormindo == True:
            print(f"{self.nome}, ele ja esta dormindo!")
        else:
            self.dormindo=True
            print(f"{self.nome}, ele esta dormindo!")

    def comer (self):
        if self.dormindo==True:
            print(f"{self.nome},esta dormir, ele nao pode comer!")
        elif self.comendo == True:
            print(f"{self.nome},ele ja esta comendo!")
        elif self.falando==True:
            print(f"{self.nome}, esta falando, ele nao pode comer!")
        else:
            self.comendo=True
            print(f"{self.nome}, esta comendo")


    def falar(self):
        if self.dormindo ==True:
            print(f"{self.nome},esta dormindo, ele nao pode falar!")
        elif self.falando == True:
            print(f"{self.nome}, ele ja esta falando!")
        elif self.comendo==True:
            print(f"{self.nome}, esta comendo, ele nao pode falar!")
        else:
            self.falando=True
            print(f"{self.nome}, ele esta falando")