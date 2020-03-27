# dog and fire car2
import turtle,time
wn=turtle.Screen()
wn.setup(2000,1000)
wn.bgpic('road.gif')
wn.bgcolor('grey')
q=turtle.Turtle()
q1=turtle.Turtle()
t=turtle.Turtle()
image=['car.gif','dog11.gif','dog12.gif','boy11.gif','boy12.gif']

for i in range (5):
    wn.addshape(image[i])
    
q.speed(0)
q.up()
q.hideturtle()
q.goto(-750,-50)
q.shape(image[1])
q.showturtle()

q1.speed(0)
q1.up()
q1.hideturtle()
q1.goto(-900,0)
q1.shape(image[3])
q1.showturtle()

t.up()
t.goto(-500,-300)
t.shape(image[0])
i=0
while True:
    turtle.tracer(2)
    i=i+1
    i1=i%4
    i2=i%2
    #print(q.xcor())
    t.fd(35)
    #time.sleep(0.001)
    
    #turtle.tracer(1)
    if i2==0:
        q1.shape(image[3])
        q1.fd(8)
        time.sleep(0.1)
        
    if i2==1:
        q1.shape(image[4])
        q1.fd(8)
        time.sleep(0.1)
    if i1<2:
        q.shape(image[1])
        q.fd(8)
 
    if i1>1:
                
        q.shape(image[2])
        q.fd(8)
        #time.sleep(0.5)

    if t.xcor()>1350:
        t.hideturtle()
        t.goto(-600,-300)
        t.showturtle()
    if q.xcor()>1100:
        q.hideturtle()
        q.goto(-750,-50)
        q.shape(image[1])
        q.showturtle()

        q1.hideturtle()
        q1.goto(-900,0)
        q1.shape(image[3])
        q1.showturtle()

