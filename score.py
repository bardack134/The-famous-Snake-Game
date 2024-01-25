# Importa la clase Turtle del módulo turtle
from turtle import Turtle

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
        
        # Levanta el lápiz para que el objeto Score no deje una línea cuando se mueva
        self.penup()
        
        # Mueve el objeto Score a la posición (0, 280)
        self.setposition(0 , 280)
        
        # Inicializa la propiedad score del objeto Score con el valor 0
        self.score=0
        
        # Escribe el score actual en la pantalla
        self.write(f"Score: {self.score}", False,  align='center', font=('arial', 14, 'normal'))    
        
    # Define un método llamado add_score para la clase Score
    def add_score(self):
        
        # Borra lo que el objeto Score ha escrito anteriormente
        self.clear()
        
        # Incrementa el score en 1
        self.score += 1
        
        # Escribe el nuevo score en la pantalla
        self.write(f"Score: {self.score}", False,  align='center', font=('arial', 14, 'normal'))
