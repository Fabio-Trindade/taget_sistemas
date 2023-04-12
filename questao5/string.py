class String:
    def __init__(self,string:str):
        self._string = string
    def inverterString(self) -> str:
        newString = ""
        tamString = len(self._string)
        for i in range(tamString):
            newString +=self._string[tamString-i-1]
        return newString

if __name__ == "__main__":
    entrada = input("Insira a string: ")
    string = String(entrada)
    
    print(f'String: {entrada} \nString invertida: {string.inverterString()}')
    