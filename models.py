# models.py
# Michael Huang (mh999), Jeffrey Tsang (jet253)
# December 3rd, 2016
"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.


class Paddle(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A NEW PADDLE
    def __init__(self, x, bottom, width, height, color):
        """Creates a paddle of Parent class Grectangle
         Initializer: Creates a GRectangle object as the paddle. Paddle is a
        subclass of GRectangle with the given arguments.
        
        Parameter x: The x-coordinate of the paddle
        Precondition: x is a number (int or float)
        
        Parameter bottom: the vertical coordinate of the bottom edge
        of the paddle
        Precondition: bottom is a number(int or float)
        
        Parameter width: the paddle width
        Precondition: width is a number(int or float)>=0
        
        Parameter height:the paddle height
        Precondition: width is a number(int or float)>=0
        
        Parameter color: the paddle color
        Precondition:color is an RGB object of class colormodel"""
        
        GRectangle.__init__(self, x=x, bottom=bottom, width=width,
                            height=height, linecolor=color, fillcolor=color)
    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS
    def move(self,press):
        """Moves the paddle left and right in the bounds of the window
        Sets left attribute to 0 and right attribute to width of game window
        to create boundaries
        
        Parameter: a number added to the x coordinate of the paddle moves
        in one key press
        Precondition: press is a number(int or float)"""
        self.x+=press
        
        if self.left<0:
            self.left=0
        if self.right>GAME_WIDTH:
            self.right=GAME_WIDTH
           
    def collides(self,ball):
        """Returns: True if the ball collides with this brick
            
        Parameter ball: The ball to check
        Precondition: ball is of class Ball"""
        if ball._vy<0:
            return self.contains(ball.x-BALL_RADIUS, ball.y-BALL_RADIUS) or\
        self.contains(ball.x-BALL_RADIUS, ball.y+BALL_RADIUS)or\
        self.contains(ball.x+BALL_RADIUS, ball.y-BALL_RADIUS) or\
        self.contains(ball.x+BALL_RADIUS, ball.y+BALL_RADIUS)
     
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
class Brick(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A BRICK
    def __init__(self, left,y, width, height, color):
         """Initializer: creates a GRectangle object as the brick. Brick is a
         subclass of GRectangle with the given arguments.
        
         Parameter left: The left edge of the paddle
         Precondition: left is a number (int or float)
        
         Parameter y: the vertical coordinate  of the paddle
         Precondition: bottom is a number(int or float)
        
         Parameter width: the paddle width
         Precondition: width is a number(int or float)>=0
        
         Parameter height:the paddle height
         Precondition: width is a number(int or float)>=0
        
         Parameter color: the paddle color
         Precondition:color is an RGB object of class colormodel"""
        
        
         GRectangle.__init__(self, left=left, y=y, width=width, height=height, \
                             linecolor=color, fillcolor=color)
    # METHOD TO CHECK FOR COLLISION
    def collides(self,ball):
         """Returns: True if the ball collides with this brick
            
         Parameter ball: The ball to check
         Precondition: ball is of class Ball"""
         return self.contains(ball.x-BALL_RADIUS, ball.y-BALL_RADIUS) or\
         self.contains(ball.x-BALL_RADIUS, ball.y+BALL_RADIUS)
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Ball(GEllipse):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getVX(self):
        """Returns: velocity in x direction of ball"""
        return self._vx
    
    def getVY(self):
        """Returns: velocity in y direction of ball"""
        return self._vy
    
    def setVY(self, value):
        """Sets vy to value
        Parameter value:value is a number(int or float)"""
        assert (type(value)==int or type(value)==float)
        self._vy=value
      # INITIALIZER TO SET RANDOM VELOCITY
    def __init__(self, x, y, width, height, color):
        """Initializer: creates a GRectangle object as the ball. Ball is a
        subclass of GRectangle with the given arguments for the instance. The
        initializer also sets the default values for attributes _vx and _vy.
        Parameter x: The x coordinate of the paddle
        Precondition: left is a number (int or float)
        
        Parameter y: the y coordinate  of the paddle
        Precondition: bottom is a number(int or float)
        
        Parameter width: the paddle width
        Precondition: width is a number(int or float)>=0
        
        Parameter height:the paddle height
        Precondition: width is a number(int or float)>=0
        
        Parameter color: the paddle color
        Precondition:color is an RGB object of class colormodel"""

        GEllipse.__init__(self, x=x, y=y, width=width, height=height,\
                          fillcolor=color)
        self._vx = random.uniform(1.0,5.0) 
        self._vx = self._vx * random.choice([-1, 1]) 
        self.setVY(-2.0)
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    def step(self):
        """Modifies the x and y attributes of the Ball instance to allow it
        to move at random speeds"""
        self.x=self.x+self._vx
        self.y=self.y+self._vy
        
    def bounce(self):
        """Modifies the _vy and _vx class attributes to be negative when the
        ball object hits any of the four corners of the game window."""
        if self.y>=GAME_HEIGHT:
            self._vy=-self._vy
        if self.x>=GAME_WIDTH:
            self._vx=-self._vx
        if self.x<=0:
            self._vx=-self._vx
        if self.y<=0:
            self._vy=-self._vy
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def bottom(self):
        """Returns: True if the y coordinate of the ball passes through the
        bottom of the screen; False otherwise
        
        Allows the Ball object to pass through the bottom of the game
        window if the player does not catch the ball with the paddle."""
        if self.y<=0:
            return True
        else:
            return False

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE
    