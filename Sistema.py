from Gestion_stock import inicializar, cargar_stock, mostrar_stock, contar, stock_cantidades
from Menu import mostrar_menu

def main():
    inicializar()
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            cargar_stock()
        elif opcion == 2:
            mostrar_stock()
        elif opcion == 3:
            categoria = input("Ingrese categoria (pescaderia, verduleria, snacks, gaseosas): ").lower()
            if categoria in stock_cantidades:
                contar(stock_cantidades[categoria])
            else:
                print("Categoria no valida")
        elif opcion == 4:
            break

if __name__ == "__main__":
    main()