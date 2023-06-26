#Made by Joe
#6/26/2023
from tkinter import LEFT, RIGHT
from manim import *
import math
from enum import Enum

class Vectors3D(ThreeDScene):
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
                self.set_camera_orientation(phi=45*DEGREES, theta=-45*DEGREES , zoom=0.9)
            
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
        
        
        
        #IMPORTANT
        anim = True #this variable controls whether or not most animations happen. set to True when exporting video.
        startUp("3D Vectors", 2.8) #Sets up the background of the video.
        grid = setGrid(-6, -4, -4, 6, 4, 4, anim) #Sets up the grid for the video. The Grid object can now be referred to by the grid variable.
        
        
        #START CODE HERE:
        #for some reason, the vector is adding about 1 to its coordinates in each direction, so the endpoint coords are all about 1 less here than they actually are.
        vec1 = Arrow3D([0, 0, 0], [3, 0, 0], color=PURPLE)
        vec2 = Arrow3D([0, 0, 0], [3, 1.25, 0], color=PURPLE)
        vec3 = Arrow3D([0, 0, 0], [3, 1.25, 2], color=PURPLE)
        
        line1 = Group()
        line1.add(Line3D([0, 0, 0], [0.333, 0, 0], color=RED))
        line1.add(Line3D([0.667, 0, 0], [1, 0, 0], color=RED))
        line1.add(Line3D([1.333, 0, 0], [1.667, 0, 0], color=RED))
        line1.add(Line3D([2, 0, 0], [2.333, 0, 0], color=RED))
        line1.add(Line3D([2.667, 0, 0], [3, 0, 0], color=RED))
        
        line2 = Group()
        line2.add(Line3D([3, 0, 0], [3, 0.25, 0], color=GREEN))
        line2.add(Line3D([3, 0.5, 0], [3, 0.75, 0], color=GREEN))
        line2.add(Line3D([3, 1, 0], [3, 1.25, 0], color=GREEN))
        
        line3 = Group()
        line3.add(Line3D([3, 1.25, 0], [3, 1.25, 0.25], color=BLUE))
        line3.add(Line3D([3, 1.25, 0.5], [3, 1.25, 0.75], color=BLUE))
        line3.add(Line3D([3, 1.25, 1], [3, 1.25, 1.25], color=BLUE))
        line3.add(Line3D([3, 1.25, 1.5], [3, 1.25, 1.75], color=BLUE))
        
        sym0 = Group()
        sym0.add(Tex(r"$\vec{u}$ = ", color=PURPLE, fill_opacity=0, font_size=96))
        sym0[0].shift(LEFT)
        t1 = Text("0", color=GRAY)
        t2 = Text("0", color=GRAY)
        t3 = Text("0", color=GRAY)
        sym0.add(MobjectMatrix([[t1], [t2], [t3]]))
        sym0[1].set_fill(PURPLE, opacity=0)
        sym0[1].shift(RIGHT*0.5)
        sym0.move_to([-4.5, 1.7, 0.])
        self.add_fixed_in_frame_mobjects(sym0)
        
        sym1 = Group()
        sym1.add(Tex(r"$\vec{u}$ = ", color=PURPLE, font_size=96))
        sym1[0].shift(LEFT)
        t1 = Text("4", color=RED)
        t2 = Text("0", color=GRAY)
        t3 = Text("0", color=GRAY)
        sym1.add(MobjectMatrix([[t1], [t2], [t3]]))
        #sym1[1].set_fill(PURPLE)
        sym1[1].shift(RIGHT*0.5)
        sym1.move_to([-4.5, 1.7, 0.])
        
        sym2 = Group()
        sym2.add(Tex(r"$\vec{u}$ = ", color=PURPLE, font_size=96))
        sym2[0].shift(LEFT)
        t1 = Text("4", color=RED)
        t2 = Text("2", color=GREEN)
        t3 = Text("0", color=GRAY)
        sym2.add(MobjectMatrix([[t1], [t2], [t3]]))
        #sym2[1].set_fill(PURPLE)
        sym2[1].shift(RIGHT*0.5)
        sym2.move_to([-4.5, 1.7, 0.])
        
        sym3 = Group()
        sym3.add(Tex(r"$\vec{u}$ = ", color=PURPLE, font_size=96))
        sym3[0].shift(LEFT)
        t1 = Text("4", color=RED)
        t2 = Text("2", color=GREEN)
        t3 = Text("3", color=BLUE)
        sym3.add(MobjectMatrix([[t1], [t2], [t3]]))
        #sym3[1].set_fill(PURPLE)
        sym3[1].shift(RIGHT*0.5)
        sym3.move_to([-4.5, 1.7, 0.])
        
        dynAdd(line1, anim)
        dynWait(1, anim)
        dynAdd(vec1, anim)
        dynReplace(sym0, sym1, anim)
        dynWait(2, anim)
        
        dynAdd(line2, anim)
        dynWait(1, anim)
        dynReplace(vec1, vec2, anim)
        dynReplace(sym0, sym2, anim)
        dynWait(2, anim)
        
        dynAdd(line3, anim)
        dynWait(1, anim)
        dynReplace(vec1, vec3, anim)
        dynReplace(sym0, sym3, anim)
        dynWait(2, anim)
        
        if anim:
            self.move_camera(phi=45*DEGREES, theta=45*DEGREES , zoom=0.9)
            self.move_camera(phi=45*DEGREES, theta=(45+90)*DEGREES , zoom=0.9)
            self.move_camera(phi=45*DEGREES, theta=(45+180)*DEGREES , zoom=0.9)
            self.move_camera(phi=45*DEGREES, theta=(45+270)*DEGREES , zoom=0.9)
        
        
        
        
        