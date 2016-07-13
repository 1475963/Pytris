# Board class using bit field array in order to store game data

import consts as Consts
import array
import math
from random import sample
from Piece import Piece


class Board(object):

    def __init__(self):
        self.height = Consts.BOA_HEIGHT
        self.width = Consts.BOA_WIDTH
        self.nextPiece = Piece.nextPiece(Consts.BOA_DEFAULT_SPAWN)
        self.setCurrentPiece()
        self.storage = None
        self.acceleration = False
        self.field = array.array(Consts.BOA_FIELD_TYPECODE)
        self.__ResetBoard()

    def __del__(self):
        pass

    def __ResetBoard(self):
        for y in range(self.height):
            for x in range(self.width + 1):
                self.field.append(Consts.BOA_EMPTY_REPR)

    def setCurrentPiece(self):
        self.currentPiece = self.nextPiece
        self.nextPiece = Piece.nextPiece(Consts.BOA_DEFAULT_SPAWN)

    def dropCurrentPiece(self):
        for point in self.currentPiece.repr:
            """
            if Consts.DEBUG and Consts.DEBUG_BACK: print("point : ", point)
            if Consts.DEBUG and Consts.DEBUG_BACK: print("type of pieceType: ", type(self.currentPiece.type))
            """
            self.field[self.__TransformCoords(point[0], point[1])] = self.currentPiece.type
            self.setAmountOfBlocks(point[1], self.getAmountOfBlocks(point[1]) + 1)
        self.currentPiece = None

    def swapStorage(self):
        if self.storage:
            self.currentPiece = self.storage, self.storage = self.currentPiece #swap variables python's lazy way

    def gravity(self):
#        if Consts.DEBUG and Consts.DEBUG_BACK: print("applying gravity ...")
        predictedRepr = [row[:] for row in self.currentPiece.repr]
        if predictedRepr:
#            if Consts.DEBUG and Consts.DEBUG_BACK: print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i][1] += 1
#            if Consts.DEBUG and Consts.DEBUG_BACK: print("predictedRepr: ", predictedRepr)
            if not self.collision(predictedRepr):
                self.currentPiece.repr = predictedRepr
                self.currentPiece.position[1] += 1
            else:
                self.__TriggerImpact()

    def collision(self, pieceRepr):
#        if Consts.DEBUG and Consts.DEBUG_BACK: print("checking collisions ...")
        if pieceRepr:
            for point in pieceRepr:
                if (((point[0] < 0 or point[0] >= Consts.BOA_WIDTH)
                    or (point[1] < 0 or point[1] >= Consts.BOA_HEIGHT))
                or self.field[self.__TransformCoords(point[0], point[1])] != Consts.BOA_EMPTY_REPR):
                    return True
        return False

    def __TriggerImpact(self):
        # function to apply side effects of impact (i.e., delete a row if the row it is filled after the impact)
        print("impact")
        self.checkLoosance()
        self.dropCurrentPiece()
        self.setCurrentPiece()
        self.__RemoveFilledLines()

    def __RemoveFilledLines(self):
        def dropoutLine(localY):
            while localY > 0:
                for x in range(self.width):
                    self.setFrame(x, localY, self.getFrame(x, localY - 1))
                self.setAmountOfBlocks(localY, self.getAmountOfBlocks(localY - 1))
                localY -= 1

        for y in range(self.height):
            if self.isLineFill(y):
                print("fill !")
                dropoutLine(y)

    def moveCurrent(self, pDirection):
        # translate current piece
        predictedRepr = [row[:] for row in self.currentPiece.repr]
#        if Consts.DEBUG and Consts.DEBUG_BACK: print("predictedRepr: ", predictedRepr)
        for i, point in enumerate(predictedRepr):
            predictedRepr[i][0] += pDirection
#        if Consts.DEBUG and Consts.DEBUG_BACK: print("predictedRepr: ", predictedRepr)
        if not self.collision(predictedRepr):
            self.currentPiece.repr = predictedRepr
            self.currentPiece.position[0] += pDirection

    def rotateCurrent(self):
        predictedRepr = [row[:] for row in self.currentPiece.repr]
        """
        if Consts.DEBUG and Consts.DEBUG_BACK:
            print("applying rotation +90")
            print("predictedRepr: ", predictedRepr)
            print("currentPos: ", self.currentPiece.position)
        """
        for i, point in enumerate(predictedRepr):
            xOrigin = self.currentPiece.position[0] + Consts.PIECE_PIVOT[self.currentPiece.type][0]
            yOrigin = self.currentPiece.position[1] + Consts.PIECE_PIVOT[self.currentPiece.type][1]
            xTranslatedOrigin = self.currentPiece.repr[i][0] - xOrigin
            yTranslatedOrigin = self.currentPiece.repr[i][1] - yOrigin
            xRotated = -yTranslatedOrigin
            yRotated = xTranslatedOrigin
            predictedRepr[i][0] = xOrigin + xRotated
            predictedRepr[i][1] = yOrigin + yRotated
#            print(round(predictedRepr[i][0]), round(predictedRepr[i][1]))
            predictedRepr[i][0] = int(round(predictedRepr[i][0]))
            predictedRepr[i][1] = int(round(predictedRepr[i][1]))
#        if Consts.DEBUG and Consts.DEBUG_BACK: print("predictedRepr: ", predictedRepr)
        if not self.collision(predictedRepr):
            print("no collision found")
            self.currentPiece.repr = predictedRepr

    def accelerate(self):
        self.acceleration = True
        Consts.TK_UPDATE_TIMER = Consts.TK_FAST_REFRESH

    def decelerate(self):
        self.acceleration = False
        Consts.TK_UPDATE_TIMER = Consts.TK_NORMAL_REFRESH

    def checkLoosance(self):
        # check loose condition, if lost return true
        # TODO
        """
        print('You lost, noob')
        sys.exit()
        """
        return False

    def getFrame(self, x, y):
        return self.field[self.__TransformCoords(x, y)]

    def setFrame(self, x, y, value):
        self.field[self.__TransformCoords(x, y)] = value

    def isLineFill(self, y):
        if Consts.DEBUG and Consts.DEBUG_BACK: print("number of blocks filled: ", self.field[y * (self.width + 1)])
        if self.field[y * (self.width + 1)] == self.width:
            return True
        return False

    def getAmountOfBlocks(self, y):
        return self.field[y * (self.width + 1)]

    def setAmountOfBlocks(self, y, value):
        self.field[y * (self.width + 1)] = value

    def __TransformCoords(self, x, y):
        return (y * (self.width + 1)) + x + 1
