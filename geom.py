# geom.py
# Walker M. White (wmw2)
# August 20, 2015
"""Module that provides tuple objects for geometry objects.

This module is not meant to be an exhaustive linear algebra packet (though it may
be at one day). It is solely for in class demonstrations.

Currently, this module provides classes for tuples, points, vectors.  The tuples are 
the base class, while points and vectors are subclasses."""
import numpy
import math
import copy


class Tuple2(object):
    """An instance is a tuple in 2D space.  
    
    This serves as the base class for both Point2 and Vector2."""
    
    # MUTABLE ATTRIBUTES
    @property
    def x(self):
        """The x coordinate
        
        **Invariant**: Value must be a float. If assigned an int, it will be typecast 
        to a float (possibly raising a TypeError)."""
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = float(value)
    
    @x.deleter
    def x(self):
        del self._x 
    
    @property
    def y(self):
        """The y coordinate
        
        **Invariant**: Value must be a float. If assigned an int, it will be typecast 
        to a float (possibly raising a TypeError)."""
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = float(value)
    
    @y.deleter
    def y(self):
        del self._y     
    
    
    # BUILT-IN METHODS
    def __init__(self, x=0, y=0):
        """**Constructor**: creates a new Tuple2 value (x,y).
        
            :param x: initial x value
            **Precondition**: value is an int or float.
            
            :param y: initial y value
            **Precondition**: value is an int or float.
        
        All values are 0.0 by default.
        """
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """**Returns**: True if self and other are equivalent Tuple2s. 
        
        This method uses numpy to test whether the coordinates are 
        "close enough".  It does not require exact equality for floats.
        
            :param other: value to compare against
        """        
        return (type(other) == Tuple2 and numpy.allclose(self.list(),other.list()))
    
    def __ne__(self, other):
        """**Returns**: True if self and other are not equivalent Tuple2s. 
        
            :param other: value to compare against
        """
        return not self == other
    
    def __str__(self):
        """**Returns**: Readable String representation of this Tuple2. """
        return "("+str(self.x)+","+str(self.y)+")"
    
    def __repr__(self):
        """**Returns**: Unambiguous String representation of this Tuple2. """
        return "%s%s" % (self.__class__,self.__str__())
    
    def __add__(self, other):
        """**Returns**: the sum of self and other.
        
        The value returned has the same type as self (so it is either a Tuple2
        or a subclass of Tuple2).  The contents of this object are not altered.
        
            :param other: tuple value to add
            **Precondition**: value has the same type as self.
        """
        assert (type(other) == type(self)), "value %(value)s is not a of type %(type)s" % {'value': `other`, 'type':`type(self)`}
        result = copy.copy(self)
        result.x += other.x
        result.y += other.y
        return result
    
    def __mul__(self, scalar):
        """**Returns**: the scalar multiple of self and other.
        
        The value returned is a new Tuple2.  The contents of this Tuple2
        are not altered.
        
            :param scalar: scalar to multiply by
            **Precondition**: value is an int or float.
        """
        assert (type(scalar) in [int,float]), "value %s is not a number" % `scalar`
        result = copy.copy(self)
        result.x *= scalar
        result.y *= scalar
        return result
    
    def __rmul__(self, scalar):
        """**Returns**: the scalar multiple of self and other.
        
        The value returned is a new Tuple2.  The contents of this Tuple2
        are not altered.
        
            :param scalar: scalar to multiply by
            **Precondition**: value is an int or float.
        """
        assert (type(scalar) in [int,float]), "value %s is not a number" % `scalar`
        result = copy.copy(self)
        result.x *= scalar
        result.y *= scalar
        return result
    
    # PUBLIC METHODS
    def copy(self):
        """**Returns**: A copy of this Tuple2"""
        return Tuple2(self.x, self.y)

    def list(self):
        """**Returns**: A python list with the contents of this Tuple2."""
        return [self.x,self.y]
    
    def abs(self): 
        """Sets each component of this Tuple2 to its absolute value."""
        self.x = abs(self.x)
        self.y = abs(self.y)
    
    def clamp(self,low,high): 
          """Clamps this tuple to the range [low, high].
          
          Any value in this Vector less than low is set to low.  Any
          value greater than high is set to high."""
          self.x = max(low,min(high,self.x))
          self.y = max(low,min(high,self.y))
    
    def interpolate(self, other, alpha):
        """**Returns**: the interpolation of self and other via alpha.
        
        The value returned has the same type as self (so it is either
        a Tuple2 or is a subclass of Tuple2).  The contents of this object
        are not altered. The resulting value is 
        
            alpha*self+(1-alpha)*other 
        
        according to Tuple2 addition and scalar multiplication.
        
            :param other: tuple value to interpolate with
            **Precondition**: value has the same type as self.
            
            :param alpha: scalar to interpolate by
            **Precondition**: value is an int or float.
        """
        assert (type(other) == type(self)), "value %(value)s is not a of type %(type)s" % {'value': `other`, 'type':`type(self)`}
        assert (type(alpha) in [int,float]), "value %s is not a number" % `alpha`
        return alpha*self+(1-alpha)*other


