class Prova:
    _myClassVariable = 0

    def __init__(self, input):
        self.myInstanceVariable = input

    # stampo quello a cui ho accesso con ogni tipo di metodo

    def standardMethod(self):
        print(self.myInstanceVariable)
        # accesso all'istanza

    @staticmethod
    def staticMethod():
        pass
        # accesso solo agli argomenti passati

    @classmethod
    def classMethod(cls):
        print(cls._myClassVariable)
        # accesso alla classe

newInstance = Prova("txt")
newInstance.standardMethod()