# Importa el módulo random para generar números aleatorios
import random

# Importa la clase Turtle del módulo turtle
from turtle import Turtle



# Define una clase llamada Food que hereda de la clase Turtle
class Food(Turtle):
    
    # El método __init__ se llama automáticamente cuando se crea un nuevo objeto de la clase Food
    def __init__(self):
        # Llama al método __init__ de la clase padre Turtle
        super().__init__()
        
        # Configura la forma del objeto Food como un círculo
        self.shape("circle")
        
        # Configura el tamaño del objeto Food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        
        # Levanta el lápiz para que el objeto Food no deje una línea cuando se mueva
        self.penup()
        
        # Configura el color del objeto Food como azul cielo profundo
        self.color("deep sky blue")
        
        # Configura la velocidad del objeto Food como la más rápida
        self.speed("fastest")
        
        # Mueve el objeto Food a la posición (X, Y)
        self.new_position()


    def new_position(self):
        # Genera un número aleatorio entre -280 y 280 para la coordenada x
        new_X=random.randint(-280, 280)

        # Genera un número aleatorio entre -280 y 280 para la coordenada y
        new_Y=random.randint(-280, 280)    
        
        # Mueve el objeto Food a la posición (X, Y)
        self.setposition(new_X, new_Y)
        
# food=Food()        

# screen=Screen()

# # Configura el tamaño de la pantalla a 600 de ancho y 600 de alto
# screen.setup(width=600, height=600)

# # Cambia el color de fondo de la pantalla a negro
# screen.bgcolor("black")

# screen.exitonclick()
