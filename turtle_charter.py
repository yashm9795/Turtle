
import turtle  # import module
#filename= input('which file to visualize?')  
#Colortype= input('Which color type do you want?') .lower()
colortype="dark"
filename="/Users/Admin/Desktop/511/a3-turtle-charter-yashm9795/data/sample_data.txt"

#title=input("What should be the chart named?") 
title="Bar Chart"   #title of the file


def count_observation(filename):     #function for computing number of observations in the file
    with open(filename) as fp:        #opening the file using with 
        count=0

        for line in fp:
            count+=1
            
    return count+1

numberofobs= count_observation(filename)
print(int(numberofobs/3))                        #each observation has 3 lines


#feature=input("which feature to consider?")   
feature=1


def get_maximum(filename, feature):   #function for computing the maximum value using the feature and filname arguments

    with open(filename) as fp:          
        count=0
        f=feature +1

        for line in fp:             #using for loop to loop through each line
            count=count+1


            if count==feature +1:       
                maxval=int(line)
            
            if count==f:
                if maxval<=int(line):   #comparing 2 numbers

                    maxval=int(line)       

                f=f+3                   #incrementing the counter by 3
    return(maxval)  
    
                                                #returning the maximum value
max_value=get_maximum(filename,int(feature))    #storing the maximum value in max_value variable
print(max_value)


window = turtle.Screen()                # create a window for the turtle to draw on
window.title(title)                      # the title to show at the top of the window
WINDOW_WIDTH = 900                       # size constants for easy changing
WINDOW_HEIGHT = 500
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)                        # specify window size (width, height)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coordinate system: origin at lower-left



height_factor= WINDOW_HEIGHT/max_value             #calculating the scaling factor for y axis

width_factor=WINDOW_WIDTH/numberofobs              #calculating the scaling factor for x axis


if max_value>=100:                                 #using if else conditions to fix a scale
    scale=20
elif max_value>=50:
    scale=10
elif max_value>=10:
    scale=2
else:
    scale=1


def draw_axes(t):                                  #defining a function that calls all other functions
    draw_y_axis(t)
    draw_x_axis(t)
    draw_y_tickmarks(t)
    draw_xaxis_labels(t)
    draw_bar(t)
    
    

def draw_y_axis(t):                                 #defining a function for drawing the yaxis by passing the turtle as argument
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.forward(WINDOW_HEIGHT+20)                     #length of the y axis
    t.color("black","black")                    
    t.begin_fill()
    t.left(90)
    t.forward(6)
    t.right(135)
    t.forward(10)
    t.backward(10)
    t.right(45)
    t.forward(12)
    t.left(135)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.home()                                    #back to orgin

def draw_x_axis(t):                             #defining a function to draw the xaxis by passing the turtle as argument
    t.pendown()
    t.forward(WINDOW_WIDTH+20)                  #length of the xaxis
    t.color("black","black")
    t.begin_fill()
    t.left(90)
    t.forward(6)
    t.right(135)
    t.forward(10)
    t.backward(10)
    t.right(45)
    t.forward(12)
    t.left(135)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.home()                                    #back to origin 


def draw_y_tickmarks(t):                    #defining a function to draw the y axis tickmarks
    count=int(max_value/scale)                #setting number if tickamrks based on maximum value and scale    
    i=1
    while count >0:

    
        t.left(90)
        t.penup()
        t.forward(scale*height_factor)          #setting up a unform distance between each tickmarks
        t.left(90)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.write(str(i*scale), align="left", font=("Arial",10,"normal"))  #setting the font type and size
        t.right(180)
        t.forward(20)
     
        count-=1
        i+=1
    t.home()

def draw_xaxis_labels(t):                   #defining a function to write the x axis labels                         
  
    count=0
    f=1
    c=1
    with open(filename) as fp:
        for line in fp:

            count+=1

            if count==f:
                t.penup()
                t.home()
                t.goto((width_factor*3*c,-30))     #unformally distributing the xaxis labels by specifying the x and y coordinates
                t.pendown()
                t.write(line,font=('Arial',9,"normal"))  #using the write attribute to specify the name of the labels
                t.penup()
                c=c+1
                f=f+3
    t.home()

def draw_rectangle(t,height,color,c):           #defining a function to draw the rectangles by passing 
    t.penup()
    
    t.goto(width_factor*3*c-5,0)               #indicating the x and y coordinates of thr bar
    t.color(color)        
    t.pendown()                     
    t.begin_fill()
    t.left(90)
    t.forward(height)                           #drawing the bar with the appropriate height
    t.right(90)
    t.forward((width_factor*3*c+15)-(width_factor*3*c-15))      #drawing the width
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    
   

def draw_bar(t):          #defining the function to draw the bars 

    with open(filename) as fp:   # opening the file
        i=1
        c=1
        f=feature+1
        count=0
        for line in fp:         #looping through the file
            count=count +1

            
            if count==f:

                height=int(line)     

                color_val=choose_color(i%4,colortype)   #assigns different colors to alternate bars
                i+=1
                
                if int(line) >0:                    
                    

                    draw_rectangle(t,height*height_factor,color_val,c)   #calling the draw_rectangle function eith the height, width, color and a variable c
                    
                    c+=1

                f=f+3                   #incrementing f by 3
        t.penup()
        t.home()
        
def choose_color(number,colortype):    
                                                      #defining a function for coloring the bars
    if colortype=="dark":

        color_list=["red","blue","green","yellow"]         #defining the list of dark colors

        if number ==1:

            coloris=color_list[number-1]

        elif number==2:

            coloris=color_list[number-1]

        elif number==3:

            coloris=color_list[number-1]

        else:

            coloris=color_list[number-1]
    
    if colortype=="light":                          
        color_list=["skyblue","lightgreen", "pink", "grey"]             #defining the list of light colors
        if number ==1:


            coloris=color_list[number-1]

        elif number==2:

            coloris=color_list[number-1]

        elif number==3:

            coloris=color_list[number-1]

        else:

            coloris=color_list[number-1]
            


    return(coloris)                         #returning the color












t= turtle.Turtle()                         
t.speed("fastest")  
draw_axes(t)                               #Calling the draw_axes function
t.hideturtle()                                            #hiding turtle
window.mainloop()                          