class Point2(Tuple2):
    """An instance is a point in 2D space.
    
    This class is a subclass of Tuple2 and inherits all of its attributes and methods.
    """
    
    # BUILT_IN METHODS
    def __init__(self, x=0, y=0):
        """**Constructor**: creates a new Point value (x,y).
        
            :param x: initial x value
            **Precondition**: value is an int or float.
        
            :param y: initial y value
            **Precondition**: value is an int or float.
        
        All values are 0.0 by default.
        """
        Tuple2.__init__(self,x,y)
    
    def __eq__(self, other):
        """**Returns**: True if self and other are equivalent Points. 
        
        This method uses numpy to test whether the coordinates are 
        "close enough".  It does not require exact equality for floats.
        
            :param other: value to compare against
        """        
        return (type(other) ==  Point2 and numpy.allclose(self.list(),other.list()))
    
    def __sub__(self, tail):
        """**Returns**: the Vector from tail to self.
        
        The value returned is a Vector2 with this point at its head.
        
            :param tail: the tail value for the new Vector
            **Precondition**: value is a Point2 object.
        """
        assert (isinstance(tail, Point2)), "value %s is not a Point2" % `tail`
        return Vector2(self.x-tail.x,self.y-tail.y)
    
    
    # PUBLIC METHODS
    def copy(self):
        """**Returns**: A copy of this Point2"""
        return Point2(self.x, self.y)
    
    def distanceTo(self, other):
        """**Returns**: the Euclidean distance from this point to other
        
            :param other: value to compare against
            **Precondition**: value is a Tuple2 object.
        """
        assert (isinstance(tail, Tuple2)), "value %s is not a Tuple2" % `tail`
        return math.sqrt((self.x-other.x)*(self.x-other.x)+
                         (self.y-other.y)*(self.y-other.y))


