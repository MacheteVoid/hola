stock_productos = {'pescaderia': [], 'verduleria': [], 'snacks': [], 'gaseosas': []}
stock_cantidades = {'pescaderia': [], 'verduleria': [], 'snacks': [], 'gaseosas': []}

def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []

def cargar_stock():
    categoria = input("Ingrese categoria (pescaderia, verduleria, snacks, gaseosas): ").lower()
    if categoria not in stock_productos:
        print("Categoria no valida")
        return
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    stock_productos[categoria].append(producto)
    stock_cantidades[categoria].append(cantidad)

def mostrar_stock():
    for categoria in stock_productos:
        print(categoria)
        for i in range(len(stock_productos[categoria])):
            print(stock_productos[categoria][i], stock_cantidades[categoria][i])

def contar(lista_productos):
    print("Cantidad de productos:", len(lista_productos))
    print("Suma de cantidades:", sum(lista_productos))