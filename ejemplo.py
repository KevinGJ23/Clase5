class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      # self.__lista_pacientes = []
      self.__lista_pacientes = {}
      self.__numero_pacientes = len(self.__lista_pacientes)
    def Verificar(self,ce):
        if (self.__lista_pacientes.get(ce) != None):
            return True
        else:
            return False 


    def ingresarPaciente(self,pa):
        # 1- solicito los datos por teclado
              
        # 3- guardo el Paciente en  la lista        
        # self.__lista_pacientes.append(pa)
        self.__lista_pacientes[pa.verCedula()] = pa
        # 4- actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self,ce):
        
        
        for paciente in self.__lista_pacientes:
            if ce == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
def main():               
    mi_sistema = Sistema()

    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. Salir:  \n"))
        if opcion == 1:
            cedula = int(input("Ingrese la cedula: "))   
            res=mi_sistema.Verificar(cedula)
            if res == False:
                nombre = input("Ingrese el nombre: ")
                genero = input("Ingrese el genero: ")
                servicio = input("Ingrese el servicio: ")
                # 2- creo el objeto Paciente y le asigno los datos
                p = Paciente()
                p.asignarNombre(nombre)
                p.asignarCedula(cedula)
                p.asignarGenero(genero)
                p.asignarServicio(servicio)  
                mi_sistema.ingresarPaciente(p)
            else:
                print("El paciente esta en el sistema, por favor ingresa uno nuevo")
        elif opcion == 2:
            print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
        elif opcion == 3:
            cedula = int(input("Ingrese la cedula a buscar: "))
            mi_sistema.verDatosPaciente(cedula)

        elif opcion == 4:
            break
        else:
            print("Opcion invalida")
main ()   