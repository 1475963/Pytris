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
            print("point : ", point)
            if Consts.DEBUG and Consts.DEBUG_BACK: print("type of pieceType: ", type(self.currentPiece.type))
            self.field[self.__TransformCoords(point[0], point[1])] = self.currentPiece.type
        self.currentPiece = None

    def swapStorage(self):
        if self.storage:
            self.currentPiece = self.storage, self.storage = self.currentPiece #swap variables python's lazy way

    def gravity(self):
        if Consts.DEBUG and Consts.DEBUG_BACK:
            print("applying gravity ...")
        predictedRepr = [row[:] for row in self.currentPiece.repr]
        if predictedRepr:
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i][1] += 1
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
        self.dropCurrentPiece()
        self.setCurrentPiece()
        self.__RemoveFilledLines()

    def __RemoveFilledLines(self):
        # should optimize this rly (does not work btw)
        def isLineFill(localY):
            for x in range(self.width):
                frame = self.getFrame(x, localY)
                if frame != None:
                    if frame == Consts.BOA_EMPTY_REPR:
                        return False
            return True

        def dropoutLine(localY):
            for i in range(localY, self.height):
                print("i = ", i)
                if i < self.height - 1:
                    for x in range(self.width):
                        self.setFrame(x, localY, self.getFrame(x, localY + 1))
                else:
                    for x in range(self.width):
                        self.setFrame(x, localY, Consts.BOA_EMPTY_REPR)

        for y in range(self.height):
            if isLineFill(y):
                print("fill !")
                dropoutLine(y)

    def moveCurrent(self, pDirection):
        # translate current piece
        predictedRepr = [row[:] for row in self.currentPiece.repr]
        if pDirection:
            # true, move to the right
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i][0] += 1
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
        else:
            # false, move to the left
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i][0] -= 1
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
        if not self.collision(predictedRepr):
            self.currentPiece.repr = predictedRepr

    def rotateCurrent(self, pDirection):
        # rotate current piece
        predictedRepr = [row[:] for row in self.currentPiece.repr]
        if pDirection:
            # true, rotate 90° clockwise
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i][0] += self.currentPiece.repr[i][1] - Consts.PIECE_PIVOT[self.currentPiece.type][0]
                predictedRepr[i][1] += Consts.PIECE_PIVOT[self.currentPiece.type][1] - self.currentPiece.repr[i][0]
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
        else:
            # false, rotate -90° clockwise
            """
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            for i, point in enumerate(predictedRepr):
                predictedRepr[i][0] = y #self.currentPiece.repr[i][1] - Consts.PIECE_PIVOT[self.currentPiece.type]
                predictedRepr[i][1] = -x #Consts.PIECE_PIVOT[self.currentPiece.type] - self.currentPiece.repr[i][0]
            if Consts.DEBUG and Consts.DEBUG_BACK:
                print("predictedRepr: ", predictedRepr)
            """
            pass
        if not self.collision(predictedRepr):
            print("lolololol")
            self.currentPiece.repr = predictedRepr

    def accelerate(self):
        # toggle acceleration
        self.accelerate = not self.accelerate
        # change timer here

    def checkLoosance(self):
        # check loose condition, if lost return true
        return False

    def getFrame(self, x, y):
        return self.field[self.__TransformCoords(x, y)]

    def setFrame(self, x, y, value):
        self.field[self.__TransformCoords(x, y)] = value

    def __TransformCoords(self, x, y):
        return (y * self.width) + x
