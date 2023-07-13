from math import sin,cos,radians
import random

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        if not isinstance(cannonSize, int) or not isinstance(ballSize, int):
            raise Exception("Game constructor arguments invalid", cannonSize, ballSize)

        self.players = [Player(self, False, -90, "blue"), Player(self, True, 90, "red")]
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.currentPlayerNum = 0
        self.currentWind = -10+random.random()*20

    """ A list containing both players """
    def getPlayers(self):
        return self.players

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannonSize

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ballSize

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.players[self.currentPlayerNum]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.players[1 - self.currentPlayerNum]

    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.currentPlayerNum

    """ Switch active player """
    def nextPlayer(self):
        self.currentPlayerNum = 1-self.currentPlayerNum
        if self.currentPlayerNum not in (0,1):
            raise Exception("Current player is: ", self.currentPlayerNum, ". Should be 0 or 1")
        return abs(self.currentPlayerNum - 1)

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        if isinstance(wind,float):
            self.currentWind = wind
        else:
            raise Exception("invalif type for wind parameter: ", wind)

    def getCurrentWind(self):
        return self.currentWind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.currentWind = -10+random.random()*20

""" Models a player """
class Player:
    def __init__(self, game, isReversed, xPos, color):
        if not isinstance(game, Game) or not isinstance(isReversed, bool) or not isinstance(xPos, int) or not isinstance(color, str):
            raise Exception("Player constructor arguments invalid", game, isReversed, xPos, color)
        self.game = game
        self.color = color
        self.isReversed = isReversed

        self.currentScore = 0
        self.xPos = xPos

        self.angle = 0
        self.velocity = 0
    
    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        if not isinstance(angle, float) or not isinstance(velocity, float):
            raise Exception("Invalid type of argument of angle or velocity: ", angle, velocity)
        elif angle <= -90 or angle >= 90:
            raise Exception("Angle out of range: ", angle)
        elif velocity < 0:
            raise Exception("Can't have negative velocity: ", velocity)

        self.velocity = velocity
        self.angle = angle
        if self.isReversed:
            newAngle = 180-angle
        else:
            newAngle = angle

        return Projectile(newAngle, self.velocity, self.game.getCurrentWind(), self.xPos, self.game.getCannonSize()/2, -110, 110)


    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        if not isinstance(proj, Projectile):
            exception = "invalid argument for projectileDistance method: "
            raise Exception(exception, proj, "excpected Projectile")

        projRadius = self.game.getBallSize()
        cannonSide = self.game.getCannonSize()

        xDelta = proj.getX() - self.getX()
        combinedSize = cannonSide/2 + projRadius

        if abs(xDelta) <=  combinedSize:
            return 0
        elif xDelta < 0:
            return xDelta + combinedSize
        elif xDelta > 0:
            return xDelta - combinedSize

    """ The current score of this player """
    def getScore(self):
        return self.currentScore

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.currentScore += 1

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.xPos

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.angle, self.velocity



""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
#Projectile(trueAngle, self.velocity, self.game.getCurrentWind(), self.xPos, self.game.getCannonSize()/2, -110, 110)
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
