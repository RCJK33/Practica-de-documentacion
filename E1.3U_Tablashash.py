import math
#from ..Unidad2.E2_U_Animales import Animal


class HashTable:
    def __init__(self,length: int = 29,magic_number: int = 7,rehash_Limit: int = 6) -> None:
        # Se recomienda utilizar numeros primos para el length de la lista
        # Se recomienda dejar el numero magico en 7, 2 o 1 (puedes probar a ver cual da menos coluciones)
        #   de preferencia un numero primo relativo del length de la lista
        self.__hashList = list(None for i in range(length))
        self.__lengthTable = length
        self.__rehashLimit = rehash_Limit

        self.__magicNumber = magic_number

        self.length = 0

    # Esta version del metodo no hacer Rehash
    def __hash__(self,key: str) -> int:
        hs = 0
        index = 1
        keyLength = len(key)
        
        for i in range(keyLength):
            # Formula Hash [Funcion lineal con los parametros 
            # i++ (ascii de Char) + (2 (o 1) + ascii char)]
            # Funcion que depende del numero de iteracion lo que significa que si hay otra letra igual, la funcion no sera igual.
            hs += (i+1) * (ord(key[i])) + self.__magicNumber
        index = hs % self.__lengthTable

        # print("{:<15}{:<10}{:<15}{:<2}".format(key,index,str(self.__hashList[index]),1))
        return index

    # Metodo basado en el metodo de Direccionamiento abierto o Hasing Cerrado (Rehash)
    # Mas info en https://ccia.ugr.es/~jfv/ed1/tedi/cdrom/docs/tablash.html
    """ def __hash__(self,key: str) -> int:
        def rehash(keyLength: int, intents: int = 1):
            hash = 0
            for it in range(keyLength):
                # Formula Hash [Funcion lineal con los parametros 
                #   i++ (ascii de Char) + no. de intentos]
                # Funcion que depende del numero de iteracion lo que significa que si hay otra letra igual, la funcion no sera igual.

                hash += (it + 1) * (ord(key[it])) + intents

                # Nota: una variacion importante, es hacer que el ciclo vaya de 2 en 2 caracteres (sumar ambos o multiplicarlos)
            return int(hash)
        
        ints = 0
        while True:
            index = rehash(len(key), (ints + self.__magicNumber)) % self.__lengthTable

            if self.__isAvailable(index):
                print("{:<15}{:<10}{:<2}".format(key, index, ints+1))
                return index
            elif ints < self.__rehashLimit:
                ints += 1
            else:
                print(f"Hash no disponible  -> {key} | [{ints} intentos].")
                break """
    
    def __isAvailable(self, index: int):
        try:
            if self.__hashList[index] is None:
                return True
        except:
            return False
        return False
    
    def add(self, key: str):
        index = self.__hash__(key)
        if self.__isAvailable(index):
            self.__hashList[index] = key
            self.length += 1

    def printTableHash(self):
        print("{:<5}{:<15}".format('index','Value'))
        for i in range(self.__lengthTable):
            print("{:<5}{:<15}".format(i,str(self.__hashList[i])))


""" 
obj_name = HashTable(value)     => La instanciacion de la clase HashTable, indica en el parametro el tamaño de la tabla.
add("Cadena de texto")          => Metodo que añade un nuevo valor a la tabla hash.
__isAvailable(index)            => Metodo privado que se asegura de saber si habra una colisión. En caso de ser asi, retorna False, de lo contrario True
__hash__("Cadena de texto")     => Metodo privado que calcula el indice en el que se almacenara un elemento
"""


hash_list = HashTable(23)
# print("{:<15}{:<10}{:<2}".format('key','index','Intentos'))

hash_list.add("Mario")
hash_list.add("Mauricio")
hash_list.add("Fernanda")
hash_list.add("Noemi")
hash_list.add("Gael")
hash_list.add("Luis")
hash_list.add("Villegas")
hash_list.add("Carlos")
hash_list.add("Elisa") 
hash_list.add("Hoper")
hash_list.add("Karina")

hash_list.add("aniraK")
hash_list.add("repoH")
hash_list.add("asilE")
hash_list.add("solraC")
hash_list.add("sagelliV")
hash_list.add("siuL")
hash_list.add("leaG")
hash_list.add("imeoN")
hash_list.add("adnanreF")
hash_list.add("oiciruaM")
hash_list.add("oiraM")

hash_list.printTableHash()