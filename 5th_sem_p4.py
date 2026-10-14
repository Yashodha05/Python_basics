#4. Develop a program using turtle graphic, write a program that asks the user for the number of sides, the length of the side, the colour, 
#and fill colour of a regular polygon. The program should draw the polygon and then fill it in. 
import turtle  

#conversion factor 
cm_to_pixels=37.8 

#Users input 

num_sides=int(input("Enter No of sides: ")) 
side_length_cm=float(input("Enter Side_Length: ")) 
side_length=side_length_cm*cm_to_pixels 
pen_color=input("Enter the Pen Color :") 

fill_color=input("Enter the Fill Color :") 
t=turtle.Turtle() 
t.color(pen_color) 
t.fillcolor(fill_color) 

#Draw polygon 
angle=360/num_sides 
t.begin_fill() 
for i in range(num_sides): 
  t.forward(side_length) 
  t.right(angle) 
t.end_fill() 
turtle.done() 