class Vector2(Tuple2):
    """An instance is a Vector in 2D space.
    
    This class is a subclass of Tuple2 and inherits all of its attributes and methods.
    """
    
    # BUILT-IN METHODS
    def __init__(self, x=0, y=0):
        """**Constructor**: creates a new Vector object (x,y,z).
        
            :param x: initial x value
            **Precondition**: value is an int or float.
        
            :param y: initial y value
            **Precondition**: value is an int or float.
        
            :param z: initial z value
            **Precondition**: value is an int or float.
        
        All values are 0.0 by default.        
        """
        Tuple2.__init__(self,x,y)
    
    def __eq__(self, other):
        """**Returns**: True if self and other are equivalent Vectors. 
        
        This method uses numpy to test whether the coordinates are 
        "close enough".  It does not require exact equality for floats.
        
            :param other: value to compare against
        """
        return (type(other) == Vector2 and numpy.allclose(self.list(),other.list()))
    
    def __str__(self):
        """**Returns**: A readable String representation of this Vector. """
        return "<"+str(self.x)+","+str(self.y)+">"
    
    def __sub__(self, other):
        """**Returns**: the difference between this Vector and other.
        
        The value returned is a new Vector.  The contents of this vector are not
        modified.
        
            :param other: the Vector to subtract
            **Precondition**: value is a Vector2 object.
        """
        assert (isinstance(other, Vector2)), "value %s is not a Vector2" % `other`
        return Vector2(self.x-other.x,self.y-other.y)
    
    
    # PUBLIC METHODS
    def copy(self):
        """**Returns**: A copy of this Vector2"""
        return Vector2(self.x, self.y)
    
    def length(self):
        """**Returns**: the length of this Vector."""
        return math.sqrt(self.x*self.x+self.y*self.y)
    
    def length2(self):
        """**Returns**: the square of the length of this Vector."""
        return self.x*self.x+self.y*self.y
    
    def angle(self,other):
        """**Returns**: the angle between this vector and other.
        
        The answer provided is in radians. Neither this Vector nor
        other may be the zero vector.
        
            :param other: value to compare against
            **Precondition**: value is a nonzero Vector2 object.
        
        """
        assert (isinstance(other, Vector2)), "value %s is not a Vector2" % `other`
        
        na = self.length()
        nb = other.length()
        assert (na != 0), "Vector %s is zero" % `self`
        assert (nb != 0), "Vector %s is zero" % `other`
        
        return math.acos(self.dot(other)/(na*nb))
    
    def perp(self):
        """**Returns**: a 2D vector perpendicular to this one.
        
        The result of this method is a new Vector2"""
        return Vector2(self.y, -self.x)
    
    def dot(self,other):
        """**Returns**: the dot product between self and other.
        
        The result of this method is a float.
            
            :param other: value to dot
            **Precondition**: value is a Vector2 object.
        """
        assert (isinstance(other, Vector2)), "value %s is not a Vector" % `other`
        return (self.x*other.x+self.y*other.y)
    
    def projection(self,other):
        """**Returns**: the projection of this vector on to other.
        
        The result of this method is a new Vector2
        
            :param other: value to project on to
            **Precondition**: value is a Vector2 object.
        """
        assert (isinstance(other, Vector2)), "value %s is not a Vector2" % `other`
        dot  = self.dot(other)
        base = other.length2()
        return (dot/base)*other
    
    def normalize(self):
        """Normalizes this Vector in place.
        
        This method alters the Vector so that it has the same direction, 
        but its length is now 1.
        """
        length = self.length()
        self.x /= length
        self.y /= length


