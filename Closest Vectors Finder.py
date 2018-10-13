from math import sqrt
import turtle
vectors=[[10,100],[300,50],[50,120],[60,10],[100,90],[10,200],[30,50]]  # Vectors
def cordinates(): 
    turtle.speed(0)
    a=0
    while a!=4:
        turtle.left(90)
        turtle.forward(300)
        a=a+1
        turtle.goto(0,0)
cordinates()

def minimum_displacement():
    mini_displacement=float("+inf") # setting minimum as infinity in the begining
    for i in vectors:
        for j in vectors:
            if i==j:# if it is comparing same vector skipping it 
                continue    
            displacement=sqrt(((i[0]-j[0])**2)+((i[1]-j[1])**2)) # calculating displacement
            if displacement<mini_displacement:
                mini_displacement=displacement
    return(mini_displacement)
def closest_vectors():
    minimum=minimum_displacement()
    closest_vectors=[]
    for i in vectors:
        turtle.speed(0)
        turtle.showturtle()
        turtle.penup()
        turtle.goto(i[0],i[1])
        turtle.dot()
        turtle.hideturtle()
        
        for j in vectors:
            if i==j:
                continue    
            displacement=sqrt(((i[0]-j[0])**2)+((i[1]-j[1])**2)) # calculating displacement
            if displacement==minimum:
                closest_vectors.append([i,j])
                for a in closest_vectors:
                    ##### To remove duplicates ####
                    for b in closest_vectors:
                        if a==b:
                            continue
                        if a[0]==b[1] and a[1]==b[0]:
                            index_of_duplicates=(closest_vectors.index([i,j])) #finding index of duplcates
                            del closest_vectors[index_of_duplicates] #deleting duplicates
    print("Closest Vectors : ")                   
    for c in closest_vectors:
        print(c)
        turtle.showturtle()
        turtle.penup()
        turtle.goto(c[0][0],c[0][1])
        turtle.pendown()
        turtle.dot("red")
        turtle.goto(c[1][0],c[1][1])
        turtle.dot("red")
        turtle.hideturtle()

closest_vectors()

