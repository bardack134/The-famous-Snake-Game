# Importa las clases Turtle y Screen del módulo turtle
import time

from turtle import Turtle, Screen, left

from snake import Snake

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


#Creamos objeto de la clase snake 'ver snake.py'
snake=Snake()


#llamamos al metodo  create snake() de la clase snake
snake.create_snake() 
    
# La función listen() hace que la pantalla comience a escuchar los eventos del teclado
screen.listen()

# La función onkey() registra una función para que se llame cuando se presiona una tecla específica
# En este caso, cuando se presiona la tecla "Up", se llama al metodo up de la clase Snake (snake.py)
screen.onkey(snake.up, "Up")

# Cuando se presiona la tecla "Down", se llama  al metodo down de la clase Snake (snake.py)
screen.onkey(snake.down, "Down")

# Cuando se presiona la tecla "Left", se llama al metodo left de la clase Snake (snake.py)
screen.onkey(snake.left, "Left")

# Cuando se presiona la tecla "Right", se llama al metodo right de la clase Snake (snake.py)
screen.onkey(snake.right, "Right")


# Inicia el juego
game_is_on=True


# Imprime la coordenada x del tercer segmento de la serpiente
# print(snake_list[0].xcor())


# Mientras el juego esté en marcha
while game_is_on:
    
    # Hace una pausa de 0.1 segundos
    time.sleep(0.1)
    
    # Actualiza la pantalla
    screen.update()
    
    #llamamos al metodo snake_move() de la clase Snake en el archivo snake.py
    snake.snake_move()
    

        

   
    



# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()
