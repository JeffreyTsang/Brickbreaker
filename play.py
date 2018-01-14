# play.py
# Michael Huang (mh999), Jeffrey Tsang (jet253)
# December 3rd, 2016
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *
import random

# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
        _tries  [int >= 0]: the number of tries left 
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY"""
    
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getBrickSize(self):
        """return length of bricks"""
        return len(self._bricks)
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    def __init__(self):
        """Initializer: Creates a list of bricks and creates
        an instance of Paddle with the given parameters in _paddle attribute. 
        _ball is optional. It can be None or a ball."""
        mybricks=[]
        for y in range(0,BRICK_ROWS):
            for x in range(0,BRICKS_IN_ROW):
                brick=Brick(BRICK_SEP_H/2.0+(x*(BRICK_SEP_H+BRICK_WIDTH)),
                            (GAME_HEIGHT-((BRICK_Y_OFFSET)))-
                            y*(BRICK_HEIGHT+BRICK_SEP_V), BRICK_WIDTH,
                            BRICK_HEIGHT, BRICK_COLORS[y])
                mybricks.append(brick)
        self._bricks=mybricks
        self._paddle=Paddle(GAME_WIDTH/2.0, PADDLE_OFFSET, PADDLE_WIDTH,
                            PADDLE_HEIGHT, PADDLE_COLOR)  
        self._ball=None
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    def updatePaddle(self,input):
        """Moves the paddle  to the right or left when a key press is
        detected through input"""
        press = 0
        if input.is_key_down('left'):
            press -=LEFT
        
        if input.is_key_down('right'):
            press +=RIGHT
        self._paddle.move(press)
    
    def makeBall(self):
        """Creates a Ball object in attribute _ball with given parameters"""
        self._ball=Ball(GAME_WIDTH/2.0, GAME_HEIGHT/2.0, BALL_DIAMETER/2.0,
                        BALL_DIAMETER/2.0, BALL_COLOR)
        
    def updateBall(self):
        """Moves the ball, bounces it, and detects for collisions with
        the bricks and the paddle"""
        self._ball.step()
        self._ball.bounce()
        if self._paddle.collides(self._ball):
            self._ball.setVY(-self._ball.getVY())
        for x in self._bricks:
            if x.collides(self._ball):
                self._ball.setVY(-self._ball.getVY())
                self._bricks.remove(x)
                seq=[Sound('bounce.wav'),Sound('saucer1.wav'),Sound('cup1.wav')\
                     ,Sound('saucer1.wav')]
                random.choice(seq).play()       
        return self._ball.bottom() 
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    def draw(self, view):
        """Draws the brick object to the view.
        
        Every single thing you want to draw in this game is a GObject.  To draw a GObject 
        g, simply use the method g.draw(self.view).  It is that easy!
        
        Many of the GObjects (such as the paddle, ball, and bricks) are attributes in Play. 
        In order to draw them, you either need to add getters for these attributes or you 
        need to add a draw method to class Play.  We suggest the latter.  See the example 
        subcontroller.py from class."""
        # IMPLEMENT ME
        for x in self._bricks:
            x.draw(view)
        
        self._paddle.draw(view)
    
        if not self._ball is None:
            self._ball.draw(view)
            
            

   
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
  
        
