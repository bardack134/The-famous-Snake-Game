class Snake():
    
    def __init__(self, Turtle):
      self.Turtle = Turtle
      self.position_list = []
      self.snake_list = []
    
    def create_snake(self):
        # Crea un objeto de la clase Turtle con forma de cuadrado
        new_segment=self.Turtle("square")

        #levantamos el lapiz para no dejar marcas cuando movamos los segmentos de la tortuga a la posicion inical x
        new_segment.penup() 
        
        # Cambia el color de la parte de la serpiente a blanco
        new_segment.color("white")

        # Mueve la parte de la serpiente a la posición (initial_position_x, 0)
        new_segment.setposition(initial_position_x, 0)
    
        #agrega la posision actual de la tortuga o new_segment creado a una lista llamada postion_list
        self.position_list.append(new_segment.position())
        
        # Disminuye la posición horizontal en 20 unidades para la siguiente parte de la serpiente
        initial_position_x -= 20
    
    
        #agregamos los objetos creados "segmentos"  a la lista vacia 
        self.snake_list.append(new_segment)
            