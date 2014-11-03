##LodeRunner
# Bonnie Ishiguro and Nick Francisci

# Implementation Notes
* The baddies navigate using a distant cousin of A*, they will not move if there is no valid path to your current location (and they cannot drop or dig, as you can)
* There are multiple levels (well, 2...) but beware that due to a limitation of the graphics.py library, a new window is created after you beat the previous level. That window is not automatically focused, so you must click it when it appears to enter key commands (it won't register them otherwise)
* Touching the top of the level is always the win condition, but there is only ever one valid path to get there, and you must collect all the gold to reveal it

# Reading our code
* First of all, reconsider the life decisions that have led you to this point
* main.py - contains the game loop and level loading
* drawable.py - the superclass of all tile and character objects in the game, provides a thin wrapper over the graphics.py library. Allows graphics commands such as the win and lose banners
* character.py - contains the player and baddie, as well as the code for our pathfinding
* tiles.py - contains all of the classes and methods pertaining to static level objects, such as bricks, rope, gold, etc.
* event.py - the registry for proactive behaviors (such as hole filling and baddie movement)
* config.py - loads in level settings
* util.py - contains a few utility functions for moving between 1D and 2D arrays and between the screen and model space
