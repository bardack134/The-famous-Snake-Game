class Snake():
    
    # Parametros de la clase Snake
    def __init__(self, Turtle):
      
      # Asigna el argumento Turtle a la propiedad Turtle del objeto Snake
      self.Turtle = Turtle
      
      # Inicializa la propiedad initial_position_x del objeto Snake con el valor 0
      self.initial_position_x=0
      
      # Inicializa la propiedad position_list del objeto Snake con una lista vacía
      self.position_list = []
      
      # Inicializa la propiedad snake_list del objeto Snake con una lista vacía
      self.snake_list = []

    
    def create_snake(self):
        
        # Crea un bucle que se repite 3 veces
        for i in range(0,3):
            
            # Crea un objeto de la clase Turtle con forma de cuadrado
            new_segment=self.Turtle("square")

            #levantamos el lapiz para no dejar marcas cuando movamos los segmentos de la tortuga a la posicion inical x
            new_segment.penup() 
            
            # Cambia el color de la parte de la serpiente a blanco
            new_segment.color("white")

            # Mueve la parte de la serpiente a la posición (initial_position_x, 0)
            new_segment.setposition(self.initial_position_x, 0)
        
            #agrega la posision actual de la tortuga o new_segment creado a una lista llamada postion_list
            self.position_list.append(new_segment.position())
            
            # Disminuye la posición horizontal en 20 unidades para la siguiente parte de la serpiente
            self.initial_position_x -= 20
        
        
            #agregamos los objetos creados "segmentos"  a la lista vacia 
            self.snake_list.append(new_segment)
    
    
    def snake_move(self):
      
      # Para cada segmento de la serpiente, empezando por el último segmento o posicion y terminando en el primer segmento o posicion dentro de la lista
      for i in range(len(self.snake_list)-1, 0, -1 ):
               
        # Obtiene la posición x del elemeto inmediatamente anterior, por eso le restamos - 1 a 'i'
        new_x_position=self.snake_list[i-1].xcor()
        
        # Obtiene la posición y del segmento anterior
        new_y_position=self.snake_list[i-1].ycor()
        
        # Mueve el segmento actual a la posición del segmento anterior, si i=2, mueve la posicion a la posicion del segmento '1'
        self.snake_list[i].setposition(new_x_position, new_y_position)        
    
      # Mueve el primer segmento de la serpiente hacia adelante en 10 unidades
      self.snake_list[0].forward(10)
              