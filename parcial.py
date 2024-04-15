class Personas:
    def __init__(self):
        self.user = []
    
    def menu(self):
        while True:
            print("MENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print(self.agregar())
            elif opcion == "2":
                print(self.listar())
            elif opcion == "3":
                print(self.eliminar())
            elif opcion == "4":
                print(self.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
            
    def agregar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        per = input("Ingrese la persona: ")
        self.user.append(per)
        return 'Dato Agregado:', per

    def listar(self):   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        return "Lista De Datos Ingresados:", self.user
            
    def eliminar(self): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim = input("Ingrese el dato a eliminar: ")
        if elim in self.user:
            self.user.remove(elim)
            print("El Dato Eliminado Es:", elim)
        else:
            print("El dato no se encuentra en la lista.")
        return "Lista Actual:", self.user
        
    def actualizar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera = input("Ingrese la Persona A Actualizar: ") 
        if pera in self.user:
            actu = input("Ingrese El Dato Nuevo: ")
            posicion = self.user.index(pera)
            self.user[posicion] = actu
            print("Dato Actualizado.")
        else:
            print("La persona no se encuentra en la lista.")


class Mascotas:
    def __init__(self):
        self.mas = []
    
    def menu(self):
        while True:
            print("MENU MASCOTAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(self.agregar())
            elif opcion == "2":
                print(self.listar())
            elif opcion == "3":
                print(self.eliminar())
            elif opcion == "4":
                print(self.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        uni = input("Ingrese la Mascota: ")
        self.mas.append(uni)
        return 'Dato Agregado:', uni

    def listar(self):   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        return "Lista De Datos Ingresados:", self.mas
            
    def eliminar(self): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim = input("Ingrese la mascota a eliminar: ")
        if elim in self.mas:
            self.mas.remove(elim)
            print("Dato Eliminado:", elim)
        else:
            print("La mascota no se encuentra en la lista.")
        return "Lista Actual:", self.mas
    
    def actualizar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera = input("Ingrese la Mascota A Actualizar: ") 
        if pera in self.mas:
            actu = input("Ingrese El Dato Nuevo: ")
            posicion = self.mas.index(pera)
            self.mas[posicion] = actu
            print("Dato Actualizado.")
        else:
            print("La mascota no se encuentra en la lista.")


class Tienda:
    def __init__(self):
        self.tie = []
    
    def menu(self):
        while True:
            print("MENU TIENDA")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(self.agregar())
            elif opcion == "2":
                print(self.listar())
            elif opcion == "3":
                print(self.eliminar())
            elif opcion == "4":
                print(self.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        r = input("Ingrese El Artículo: ")
        self.tie.append(r)
        return "Dato Agregado:", r

    def listar(self): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')  
        return "Lista De Datos Ingresados:", self.tie
    
    def eliminar(self): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim = input("Ingrese El Artículo a eliminar: ")
        if elim in self.tie:
            self.tie.remove(elim)
            print("Dato Eliminado", elim)
        else:
            print("El artículo no se encuentra en la lista.")
        return "Lista Actual: ", self.tie
    
    def actualizar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera = input("Ingrese El Artículo A Actualizar: ") 
        if pera in self.tie:
            actu = input("Ingrese El Dato Nuevo: ")
            posicion = self.tie.index(pera)
            self.tie[posicion] = actu
            print("Dato Actualizado.")
        else:
            print("El artículo no se encuentra en la lista.")


class Animales:
    def __init__(self):
        self.ani = []
    
    def menu(self):
        while True:
            print("MENU ANIMALES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(self.agregar())
            elif opcion == "2":
                print(self.listar())
            elif opcion == "3":
                print(self.eliminar())
            elif opcion == "4":
                print(self.actualizar())
            elif opcion == "5":
                break

    def agregar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        a = input("Ingrese El Animal: ")
        self.ani.append(a)
        return 'Dato Agregado:', a

    def listar(self):   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        return "Lista De Datos Ingresados:", self.ani
    
    def eliminar(self): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        elim = input("Ingrese El animal a eliminar: ")
        if elim in self.ani:
            self.ani.remove(elim)
            print("Dato Eliminado", elim)
        else:
            print("El animal no se encuentra en la lista.")
        return "Lista Actual:", self.ani
    
    def actualizar(self):
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        pera = input("Ingrese Animal A Actualizar: ") 
        if pera in self.ani:
            actu = input("Ingrese El Dato Nuevo: ")
            posicion = self.ani.index(pera)
            self.ani[posicion] = actu
            print("Dato Actualizado.")
        else:
            print("El animal no se encuentra en la lista.")
           


