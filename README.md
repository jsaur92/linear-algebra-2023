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
# Classes:

``VecGroup``

A class that contains a Vector and supporting mObjects that help represent it such as Text for coordinates and a Matrix mObject to represent the Vector's component form.

### VecGroup Attributes:

- ``start`` int array of size 2 that represents the Vector's starting position.
- ``end`` int array of size 2 that represents the Vector's ending position.
- ``fill`` color of the Vector.
- ``comp`` int array of size 2 that represents the component form of the Vector.
- ``orientation`` int array of size 3 that represents where the Matrix representing the component form of the Vector is placed in relation to the Vector.
- ``shift`` int array of size 3 that represents how much the Matrix representing the component form of the Vector should be moved from its starting position.
            
- ``show_coords`` boolean that represents whether or not the coordinates should be shown. If False, does not display the coordinate mObjects and their respective bar mObjects.
            
- ``vector`` object reference of the Vector.
- ``start_point`` object reference of the Point that is at the Vector's start.
- ``end_point`` object reference of the Point that is at the Vector's emd.
- ``start_coords`` object reference of the Text that contains the Vector's start coordinates.
- ``end_coords`` object reference of the Text that contains the Vector's end coordinates.
- ``start_bar`` object reference of the Rectangle placed behind the starting coordinates.
- ``end_bar`` object reference of the Rectangle placed behind the ending coordinates.
- ``matrix`` object reference of the Matrix that represents the Vector's component form.
- ``matrix_bar`` object reference of the Rectangle placed behind the Matrix.

### VecGroup Methods

``makeVector()``

Makes a Vector mObject based on the ``start`` and ``end`` attributes of the VecGroup.

- returns the Vector mObject.

``makePoint(coords)``

Makes a Point mObject located at the ``coords`` parameter.

- ``cords`` int array of size 2 that represents the location on the ``grid`` that the Point will be placed on.
- returns the Point mObject.

``makeCoordText(coords, flip=False)``

Makes a Text mObject with text based on the ``coords`` parameter, and places it at the start or end of the ``vector`` based on ``flip``.

- ``cords`` int array of size 2 that determines what the text on the Text mObject will display.
- ``flip`` boolean that when True places the Text at the end of the Vector and when False places the Text at the start of the Vector.
- returns the Text mObject.

``makeBar(reference, wid=1.0, hei=0.5, opac=1)``

Makes a black Rectange mObject behind the ``reference`` mObject that acts as a background for any mObject that needs to be visible on a black background.

- ``reference`` the mObject that the Rectangle will be placed on.
- ``wid`` the width of the Rectangle.
- ``hei`` the height of the Rectangle.
- ``opac`` the opacity of the Rectangle.
- returns the Rectangle mObject.

``makeMatrix(orientation=UP)``

Makes a Matrix mObject that represents the component form of the Vector.

- ``orientation`` where the Matrix mObject will be placed in reference to the Vector mObject.
- returns the Matrix mObject.

``makeMatrixEquation(orientation=UP, extension=True)``

Makes a complex Matrix mObject that represents the component form of the Vector along with an extra animation based on the ``extension`` parameter.

- ``orientation`` where the Matrix mObject will be placed in reference to the Vector mObject.
- ``extension`` the type of extra animation that will be played. The following are the current extra animations that can be played:
  - ``add``: set ``extension`` to a list of length 3 with ``extension[0]=add``, and index 1 and 2 being int lists of length 2 that represent the two vectors that will be added together to result in this Matrix.
  -  ``subtract``: set ``extension`` to a list of length 3 with ``extension[0]=subtract``, and index 1 and 2 being int lists of length 2 that represent the two vectors that will be subtracted to result in this Matrix.
  -  ``derive``: set ``extension`` to True. The animation will take the ending coordinates and subtract the starting coordinates from it.
- returns the Matrix mObject.

``addVecGroup(anim=True, extend=False, wait=2)``

Uses ``dynAdd()`` to dynamically add the full VecGroup.

- ``anim`` whether or not ``dynAdd()`` will animate or not.
- ``extend`` whether or not the method will use ``makeMatrix()`` or ``makeMatrixEquation()``, and if it uses the latter it will pass on to that method's ``extension`` parameter.
- ``wait`` how long the ``dynWait()`` at the end of this method will play.

``removeVecGroup(anim=True, wait=2)``

Uses ``dynRemove()`` to dynamically remove the full VecGroup.

- ``anim`` whether or not ``dynRemove()`` will animate or not.
- ``wait`` how long the ``dynWait()`` at the end of this method will play.

``replaceVecGroup(other, anim=True, wait=2)``

Uses ``dynReplace()`` to dynamically replace the full VecGroup with another VecGroup.

- ``other`` the other VecGroup that this one will be replaced with.
- ``anim`` whether or not ``dynReplace()`` will animate or not.
- ``wait`` how long the ``dynWait()`` at the end of this method will play.
