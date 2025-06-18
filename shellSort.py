import random as rd

class ShellSorted:
    def __init__ (self , data):
        self.data = data
    
    def shell_sort(self):
        n = len(self.data)
        gap = n // 2   # Se comienza con un gap de la mitad del tamaño de la lista

        # Realiza la ordenación por inserción con el gap actual
        while gap > 0:
            for i in range(gap , n):
                temp = self.data[i]
                j = i
                # Realiza la inserción con el gap actual
                while j >= gap and self.data[j - gap] > temp:
                    self.data[j] = self.data[j - gap]
                    j -= gap
                    self.data[j] = temp
            gap //= 2
    
    def get_sorted_data(self):
        return self.data

numeros = [ rd.randint(1 , 15) for i in range(20)]

ordenador = ShellSorted(numeros)

print("Lista original:", numeros)
ordenador.shell_sort()
print("Lista ordenada:", ordenador.get_sorted_data())