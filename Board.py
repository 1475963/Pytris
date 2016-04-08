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

    def swapStorage(self):
        if self.storage:
            self.currentPiece = self.storage, self.storage = self.currentPiece #swap variables python's lazy way

    def gravity(self):
#        print("applying gravity ...")
        """
        if self.currentPosition[1] > 0 and self.field.getFrame(self.currentPosition[0], self.currentPosition[1] - 1) == BOA_EMPTY_REPR:
            self.currentPosition[1] -= 1
        """
        pass

    def collision(self):
        pass

    def __TriggerImpact(self):
        # function to apply side effects of impact (i.e., delete a row if the row is filled after the impact)
        pass

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

    def getFrame(self, x, y):
        return self.field[self.__TransformCoords(x, y)]

    def setFrame(self, pX, pY):
        # TODO, there is code from the tictactoe bellow
        localFrame = self.field[self.__TransformCoords(pX, pY)]
        if localFrame == Consts.BOA_EMPTY_REPR:
            self.field[self.__TransformCoords(pX, pY)] = self.turn
            if self.checkWinnance(pX, pY):
                winner = 'VOID LOL'
                if self.turn == Consts.BOA_P1_REPR:
                    winner = 'P1 - CROSS'
                elif self.turn == Consts.BOA_P2_REPR:
                    winner = 'P2 - CIRCLE'
                raise Exception('ALLER CHAMPION (%s) A GAGNER' % winner)
            self.fireNextTurn()

    def checkLoosance(self):
        # check loose condition, if lost return true
        return False

    def __TransformCoords(self, x, y):
        return (y * self.width) + x