class Tuple3(object):
    """An instance is a tuple in 3D space.  
    
    This serves as the base class for both Point3 and Vector3."""
    
    # MUTABLE ATTRIBUTES
    @property
    def x(self):
        """The x coordinate
        
        **Invariant**: Value must be a float. If assigned an int, it will be typecast 
        to a float (possibly raising a TypeError)."""
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = float(value)
    
    @x.deleter
    def x(self):
        del self._x 
    
    @property
    def y(self):
        """The y coordinate
        
        **Invariant**: Value must be a float. If assigned an int, it will be typecast 
        to a float (possibly raising a TypeError)."""
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = float(value)
    
    @y.deleter
    def y(self):
        del self._y     
    
    @property
    def z(self):
        """The z coordinate
        
        **Invariant**: Value must be a float. If assigned an int, it will be typecast 
        to a float (possibly raising a TypeError)."""
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = float(value)
    
    @z.deleter
    def z(self):
        del self._z     
    
    
    # BUILT-IN METHODS
    def __init__(self, x=0, y=0, z=0):
        """**Constructor**: creates a new Tuple3 value (x,y,z).
        
            :param x: initial x value
            **Precondition**: value is an int or float.
            
            :param y: initial y value
            **Precondition**: value is an int or float.
            
            :param z: initial z value
            **Precondition**: value is an int or float.
        
        All values are 0.0 by default.
        """
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, other):
        """**Returns**: True if self and other are equivalent Tuple3s. 
        
        This method uses numpy to test whether the coordinates are 
        "close enough".  It does not require exact equality for floats.
        
            :param other: value to compare against
        """        
        return (type(other) == Tuple3 and numpy.allclose(self.list(),other.list()))
    
    def __ne__(self, other):
        """**Returns**: True if self and other are not equivalent Tuple3s. 
        
            :param other: value to compare against
        """
        return not self == other
    
    def __str__(self):
        """**Returns**: Readable String representation of this Tuple3. """
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
    
    def __repr__(self):
        """**Returns**: Unambiguous String representation of this Tuple3. """
        return "%s%s" % (self.__class__,self.__str__())
    
    def __add__(self, other):
        """**Returns**: the sum of self and other.
        
        The value returned has the same type as self (so it is either
        a Tuple3 or is a subclass of Tuple3).  The contents of this object
        are not altered.
        
            :param other: tuple value to add
            **Precondition**: value has the same type as self.
        """
        assert (type(other) == type(self)), "value %(value)s is not a of type %(type)s" % {'value': `other`, 'type':`type(self)`}
        result = copy.copy(self)
        result.x += other.x
        result.y += other.y
        result.z += other.z
        return result
    
    def __mul__(self, scalar):
        """**Returns**: the scalar multiple of self and other.
        
        The value returned is a new Tuple3.  The contents of this Tuple3
        are not altered.
        
            :param scalar: scalar to multiply by
            **Precondition**: value is an int or float.
        """
        assert (type(scalar) in [int,float]), "value %s is not a number" % `scalar`
        result = copy.copy(self)
        result.x *= scalar
        result.y *= scalar
        result.z *= scalar
        return result
    
    def __rmul__(self, scalar):
        """**Returns**: the scalar multiple of self and other.
        
        The value returned is a new Tuple3.  The contents of this Tuple3
        are not altered.
        
            :param scalar: scalar to multiply by
            **Precondition**: value is an int or float.
        """
        assert (type(scalar) in [int,float]), "value %s is not a number" % `scalar`
        result = copy.copy(self)
        result.x *= scalar
        result.y *= scalar
        result.z *= scalar
        return result
    
    # PUBLIC METHODS
    def copy(self):
        """**Returns**: A copy of this Tuple3"""
        return Tuple3(self.x, self.y, self.z)
    
    def list(self):
        """**Returns**: A python list with the contents of this Tuple3."""
        return [self.x,self.y,self.z]
    
    def abs(self): 
        """Sets each component of this Tuple3 to its absolute value."""
        self.x = abs(self.x)
        self.y = abs(self.y)
        self.z = abs(self.z)
    
    def clamp(self,low,high): 
          """Clamps this tuple to the range [low, high].
          
          Any value in this Vector less than low is set to low.  Any
          value greater than high is set to high."""
          self.x = max(low,min(high,self.x))
          self.y = max(low,min(high,self.y))
          self.z = max(low,min(high,self.z))
    
    def interpolate(self, other, alpha):
        """**Returns**: the interpolation of self and other via alpha.
        
        The value returned has the same type as self (so it is either
        a Tuple3 or is a subclass of Tuple3).  The contents of this object
        are not altered. The resulting value is 
        
            alpha*self+(1-alpha)*other 
        
        according to Tuple3 addition and scalar multiplication.
        
            :param other: tuple value to interpolate with
            **Precondition**: value has the same type as self.
            
            :param alpha: scalar to interpolate by
            **Precondition**: value is an int or float.
        """
        assert (type(other) == type(self)), "value %(value)s is not a of type %(type)s" % {'value': `other`, 'type':`type(self)`}
        assert (type(alpha) in [int,float]), "value %s is not a number" % `alpha`
        return alpha*self+(1-alpha)*other


class Point3(Tuple3):
    """An instance is a point in 3 space.
    
    This class is a subclass of Tuple3 and inherits all of its attributes and methods.
    """
    
    # BUILT_IN METHODS
    def __init__(self, x=0, y=0, z=0):
        """**Constructor**: creates a new Point value (x,y,z).
        
            :param x: initial x value
            **Precondition**: value is an int or float.
        
            :param y: initial y value
            **Precondition**: value is an int or float.
        
            :param z: initial z value
            **Precondition**: value is an int or float.
        
        All values are 0.0 by default.
        """
        Tuple3.__init__(self,x,y,z)
    
    def __eq__(self, other):
        """**Returns**: True if self and other are equivalent Points. 
        
        This method uses numpy to test whether the coordinates are 
        "close enough".  It does not require exact equality for floats.
        
            :param other: value to compare against
        """        
        return (type(other) == Point3 and numpy.allclose(self.list(),other.list()))
    
    def __sub__(self, tail):
        """**Returns**: the Vector from tail to self.
        
        The value returned is a Vector with this point at its head.
        
            :param tail: the tail value for the new Vector
            **Precondition**: value is a Point object.
        """
        assert (isinstance(tail, Point3)), "value %s is not a Point" % `tail`
        return Vector3(self.x-tail.x,self.y-tail.y,self.z-tail.z)
    
    
    # PUBLIC METHODS
    def copy(self):
        """**Returns**: A copy of this Point3"""
        return Point3(self.x, self.y, self.z)
    
    def distanceTo(self, other):
        """**Returns**: the Euclidean distance from this point to other
        
            :param other: value to compare against
            **Precondition**: value is a Tuple3 object.
        """
        return math.sqrt((self.x-other.x)*(self.x-other.x)+
                         (self.y-other.y)*(self.y-other.y)+
                         (self.z-other.z)*(self.z-other.z))


