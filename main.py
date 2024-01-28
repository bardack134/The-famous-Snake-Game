# Importa las clases Turtle y Screen del módulo turtle
import time

from turtle import Turtle, Screen

from snake import Snake

from food import Food

from score import Score

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

#creo un objeto de la clase Score que hereda de turtle, ver score.py
score=Score()

#Creamos objeto de la clase snake 'ver snake.py'
snake=Snake()

food=Food()

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
    
    # Hace una pausa de 0.1 segundos,  Sin esta línea, el juego se actualizaría tan rápido como sea posible, lo que podría hacer que sea difícil de jugar.
    time.sleep(0.1)
    
    # se utiliza para forzar a la pantalla a actualizar y mostrar todos los cambios que se han hecho desde la última actualización.
    screen.update()
    
    #llamamos al metodo snake_move() de la clase Snake en el archivo snake.py
    snake.snake_move()
    
        
    #comparo la distancia entre la posicion de la cabeza de la snake con la distancia a la food
    if snake.snake_list[0].distance(food) < 15:
                        
        #mueve la food a una nueva posicion food.py  
        food.new_position()
                        
        #agrega 1 turtle con shape'square' al snake (snake.py)
        snake.add_segment()
        
        score.add_score()
    
    #si la snake choca con la pared del juego    
    if snake.snake_list[0].xcor()>286 or snake.snake_list[0].xcor()<-286 or snake.snake_list[0].ycor()>286 or snake.snake_list[0].ycor()<-286:
        
        game_is_on = False
        
        score.end_game()
        
   # Dectectamos colision de la snake consigo misma
    for i in range(1, len(snake.snake_list)):    
        
        # Comprobamos la distancia entre la cabeza de la serpiente y el resto de segmentos del cuerpo
        if snake.snake_list[0].distance(snake.snake_list[i]) < 5:  
            
            # Si la distancia es menor que 10, hay una colisión y el juego termina
            game_is_on = False
            score.end_game()

       
   
    



# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()
