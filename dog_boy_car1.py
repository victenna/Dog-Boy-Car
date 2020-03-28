# dog and fire car2
import turtle,time
wn=turtle.Screen()
wn.setup(2000,1000)
wn.bgpic('road.gif')
wn.bgcolor('grey')
turtle.tracer(2)

car=turtle.Turtle()
car.up()
car_image=['car21.gif','car22.gif','car23.gif','car24.gif']
for i in range(4):
    wn.addshape(car_image[i])
car.shape(car_image[0])
car.hideturtle()
car.goto(-900,-270)
car.showturtle()

dog=turtle.Turtle()
dog_image=['dogy0.gif','dogy1.gif','dogy2.gif','dogy3.gif','dogy4.gif','dogy5.gif',\
           'dogy6.gif','dogy7.gif','dogy8.gif','dogy9.gif']
for i in range (10):
    wn.addshape(dog_image[i])

dog.shape(dog_image[3])
dog.up()
dog.goto(-600,-40)
dog.showturtle() 

i=0
while True:
    i=i+1
    i0=i%4
    
    car.shape(car_image[i0])
    car.fd(40)
    time.sleep(0.1)
    i1=i%10
    dog.shape(dog_image[i1])
    dog.fd(10)
    #time.sleep(0.03)
    if car.xcor()>1350:
        car.hideturtle()
        car.goto(-900,-270)
        car.shape(car_image[0])
        car.showturtle()
    if dog.xcor()>1200:
        dog.hideturtle()
        dog.goto(-600,-40)
        dog.shape(dog_image[i1])
        dog.showturtle()

