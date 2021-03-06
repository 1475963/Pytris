# Piece class to define current piece used and storage pieces

import consts as Consts
import array
from random import sample


class Piece(object):

    def __init__(self, pieceRepr, pieceType, piecePos):
        self.repr = pieceRepr
        self.type = pieceType
        self.position = [int(piecePos[0]), int(piecePos[1])]

    def __del__(self):
        pass

    @staticmethod
    def buildPiece(pos, virtualPiece):
        piece = []
        for point in Consts.BOA_REAL_REPR[virtualPiece]:
            piece.append([int(point[0] + pos[0]), int(point[1] + pos[1])])
        if Consts.DEBUG and Consts.DEBUG_BACK:
            print("piece: ", piece)
        return Piece(piece, virtualPiece, pos)

    @staticmethod
    def nextPiece(pos):
        pieceType = sample(Consts.BOA_VALID_REPR[1:], 1)[0]
        if Consts.DEBUG and Consts.DEBUG_BACK:
            print("pieceType: ", pieceType)
        return Piece.buildPiece(pos, pieceType)
