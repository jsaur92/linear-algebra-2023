#Made by Joe
#6/28/2023
from tkinter import LEFT, RIGHT
from manim import *
import math
from enum import Enum

class EquivalentVectors3D(ThreeDScene):
    def construct(self):
        
        #title the text to display at the top of the video
        #bar_width the width of the black bar that the title is put on top of.
        def startUp(title="Video", bar_width=4.0):
            #Set up the title and enclosing box
            boxshift = 0.2*DOWN

            color1 = rgb_to_color([115/255, 0, 10/255])

            rect1 = Rectangle(width=13.0, height=6.5, color=color1).shift(0.2*UP+boxshift)
            self.add_fixed_in_frame_mobjects(rect1)

                #change width of this rectangle as needed
            rect2 = Rectangle(width = bar_width, height=0.5, color=BLACK).shift(3.5*UP+3.5*LEFT + boxshift)
            rect2.set_fill(BLACK, opacity=1)
            self.add_fixed_in_frame_mobjects(rect2)

                #change text of this title as needed
            title1 = Text(title, color=WHITE, weight=BOLD).scale(0.7)
            title1.shift(3.497*UP+3.507*LEFT+boxshift)
            self.add_fixed_in_frame_mobjects(title1)
        
        def setGrid(min_x, min_y, min_z, max_x, max_y, max_z, anim=True):
            #Set the grid
            grid = ThreeDAxes(
                x_range=[min_x, max_x, 1],
                y_range=[min_y, max_y, 1],
                z_range=[min_z, max_z, 1],
                x_length=9,
                y_length=5.5,
                z_length=5.5,
                tips=False,
                axis_config={"include_numbers": True,
                             "tip_shape": StealthTip},
            ).add_coordinates()
            self.add(grid)
            
            if anim:
                self.move_camera(phi=45*DEGREES, theta=-45*DEGREES , zoom=0.9)
            else:
                self.set_camera_orientation(phi=55*DEGREES, theta=-45*DEGREES , zoom=0.9)
            
            return grid
        
        #Dynamic Add: adds a mObject to the scene.
        #mObject the mObject to add
        #animate whether or not the change will be animated (uses the Create animation)
        def dynAdd(mObject, animate=True):
            if animate:
                if type(mObject) == Group:
                    dynGroup(mObject.submobjects, dg.add, animate=animate)
                else:
                    return self.play(Create(mObject))
            else:
                return self.add(mObject)
        
        #Dynamic Remove: removes a mObject from the scene.
        #mObject the mObject to remove
        #animate whether or not the change will be animated (uses the Uncreate animation)
        def dynRemove(mObject, animate=True):
            if animate:
                if type(mObject) == Group:
                    dynGroup(mObject.submobjects, dg.remove, animate=animate)
                else:
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
                self.remove(mObject1)
                mObject1 = mObject2.copy()
                return self.add(mObject1)
        
        #Dynamic Wait: pauses the video for some time.
        #time the amount of time to wait for
        #animate whether or not the 
        def dynWait(time=1, animate=True):
            if animate:
                self.wait(time)
        
        #enum for the dynGroup function. You can use these values for the changes parameter, such as [dg.add] instead of [0].
        dg = Enum('dg', ['add', 'remove', 'replace'])
        
        #Dynamic Group will perform a series of methods based on the changes array, and can animate or not animate them.
        #mObjects an array of mObjects
        #changes an array of ints. 1->add, 2->remove, 3->replace. Can also be a single int, and will apply that change to all mObjects.
        #animate whether or not the changes will be animated.
        def dynGroup(mObjects, changes, animate=True):
            
            if type(changes) != list:
                changes = [changes]
            for i in range(len(changes)):
                changes[i] = DGcorrectEnum(changes[i])
            if len(changes) < len(mObjects):
                fix = True
                first = changes[0]
                for i in range(len(changes)):
                    if changes[i] != first:
                        fix = False
                if fix:
                    while len(changes) < len(mObjects):
                        changes.append(first)
            
            if animate:
                
                my_args = []
                for i in range(len(mObjects)):
                    if type(mObjects[i]) == Group:
                        dynGroup(mObjects[i], changes[i], animate)
                    else:
                        my_args.append(getAnim(mObjects[i], changes[i]))
                self.play(*my_args)
            else:
                for i in range(len(mObjects)):
                    routeChange(mObjects[i], changes[i])
          
        #Helper method for dynGroup
        def getAnim(mObject, change):
            if type(mObject) != Group:
                if change == 1:
                    return Create(mObject)
                elif change == 2:
                    return Uncreate(mObject)
                elif change == 3:
                    return Transform(mObject[0], mObject[1])
        
        #Helper method for dynGroup
        def routeChange(mObject, change):
            if change == 1:
                self.add(mObject)
            elif change == 2:
                self.remove(mObject)
            elif change == 3:
                self.remove(mObject[0])
                self.remove(mObject[1])
        
        #Helper method for dynGroup. Converts dgEnum into an int that dynGroup can use.
        def DGcorrectEnum(change):
            if change == dg.add:
                return 1
            elif change == dg.remove:
                return 2
            elif change == dg.replace:
                return 3
            else:
                return change
        
        #method only used in k02
        def sameVec(start=[0,0,0]):
            end_x = 1
            end_y = 1
            end_z = 1
            vec = Arrow3D(start, [start[0]+end_x, start[1]+end_y, start[2]+end_z], color=PURPLE)
            return vec
        
        #IMPORTANT
        anim = True #this variable controls whether or not most animations happen. set to True when exporting video.
        startUp("Equivalent Vectors 3D", 5.5) #Sets up the background of the video.
        grid = setGrid(-6, -4, -4, 6, 4, 4, anim) #Sets up the grid for the video. The Grid object can now be referred to by the grid variable.
        
        
        
        #START CODE HERE:
        vec0 = sameVec()
        vec1 = sameVec()
        vec2 = sameVec([1, -2, 1])
        vec3 = sameVec([-2, 1, -1.5])
        vec4 = sameVec([-1.5, -1, -1.5])
        vec5 = sameVec([1.5, -1.5, -2])
        
        dynGroup([vec0, vec1], dg.add, anim)
        dynWait(1, anim)
        vecA = vec0.copy()
        dynReplace(vecA, vec2, anim)
        dynWait(1, anim)
        vecB = vec0.copy()
        dynReplace(vecB, vec3, anim)
        vec1 = vec0.copy()
        dynWait(1, anim)
        vecC = vec0.copy()
        dynReplace(vecC, vec4, anim)
        vec1 = vec0.copy()
        dynWait(1, anim)
        vecD = vec0.copy()
        dynReplace(vecD, vec5, anim)
        dynWait(1, anim)
        
        if anim:
            self.move_camera(phi=45*DEGREES, theta=45*DEGREES , zoom=0.9)
            dynWait(1, anim)
            self.move_camera(phi=45*DEGREES, theta=(45+90)*DEGREES , zoom=0.9)
            dynWait(1, anim)
            self.move_camera(phi=45*DEGREES, theta=(45+180)*DEGREES , zoom=0.9)
            dynWait(1, anim)
            self.move_camera(phi=45*DEGREES, theta=(45+270)*DEGREES , zoom=0.9)
            dynWait(1, anim)
        
        dynGroup([vecA, vecB, vecC, vecD], dg.remove, False)
        dynGroup([[vec2, vec0], [vec3, vec0], [vec4, vec0], [vec5, vec0]], dg.replace, anim)
        dynWait(3, anim)
        
        
        