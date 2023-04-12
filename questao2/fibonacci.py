class Fibonacci:
    @classmethod
    def __fibAuxiliar(cls,numero:int, n1:int, n2:int)-> bool:
        soma = n1+n2
        if numero == soma:
            return True
        elif soma < numero:
            return cls.__fibAuxiliar(numero,n2,soma)
        else:
            return False
        
    @classmethod
    def fibonacciContemRecursivo(cls,numero:int)->bool:
        fib0:int = 0
        fib1:int = 1
        if numero == 0 or numero ==1:
            return True
        return cls.__fibAuxiliar(numero,fib0,fib1)
        
    def fibonacciContemIterativo(numero:int)->bool:
        fib0:int = 0
        fib1:int = 1
        if numero == 0 or numero == 1:
            return True
        proximo = 1
        while proximo < numero:
            fib0 = fib1
            fib1 = proximo
            proximo = fib0 + fib1
            if proximo == numero:
                return True
        return False
    
if __name__ == "__main__":
    fib = Fibonacci
    numero = int(input())
    print("O número",f'{numero}',"pertence a sequência Fibonacci." if fib.fibonacciContemIterativo(numero)
           else "não pertence a sequência Fibonacci.", "(Versão iterativa)")
    print("O número",f'{numero}',"pertence a sequência Fibonacci." if fib.fibonacciContemRecursivo(numero) 
          else "não pertence a sequência Fibonacci.", "(Versão recursiva)")

