from turtle import  Turtle

#variables constantes
MOVE_DISTANCE = 15

class Snake():
    
    # Parametros de la clase Snake
    def __init__(self, ):
      
          
      # Inicializa la propiedad initial_position_x del objeto Snake con el valor 0
      self.initial_position_x=0
      
      # Inicializa la propiedad position_list del objeto Snake con una lista vacía
      self.position_list = []
      
      # Inicializa la propiedad snake_list del objeto Snake con una lista vacía
      self.snake_list = []


    #crea la snake del comienzo de 3 cuadrados de longitud
    def create_snake(self):
        
        # Crea un bucle que se repite 3 veces
        for i in range(0,3):
            
            # Crea un objeto de la clase Turtle con forma de cuadrado
            new_segment=Turtle("square")

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
            
    
    #funcion acerca del movimiento de la snake, la snake de posicion 0, se mueve hacia delante, y las demas posiciones toman la posicion de su 
    # antecesor
    def snake_move(self):
      
      # Para cada segmento de la serpiente, empezando por el último segmento o posicion y terminando con el segundo segmento o posicion dentro de la lista
      for i in range(len(self.snake_list)-1, 0, -1 ):
               
        # Obtiene la posición x del elemeto inmediatamente anterior, por eso le restamos - 1 a 'i'
        new_x_position=self.snake_list[i-1].xcor()
        
        # Obtiene la posición y del segmento anterior
        new_y_position=self.snake_list[i-1].ycor()
        
        # Mueve el segmento actual a la posición del segmento anterior, si i=2, mueve la posicion a la posicion del segmento '1'
        self.snake_list[i].setposition(new_x_position, new_y_position)        
    
      # Mueve el primer segmento de la serpiente hacia adelante en 10 unidades
      self.snake_list[0].forward(MOVE_DISTANCE)
    
    
    #metodo que agrega un nuevo segmento a la snake cuando esta come la bolita del juego
    def add_segment(self):   
      
      # Crea un objeto de la clase Turtle con forma de cuadrado 
      new_segment=Turtle('square')
       
      #levantamos el lapiz para no dejar marcas cuando movamos los segmentos de la tortuga a la posicion inical x
      new_segment.penup() 
            
      #despues de crear el nuevo objeto de la clase Turtle, que sera el nuevo segmento de la snake, con el meotod goto() lo dirigimos inmediatamente
      #a la ultima posicion de la snake y asi evitamos que por unos segundos se vea ese segmento nuevo creado en la posicion (0,0)      
      new_segment.goto(self.snake_list[-1].position())
            
      # Cambia el color de la parte de la serpiente a blanco
      new_segment.color("white")
      
      # agregamos  el objeto creado "segmento"  a la lista vacia 'snake_list'  que contiene todaos los segmentos de nuestra snake
      self.snake_list.append(new_segment)
      
             
    # Define el método para mover la serpiente hacia arriba
    def up(self):
          
          # Si la serpiente está moviéndose hacia la derecha
          if self.snake_list[0].heading()==0 :
            
            # Cambia la dirección de la serpiente a arriba
            new_setheading=self.snake_list[0].heading() + 90
            
            self.snake_list[0].setheading(new_setheading)
            
            
          # Si la serpiente está moviéndose hacia la izquierda
          elif self.snake_list[0].heading()==180:
            
            # Cambia la dirección de la serpiente a arriba
            new_setheading=self.snake_list[0].heading() - 90
            
            self.snake_list[0].setheading(new_setheading)   
        
            
    # Define el método para mover la serpiente hacia abajo
    def down(self):
          
          # Si la serpiente está moviéndose hacia la derecha
          if self.snake_list[0].heading()==0: 
            
            # Cambia la dirección de la serpiente a abajo
            new_setheading=self.snake_list[0].heading() + 270
            
            self.snake_list[0].setheading(new_setheading)
          
          
          # Si la serpiente está moviéndose hacia la izquierda
          elif self.snake_list[0].heading()==180:
            
            # Cambia la dirección de la serpiente a abajo
            new_setheading=self.snake_list[0].heading() + 90
            
            self.snake_list[0].setheading(new_setheading)    
            
            
    # Define el método para mover la serpiente hacia la izquierda
    def left(self):
          
          # Si la serpiente está moviéndose hacia arriba
          if self.snake_list[0].heading()==90: 
            
            # Cambia la dirección de la serpiente a la izquierda
            new_setheading=self.snake_list[0].heading() + 90
            
            self.snake_list[0].setheading(new_setheading)
          
          
          # Si la serpiente está moviéndose hacia abajo
          elif self.snake_list[0].heading()==270:
            
            # Cambia la dirección de la serpiente a la izquierda
            new_setheading=self.snake_list[0].heading() - 90
            
            self.snake_list[0].setheading(new_setheading)   
            
            
    # Define el método para mover la serpiente hacia la derecha
    def right(self):
          
          # Si la serpiente está moviéndose hacia arriba
          if self.snake_list[0].heading()==90: 
            
            # Cambia la dirección de la serpiente a la derecha
            new_setheading=self.snake_list[0].heading() - 90
            
            self.snake_list[0].setheading(new_setheading)
          
          
          # Si la serpiente está moviéndose hacia abajo
          elif self.snake_list[0].heading()==270:
            
            # Cambia la dirección de la serpiente a la derecha
            new_setheading=self.snake_list[0].heading() + 90
            
            self.snake_list[0].setheading(new_setheading)  
