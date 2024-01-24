# Importa las clases Turtle y Screen del módulo turtle
import time
from turtle import Turtle, Screen, left

# Crea un objeto de la clase Screen
screen=Screen()

# Configura el tamaño de la pantalla a 600 de ancho y 600 de alto
screen.setup(width=600, height=600)

# Cambia el color de fondo de la pantalla a negro
screen.bgcolor("black")

# Cambia el título de la ventana a "The famous Snake Game"
screen.title("The famous Snake Game")

#Este comando desactiva la animación en la pantalla. Esto es útil cuando se quiere dibujar algo rápidamente sin mostrar cada paso del proceso
screen.tracer(0)

# Crea una variable para guardar la posición horizontal inicial de la primera parte de la serpiente
initial_position_x=0

#lista vacia de los segmentos de la serpiente
snake_list=[]

#lista de posiciones
position_list=[]

# Crea un bucle que se repite 3 veces
for i in range(0,3):
    
    # Crea un objeto de la clase Turtle con forma de cuadrado
    new_segment=Turtle("square")

    #levantamos el lapiz para no dejar marcas cuando movamos los segmentos de la tortuga a la posicion inical x
    new_segment.penup() 
    
    # Cambia el color de la parte de la serpiente a blanco
    new_segment.color("white")

    # Mueve la parte de la serpiente a la posición (initial_position_x, 0)
    new_segment.setposition(initial_position_x, 0)
   
    #agrega la posision actual de la tortuga o new_segment creado a una lista llamada postion_list
    position_list.append(new_segment.position())
    
    # Disminuye la posición horizontal en 20 unidades para la siguiente parte de la serpiente
    initial_position_x -= 20
   
   
    #agregamos los objetos creados "segmentos"  a la lista vacia 
    snake_list.append(new_segment)
    
    
# Imprime la lista de posiciones
print(position_list)


# Imprime la longitud de la lista de segmentos de la serpiente
print(len(snake_list))


# Inicia el juego
game_is_on=True


# Imprime la coordenada x del tercer segmento de la serpiente
print(snake_list[0].xcor())


# Mientras el juego esté en marcha
while game_is_on:
    
    # Hace una pausa de 0.1 segundos
    time.sleep(0.1)
    
    # Actualiza la pantalla
    screen.update()
    
    # Para cada segmento de la serpiente, empezando por el último segmento o posicion y terminando en el primer segmento o posicion dentro de la lista
    for i in range(len(snake_list)-1, 0, -1 ):
        
        # Obtiene la posición x del elemeto inmediatamente anterior, por eso le restamos - 1 a 'i'
        new_x_position=snake_list[i-1].xcor()
        
        # Obtiene la posición y del segmento anterior
        new_y_position=snake_list[i-1].ycor()
        
        # Mueve el segmento actual a la posición del segmento anterior, si i=2, mueve la posicion a la posicion del segmento '1'
        snake_list[i].setposition(new_x_position, new_y_position)        
    
    # Mueve el primer segmento de la serpiente hacia adelante en 10 unidades
    snake_list[0].forward(10)
    

        

   
    



# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()
