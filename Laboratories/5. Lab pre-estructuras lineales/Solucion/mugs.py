"""Menu
   Venta de mugs

    Color de fondo:
        -Negro
        -Blanco
        -Azul
        -Rojo
    Estilos:
        -Dragon Ball: 35.000
        -Spiderman: 25.000
        -Mafalda: 20.000
        -Stitch: 15.000
    -El precio mostrado ya esta incluido el color de fondo; cualquier color de fondo tiene un costo de 5000
    """


products = {"DRAGON BALL": 35000, "SPIDERMAN": 25000, "MAFALDA": 20000, "STITCH": 15000}
colors = ["NEGRO", "BLANCO", "AZUL", "ROJO"]
class Shopping:
    def __init__(self, style: str, color: str, amount: int):
        self.style, self.amount, self.color = None, 0, None
        self.set_style(style)
        self.set_color(color)
        self.set_amount(amount)
        self.calculatePrice()

    def set_style(self, style : str ):
        if not isinstance(style,str):
            raise Exception("Data validation error,  attribute style must be str")
        self.style = style
        self.calculatePrice()

    def set_color(self, color : str ):
        if not isinstance(color,str):
            raise Exception("Data validation error,  attribute color must be str")
        self.color = color

    def set_amount(self, amount : int ):
        if not isinstance(amount, int):
            raise Exception("Data validation error,  attribute amount must be int")
        self.amount = amount
        self.calculatePrice()

    def update_amount(self, new_amount):
        self.set_amount(new_amount)

    def calculatePrice(self):
        self.price = products[self.style] * self.amount

    def __str__(self):
        return str(("Style:",self.style,"Color:",self.color,"Amount:",self.amount,"Price:",self.price))
class Cliente:
    def __init__(self, id):
        self.set_id(id)
        self.car = []
        self.fprice = 0

    def set_id(self, id):
        if (not isinstance(id, str)):
            raise Exception("Data validation error, attribute id must be str")
        self.id = id

    def delete_car(self, new_shopping):
        if (not isinstance(new_shopping, Shopping)):
            raise Exception("Data validation error, attribute Shopping must be Shopping")
        check, index= False, 0
        while not check and index < len(self.car):
            check, index = (self.car[index].style == new_shopping.style and self.car[index].color == new_shopping.color), index+1
        if check:
            self.car.pop(index-1)
            self.calculate_price()

        else:
            raise Exception("Object not present in car")
    def update_car(self, new_shopping):
        if (not isinstance(new_shopping, Shopping)):
            raise Exception("Data validation error, attribute Shopping must be Shopping")
        check, index= False, 0
        while not check and index < len(self.car):
            check, index = (self.car[index].style == new_shopping.style and self.car[index].color == new_shopping.color), index+1
        if check:
            self.car[index-1].update_amount(new_shopping.amount + self.car[index-1].amount)

        else:
            self.car.append(new_shopping)
        self.calculate_price()
    def calculate_price(self):
        temp_price = 0
        for x in self.car:
            temp_price += x.price
        self.fprice = temp_price if len(self.car) > 0 else 0

    def __str__(self):
        return str({"ID": self.id,
                    "CAR": list(map(str, self.car)),
                    "FINAL PRICE": self.fprice})


#Interfaz
def car():
    print("¿Que producto desea comprar?")
    style = input().upper()
    while style not in products.keys():
        print("Este producto no esta en nuestro menu\n¿Que producto desea comprar?")
        style = input().upper()
    print("¿Que color de fondo desea?")
    color = input().upper()
    while color not in colors:
        print("Este color no esta en nuestro menu\n¿Que color de fondo desea?")
        color = input().upper()
    print("¿Que cantidad desea?")
    amount = int(input())
    while amount <= 0:
        print("Esta en una cantidad invalida, intentelo de nuevo")
        amount = int(input())
    return style, color, amount
def main():
    id = input("Ingrese el numero de documento")
    carrito = Cliente(id)
    #interfaz
    """rta = "SI"
    while rta == "SI":
        style, color, amount = car()
        carrito.update_car(Shopping(style, color, amount))
        rta = input("¿Desea seguir comprando? (si/no)").upper()"""
    # Para efectos de prueba
    carrito.update_car(Shopping("DRAGON BALL", "NEGRO", 2))
    carrito.update_car(Shopping("DRAGON BALL", "NEGRO", 2))
    carrito.update_car(Shopping("SPIDERMAN", "NEGRO", 2))
    carrito.delete_car(Shopping("DRAGON BALL", "NEGRO",0))
    print("datos:", carrito)
    #print( "carrito:",list(map(str, carrito.car)))
    print("El precio final de su compra es de :", (carrito.fprice * (19/100)) + carrito.fprice, "(Incluido IVA)")
main()

