"""
Array 2D(filas,columnas)
get_num_rows() ----> regresa una fila
get_num_cols() ----> regresa columnas
clearing(value)
set_item(r,c,valor)
get_item(r,c)

"""

class Array2D:
    def __init__(self,filas,columnas):
        self.__data = []
        self.__fila = filas
        self.__columna = columnas


        for i in range(filas):
            tmp = []
            for j in range(columnas):
                tmp.append(None)
            self.__data.append(tmp)

    def to_string(self):
        print(f"{self.__data}")

    def get_num_rows(self):
        return self.__fila

    def get_num_cols(self):
        return self.__fila #Checar esta linea de código

    def clearing(self, valor):
        for fila in range(self.__fila):
            for columna in range(self.__columna):
                self.__data[fila][columna] = valor


    def set_item(self,fila,columna,valor):
        if fila >= 0 and fila <self.__fila and columna >= 0 and columna < self.__columna:
            self.__data[fila][columna] = valor
        else:
            print("error en longitud")


    def 

