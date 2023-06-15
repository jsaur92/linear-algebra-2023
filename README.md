# linear-algebra-2023
Videos animated with Python through the Manim library for USC's Linear Algebra course.

These videos are all made from an edited "TEMPLATE" file. The template contains various predefined methods and classes that help streamline the animation process with Manim. As this project continues, the template will be extended with more methods and classes, so make sure to use the most current version of ``j00_TEMPLATE.py``.

#
# Attributes:

``anim``

Set to False to disable most animations when testing out the program to make it compile faster, and set to True when exporting the video for a long compile time but full video. Use this variable for the ``animate`` parameter of the dynamic animation methods so that the animations will be consistant. 

``dg``

An enumerator that represents different animations or changes when using ``dynGroup()``.
- ``dg.add`` : 0
- ``dg.remove`` : 1
- ``dg.replace`` : 2

#
# Methods:

``startUp(title="Video", bar_width=4.0)``

Sets up the background and title of the video. Call this at the top of your coding area.

- ``title`` the title of the video to display in the top-left corner. Make sure to change the name of the script to this as well.
- ``bar_width`` the width of the black bar behind the title. The width should be adjusted so that the bar covers the entire title.

#
``setGrid(min_x, min_y, max_x, max_y)``

Sets up and returns the grid that the video should take place in. Use ``grid = setGrid(min_x, min_y, max_x, max_y)`` to call it at the top of your coding area. Objects can still be placed outside of the defined values, so the minimums and maximums are only for the visual part of the graph.

- ``min_x`` the minimum x-value displayed on the graph. 
- ``min_y`` the minimum y-value displayed on the graph. 
- ``max_x`` the maximum x-value displayed on the graph. 
- ``max_y`` the maximum y-value displayed on the graph. 
- returns the object reference of the grid that has been made. Store this in a variable such as ``grid`` and use the statement ``grid.coords_to_point(0, 0)`` to get real coordinates from the grid.

#
``dynAdd(mObject, animate=True)``

Adds a mObject to the scene.

- ``mObject`` the mObject or Group of mObjects to add.
- ``animate`` whether or not the animation will be displayed. Uses ``self.play(Create(mObject))`` when true and ``self.add(mObject)`` when false.
- returns the animation played.

#
``dynRemove(mObject, animate=True)``

Removes a mObject from the scene.

- ``mObject`` the mObject or Group of mObjects to add.
- ``animate`` whether or not the animation will be displayed. Uses ``self.play(Uncreate(mObject))`` when true and ``self.remove(mObject)`` when false.

#
``dynReplace(mObject1, mObject2, animate=True)``

Replaces one mObject from the scene with another.

- ``mObject1`` the mObject to replace. The reference to this mObject will take on all of the atributes from mObject 2 and stay on the screen as mObject1, and mObject2 will never actually be instantiated.
- ``mObject2`` the mObject to appear. This mObject will not actually be instantiated, but instead all of its traits will be given to the first mObject.
- ``animate`` whether or not the animation will be displayed. Uses ``self.play(Transform(mObject1, mObject2))`` when true and ``self.replace(mObject1, mObject2)`` when false.

#
``dynWait(time=1, animate=True)``

Wait for a given amount of time. 

- ``time`` the amount of time to wait for in seconds.
- ``animate`` whether or not the wait will be used. Uses ``self.wait(time)`` when true and skips over this line of code when false.

#
``dynGroup(mObjects, changes, animate=True)``

Performs a group of dynamic animations at once.

- ``mObjects`` the array of mObjects or a Group of mObjects to change.
- ``changes`` an array of integers or values of type ``dg`` enumerators. The corresponding value for the item in ``mObjects`` determines the animation that item will play. See the ``dg`` attribute to see how to input this. You can also use a single integer or enumerator instead of a list to use that animation for every mObject.
- ``animate`` passes on to the animate parameters for the animations that will play.

#
``getAnim(mObject, change)``

``routeChange(mObject, change)``

``DGcorrectEnum(change)``

Helper methods for the ``dynGroup()`` method, there is no need to use or modify these functions.

#
#
