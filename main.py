from parcial import Personas, Mascotas, Tienda, Animales

if __name__ == "__main__":
    personas = Personas()
    mascotas = Mascotas()
    tienda = Tienda()
    animales = Animales()

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Personas")
        print("2. Mascotas")
        print("3. Tienda")
        print("4. Animales")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            personas.menu()
        elif opcion == "2":
            mascotas.menu()
        elif opcion == "3":
            tienda.menu()
        elif opcion == "4":
            animales.menu()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")
