
class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def formateada(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

# Ejemplo de uso
if __name__ == "__main__":
    f = Fecha(21, 11, 2022)
    print(f.formateada())


f = Fecha(21, 11, 2022)
print(f.formateada())
