# linear-algebra-2023
Videos animated with Python through the Manim library for USC's Linear Algebra course.

These videos are all made from an edited "TEMPLATE" file. The template contains various predefined methods and classes that help streamline the animation process with Manim. As this project continues, the template will be extended with more methods and classes, so make sure to use the most current version of TEMPLATE.py.

#
# Instance Variables:

``anim``

Set to False to disable most animations when testing out the program to make it compile faster, and set to True when exporting the video for a long compile time but full video. Use this variable for the ``animate`` parameter of the dynamic animation methods so that the animations will be consistant. 

``dg``
(fill this out)

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
- ``min_y`` the maximum y-value displayed on the graph. 

#
``dynAdd(mObject, animate=True)``

Adds a mObject to the scene.

- ``mObject`` the mObject or Group of mObjects to add.
- ``animate`` whether or not the animation will be displayed. Uses ``self.play(Create(mObject))`` when true and ``self.add(mObject)`` when false.
