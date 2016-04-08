# Board class using bit field array in order to store game data

import consts as Consts
import array
from random import sample
from Piece import Piece


class Board(object):

    def __init__(self):
        self.height = Consts.BOA_HEIGHT
        self.width = Consts.BOA_HEIGHT
        self.nextPiece = Piece.nextPiece(Consts.BOA_DEFAULT_SPAWN)
        self.setCurrentPiece()
        self.storage = None
        self.accelerate = False
        self.field = array.array(Consts.BOA_FIELD_TYPECODE)
#        self.field[]
        self.__ResetBoard()

    def __del__(self):
        pass

    def __ResetBoard(self):
        for y in range(self.height):
            for x in range(self.width):
                self.field.append(Consts.BOA_EMPTY_REPR)

    def setCurrentPiece(self):
        self.currentPiece = self.nextPiece
        self.nextPiece = Piece.nextPiece(Consts.BOA_DEFAULT_SPAWN)

    def dropCurrentPiece(self):
        for point in self.currentPiece.repr:
            print("type of pieceType: ", type(self.currentPiece.type))
            self.field[self.__TransformCoords(point[0], point[1])] = self.currentPiece.type
        self.currentPiece = None

    def swapStorage(self):
        if self.storage:
            self.currentPiece = self.storage, self.storage = self.currentPiece #swap variables python's lazy way

    def gravity(self):
        if Consts.DEBUG and Consts.DEBUG_BACK:
            print("applying gravity ...")
        predictedRepr = self.currentPiece.repr[:]
        if predictedRepr:
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i] = (point[0], point[1] + 1)
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            if not self.collision(predictedRepr):
                self.currentPiece.repr = predictedRepr
            else:
                self.__TriggerImpact()

    def collision(self, pieceRepr):
        if Consts.DEBUG and Consts.DEBUG_BACK:
            print("checking collisions ...")
        # Check loose condition
        # TO DO
        # Check collisions
        if pieceRepr:
            for point in pieceRepr:
                if ((point[0] < 0 or point[0] >= Consts.BOA_WIDTH)
                    or (point[1] < 0 or point[1] >= Consts.BOA_HEIGHT)):
                    return True
                if self.field[self.__TransformCoords(point[0], point[1])] != Consts.BOA_EMPTY_REPR:
                    return True
        return False

    def __TriggerImpact(self):
        # function to apply side effects of impact (i.e., delete a row if the row it is filled after the impact)
        # check lines to delete
        self.dropCurrentPiece()
        self.setCurrentPiece()

    def moveCurrent(self, pDirection):
        # translate current piece
        if pDirection:
            # true, move to the right
            pass
        else:
            # false, move to the left
            pass

    def rotateCurrent(self, pDirection):
        # rotate current piece
        if pDirection:
            # true, rotate 90° clockwise
            pass
        else:
            # false, rotate -90° clockwise
            pass

    def accelerate(self, pToggle):
        # toggle acceleration
        pass

    def checkLoosance(self):
        # check loose condition, if lost return true
        return False

    def getFrame(self, x, y):
        return self.field[self.__TransformCoords(x, y)]

    def setFrame(self, x, y, value):
        self.field[self.__TransformCoods(x, y)] = value

    def __TransformCoords(self, x, y):
        return (y * self.width) + x
