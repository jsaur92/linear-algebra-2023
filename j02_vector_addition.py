#Made by Joe
#6/13/2023
#Template for Manim animation
from tkinter import LEFT, RIGHT
from manim import *
import math
from enum import Enum

#make sure to rename the class!
class VectorAddition(Scene):
    def construct(self):
        
        #title the text to display at the top of the video
        #bar_width the width of the black bar that the title is put on top of.
        def startUp(title="Video", bar_width=4.0):
            #Set up the title and enclosing box
            boxshift = 0.2*DOWN

            color1 = rgb_to_color([115/255, 0, 10/255])

            rect1 = Rectangle(width=13.0, height=6.5, color=color1).shift(0.2*UP+boxshift)
            self.add(rect1)

                #change width of this rectangle as needed
            rect2 = Rectangle(width = bar_width, height=0.5, color=BLACK).shift(3.5*UP+3.5*LEFT + boxshift)
            rect2.set_fill(BLACK, opacity=1)
            self.add(rect2)

                #change text of this title as needed
            title1 = Text(title, color=WHITE, weight=BOLD).scale(0.7)
            title1.shift(3.497*UP+3.507*LEFT+boxshift)
            self.add(title1)
        
        def setGrid(min_x, min_y, max_x, max_y):
            #Set the grid
            grid = Axes(
                x_range=[min_x, max_x, 1],
                y_range=[min_y, max_y, 1],
                x_length=9,
                y_length=5.5,
                tips=False,
                axis_config={"include_numbers": True,
                             "tip_shape": StealthTip},
            ).add_coordinates()
            self.add(grid)
            return grid
        
        #Dynamic Add: adds a mObject to the scene.
        #mObject the mObject to add
        #animate whether or not the change will be animated (uses the Create animation)
        def dynAdd(mObject, animate=True):
            if animate:
                return self.play(Create(mObject))
            else:
                return self.add(mObject)
        
        #Dynamic Remove: removes a mObject from the scene.
        #mObject the mObject to remove
        #animate whether or not the change will be animated (uses the Uncreate animation)
        def dynRemove(mObject, animate=True):
            if animate:
                return self.play(Uncreate(mObject))
            else:
                return self.remove(mObject)
        
        #Dynamic Replace: replaces a mObject with another mObject.
        #mObject1 the mObject to remove
        #mObject2 the mObject to take its place
        #animate whether or not the change will be animated (uses the Transform animation).
        def dynReplace(mObject1, mObject2, animate=True):
            if animate:
                return self.play(Transform(mObject1, mObject2))
            else:
                return self.replace(mObject1, mObject2)
        
        #Dynamic Wait: pauses the video for some time.
        #time the amount of time to wait for
        #animate whether or not the 
        def dynWait(time=1, animate=True):
            if animate:
                self.wait(time)
        
        #Dynamic Group will perform a series of methods based on the changes array, and can animate or not animate them.
        #mObjects an array of mObjects
        #changes an array of ints. 0->add, 1->remove, 2->replace
        #animate whether or not the changes will be animated.
        def dynGroup(mObjects, changes, animate=True):
            if animate == True:
                
                my_args = []
                
                for i in range(len(mObjects)):
                    my_args.append(getAnim(mObjects[i], changes[i]))
                
                self.play(*my_args)
            else:
                for i in range(len(mObjects)):
                    routeChange(mObjects[i], changes[i])
          
        #Helper method for dynGroup
        def getAnim(mObject, change):
            if change == 0:
                return Create(mObject)
            elif change == 1:
                return Uncreate(mObject)
            elif change == 2:
                return Transform(mObject[0], mObject[1])
        
        #Helper method for dynGroup
        def routeChange(mObject, change):
            if change == 0:
                self.add(mObject)
            elif change == 1:
                self.remove(mObject)
            elif change == 2:
                self.remove(mObject[0])
                self.remove(mObject[1])
        
        class VecGroup:
            start = [0, 0]  #array of vector start position
            end = [1, 1]    #array of vector end position
            fill = PURPLE   #color of the vector
            comp = [1, 1]   #component form of the vector
            orientation = UP #where the matrix should be placed in reference to the vector.
            
            show_coords = True
            
            vector = None          #object of the vector
            start_point = None     #object of the vector's start point
            end_point = None       #object of the vector's end point
            start_coords = None    #object of the text that contains the vector's start coordinates
            end_coords = None      #object of the text that contains the vector's end coordinates
            start_bar = None       #black bar placed behind starting coordinates
            end_bar = None         #black bar placed behind ending coordinates
            matrix = None          #object of the vector's matrix
            matrix_bar = None      #black bar placed behind matrix
            
            #example: vec1 = VecGroup([0, 0], [4, 3], fill=BLUE)
            def __init__(self, start, end, fill=PURPLE, orientation=UP, show_coords=True):
                self.start = start
                self.end = end
                self.fill = fill
                self.comp = [end[0]-start[0], end[1]-start[1]]
                self.orientation = orientation
                
                self.show_coords = show_coords
                
                self.vector = self.makeVector()
                self.start_point = self.makePoint(start)
                self.end_point = self.makePoint(end)
                self.start_coords = self.makeCoordText(start)
                self.end_coords = self.makeCoordText(end, flip=True)
                self.start_bar = self.makeBar(self.start_coords)
                self.end_bar = self.makeBar(self.end_coords)
                self.matrix = self.makeMatrix(self.orientation)
                self.matrix_bar = self.makeBar(self.matrix, 1.0, 1.6)
            
            #SETUP METHODS
            def makeVector(self):
                vec = Vector([self.end[0] - self.start[0], self.end[1]-self.start[1]], color=self.fill, z_index=0)
                vec.set_fill(self.fill)
                vec.put_start_and_end_on(
                    grid.coords_to_point(self.start[0], self.start[1]),
                    grid.coords_to_point(self.end[0], self.end[1])
                )
                return vec
            
            def makePoint(self, coords):
                d = Dot(grid.coords_to_point(coords[0], coords[1]), z_index=2)
                d.set_fill(WHITE)
                return d
            
            def makeCoordText(self, coords, flip=False):
                c = Text("(" + str(coords[0]) + ", " + str(coords[1]) + ")", font_size=32, z_index=10)
                
                mod = 1
                if flip:
                    mod = -1
                
                if   (self.end[0] - self.start[0])*mod > 0 and (self.end[1] - self.start[1])*mod > 0:
                    c.next_to(self.vector, 0.5*LEFT + 0.5*DOWN)
                elif (self.end[0] - self.start[0])*mod < 0 and (self.end[1] - self.start[1])*mod > 0:
                    c.next_to(self.vector, 0.5*RIGHT + 0.5*DOWN)
                elif (self.end[0] - self.start[0])*mod < 0 and (self.end[1] - self.start[1])*mod < 0:
                    c.next_to(self.vector, 0.5*RIGHT + 0.5*UP)
                elif (self.end[0] - self.start[0])*mod > 0 and (self.end[1] - self.start[1])*mod < 0:
                    c.next_to(self.vector, 0.5*LEFT + 0.5*UP)
                c.set_fill(self.fill)
                
                return c
            
            def makeBar(self, reference, wid=1.0, hei=0.5, opac=1):
                rec = Rectangle(width=wid, height=hei, color=BLACK, z_index=0)
                rec.set_fill(BLACK, opacity=opac)
                rec.set_x(reference.get_x())
                rec.set_y(reference.get_y())
                return rec
            
            def makeMatrix(self, orientation=UP):
                mat = IntegerMatrix([[self.end[0]-self.start[0]], [self.end[1]-self.start[1]]], z_index=2)
                mat.next_to(self.vector, orientation)
                mat.set_fill(self.fill)
                return mat
            
            def makeMatrixEquation(self, orientation=UP, extension=True):
                if type(extension) == list:
                    if extension[0] == "add":
                        t1 = str(extension[1][0]) + " + " + str(extension[2][0])
                        t2 = str(extension[1][1] )+ " + " + str(extension[2][1])
                    else:
                        t1 = str(extension[1][0]) + " - " + str(extension[2][0])
                        t2 = str(extension[1][1]) + " - " + str(extension[2][1])
                else:
                    t1 = str(self.end[0]) + " - " + str(self.start[0])
                    t2 = str(self.end[1]) + " - " + str(self.start[1])
                    
                mat = Matrix([[t1], [t2]], z_index=2)
                mat.next_to(self.vector, orientation)
                mat.set_fill(self.fill)
                return mat
            
            #ANIMATION METHODS
            def addVecGroup(self, anim=True, extend=False, wait=2):
                if self.show_coords:
                    dynAdd(self.start_bar, False)
                    dynGroup([self.start_point, self.start_coords], [0, 0], anim)
                else:
                    dynAdd(self.start_point, anim)
                
                dynAdd(self.vector, anim)
                
                if self.show_coords:
                    dynAdd(self.end_bar, False)
                    dynGroup([self.end_point, self.end_coords], [0, 0], anim)
                else:
                    dynAdd(self.end_point, anim)
                    
                dynWait(1, anim)
                
                if extend:
                    mat_a = self.makeMatrixEquation(extension=extend)
                    bar_a = self.makeBar(mat_a, 1.6, 1.6)
                    dynAdd(bar_a, False)
                    dynAdd(mat_a, anim)
                    dynWait(2, anim)
                    dynGroup([[bar_a, self.matrix_bar], [mat_a, self.matrix]], [2, 2], anim)
                    dynRemove(bar_a, False)
                    dynRemove(mat_a, False)
                    dynAdd(self.matrix_bar, False)
                    dynAdd(self.matrix, False)
                else:
                    dynAdd(self.matrix_bar, False)
                    dynAdd(self.matrix, anim)
                    
                dynWait(wait, anim)
            
            def removeVecGroup(self, anim=True, wait=2):
                if self.show_coords:
                    dynGroup([self.start_point, self.start_coords], [1, 1], anim)
                    dynRemove(self.start_bar, False)
                else:
                    dynRemove(self.start_point, anim)
                dynRemove(self.vector, anim)
                if self.show_coords:
                    dynGroup([self.end_point, self.end_coords], [1, 1], anim)
                    dynRemove(self.end_bar, False)
                else:
                    dynRemove(self.end_point, anim)
                dynWait(1, anim)
                dynRemove(self.matrix, anim)
                dynRemove(self.matrix_bar, False)
                
                dynWait(wait, anim)
            
            def replaceVecGroup(self, other, anim=True, wait=2):
                
                group = [
                    [self.vector, other.vector],
                    [self.start_point, other.start_point],
                    [self.end_point, other.end_point],
                    [self.matrix, other.matrix],
                    [self.matrix_bar, other.matrix_bar]
                    ]
                
                if self.show_coords or other.show_coords:
                    group.extend([
                    [self.start_coords, other.start_coords],
                    [self.end_coords, other.end_coords],
                    [self.start_bar, other.start_bar],
                    [self.end_bar, other.end_bar]
                    ])
                    
                dynGroup( group, [2, 2, 2, 2, 2, 2, 2, 2, 2] )
                
                dynWait(wait, anim)
        
        #IMPORTANT
        anim = True #this variable controls whether or not most animations happen. set to True when exporting video.
        startUp("Vector Addition", 4.0) #Sets up the background of the video.
        grid = setGrid(-3, -1, 9, 7) #Sets up the grid for the video. The Grid object can now be referred to by the grid variable.
        
        
        #START CODE HERE:
        
        #first vector to add
        vec1 = VecGroup([1, 1], [4, 3], fill=RED, orientation=DOWN, show_coords=False)
        vec1.addVecGroup(anim)

        #second vector to add
        vec2 = VecGroup([5, 2], [6, 5], fill=BLUE, orientation=RIGHT*2, show_coords=False)
        vec2.addVecGroup(anim)

        #second vector to add, but moved to the first one's end
        vec2_1 = VecGroup([4, 3], [5, 6], fill=BLUE, orientation=RIGHT*2, show_coords=False)
        vec2.replaceVecGroup(vec2_1, anim, wait=1)

        #sum of vectors 1 and 2
        vec3 = VecGroup([1, 1], [5, 6], fill=PURPLE, orientation=UP, show_coords=False)
        vec3.addVecGroup(anim, extend=["add", [3, 2], [1, 3]])
        
        dynWait(3, anim)
        
        
        
        
        