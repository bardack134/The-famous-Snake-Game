# Importa la clase Turtle del módulo turtle
from turtle import Turtle

#constantes que definen caracteristicas del programa como tipo de letra y tama;o de letra, las pongo aca por si las 
# quiero modificar en el futuro y no tener que buscarlas dentro del codigo
ALIGMENT='center'

FONT=('Courier', 16, 'normal')

# Define una clase llamada Score que hereda de la clase Turtle
class Score(Turtle):
    
    # El método __init__ se llama automáticamente cuando se crea un nuevo objeto de la clase Score
    def __init__(self):
        
        # Llama al método __init__ de la clase padre Turtle
        super().__init__()
        
        # Inicializa la propiedad score del objeto Score con una lista vacía
        self.score=[]
        
        # Configura el color del lápiz del objeto Score como blanco
        self.pencolor('white')
        
        self.hideturtle()
        
        # Levanta el lápiz para que el objeto Score no deje una línea cuando se mueva
        self.penup()
        
        # Mueve el objeto Score a la posición (0, 280)
        self.setposition(0 , 270)
        
        # Inicializa la propiedad score del objeto Score con el valor 0
        self.score=0
        
        self.update_scoreboard()  
        
    
    #funcion que escribe el msj de 'Score:0' en pantalla
    def update_scoreboard(self):
        self.clear()
        
        # Escribe el score actual en la en la pantalla, write es una funcion de Turtle 
        self.write(f"score: {self.score}", False,  align=ALIGMENT, font=FONT) 
        
    # Metodo que aumenta el puntaje o registro de la propiedad self.score
    def add_score(self):
        
        # Borra lo que el objeto Score ha escrito anteriormente
        self.clear()
        
        # Incrementa el score en 1
        self.score += 10
        
        # Escribe el nuevo score en la pantalla
        self.update_scoreboard()


    #funcion cuando termina el juego, ejemplo si la snake toca la pared
    def end_game(self):
        #llevamos el turtle al centro
        self.goto(0, 0)
        
        #mostramos msj al user
        self.write(f"GAME OVER: {self.score}", False,  align=ALIGMENT, font=('Courier', 20, 'bold')) 