class Vector3(Tuple3):
    """An instance is a Vector in 3 space.
    
    This class is a subclass of Tuple3 and inherits all of its attributes and methods.
    """
    
    # BUILT-IN METHODS
    def __init__(self, x=0, y=0, z=0):
        """**Constructor**: creates a new Vector object (x,y,z).
        
            :param x: initial x value
            **Precondition**: value is an int or float.
        
            :param y: initial y value
            **Precondition**: value is an int or float.
        
            :param z: initial z value
            **Precondition**: value is an int or float.
        
        All values are 0.0 by default.        
        """
        Tuple3.__init__(self,x,y,z)
    
    def __eq__(self, other):
        """**Returns**: True if self and other are equivalent Vectors. 
        
        This method uses numpy to test whether the coordinates are 
        "close enough".  It does not require exact equality for floats.
        
            :param other: value to compare against
        """        
        return (type(other) == Vector3 and numpy.allclose(self.list(),other.list()))
    
    def __str__(self):
        """**Returns**: A readable String representation of this Vector. """
        return "<"+str(self.x)+","+str(self.y)+","+str(self.z)+">"
    
    def __sub__(self, other):
        """**Returns**: the difference between this Vector and other.
        
        The value returned is a new Vector.  The contents of this vector are not
        modified.
        
            :param other: the Vector to subtract
            **Precondition**: value is a Vector object.
        """
        assert (type(other) == Vector), "value %s is not a Vector" % `other`
        return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
    
    
    # PUBLIC METHODS
    def copy(self):
        """**Returns**: A copy of this Vector3"""
        return Vector3(self.x, self.y, self.z)
    
    def length(self):
        """**Returns**: the length of this Vector."""
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    
    def length2(self):
        """**Returns**: the square of the length of this Vector."""
        return self.x*self.x+self.y*self.y+self.z*self.z

    def angle(self,other):
        """**Returns**: the angle between this vector and other.
        
        The answer provided is in radians. Neither this Vector nor
        other may be the zero vector.
        
            :param other: value to compare against
            **Precondition**: value is a nonzero Vector3 object.
        
        """
        assert (instance(other, Vector3)), "value %s is not a Vector" % `other`
        
        na = self.length()
        nb = other.length()
        assert (na != 0), "Vector %s is zero" % `self`
        assert (nb != 0), "Vector %s is zero" % `other`
        
        return math.acos(self.dot(other)/(na*nb))
    
    def cross(self,other):
        """**Returns**: the cross product between self and other.
        
        The result of this method is a new Vector3
        
            :param other: value to cross
            **Precondition**: value is a Vector3 object.
        """
        assert (isinstance(other, Vector3)), "value %s is not a Vector" % `other`
        return Vector3(self.y*other.z-self.z*other.y,
                       self.z*other.x-self.z*other.z,
                       self.x*other.y-self.y*other.x)
    
    def dot(self,other):
        """**Returns**: the dot product between self and other.
        
        The result of this method is a float.
            
            :param other: value to dot
            **Precondition**: value is a Vector3 object.
        """
        assert (isinstance(other, Vector3)), "value %s is not a Vector" % `other`
        return (self.x*other.x+self.y*other.y+self.z*other.z)
    
    def projection(self,other):
        """**Returns**: the projection of this vector on to other.
        
        The result of this method is a new Vector2
        
            :param other: value to project on to
            **Precondition**: value is a Vector3 object.
        """
        assert (type(other) == Vector3), "value %s is not a Vector3" % `other`
        dot  = self.dot(other)
        base = other.length2()
        return (dot/base)*other
    
    def normalize(self):
        """Normalizes this Vector in place.
        
        This method alters the Vector so that it has the same direction, 
        but its length is now 1.
        """
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
