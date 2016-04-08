# module to draw things with tkinter

from tkinter import *
import board_properties as Config
import consts as Consts


def getInstance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()


def clickHandler(event, pBoard):
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('click at x : (%d), y : (%d)' % (event.x, event.y))


def keyboardHandler(event):
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('keystroke pressed : ', repr(event.char))


def updateHandler(pInstance, pWindow, pBoard):
    """
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('update')
    """
    drawBoard(pWindow, pBoard)
    pBoard.gravity()
    attachUpdater(pInstance, pWindow, pBoard)


def getWindow(pInstance, pBoard):
    ''' Returns a canvas object to draw on '''
    canvas = Canvas(pInstance, width=Config.WIDTH, height=Config.HEIGHT)
    canvas.bind('<Key>', keyboardHandler)
    canvas.bind('<ButtonPress-1>',
                lambda event, board=pBoard: clickHandler(event, board))
    canvas.pack()
    return canvas


def attachUpdater(pInstance, pWindow, pBoard):
    pInstance.after(Consts.TK_UPDATE_TIMER, updateHandler,
                    pInstance, pWindow, pBoard)


def attachMainloop(pInstance):
    ''' Calls Tkinter mainloop() function '''
    pInstance.mainloop()


def scaleBoardToGraphic(pPoint):
    if len(pPoint) == 2:
        for i in range(2):
            if not (isinstance(pPoint[i], int) or isinstance(pPoint[i], float)):
                raise Exception('bad point format')
        return ((pPoint[0] * (Config.WIDTH / Consts.BOA_WIDTH)),
                (pPoint[1] * (Config.HEIGHT / Consts.BOA_HEIGHT)))

def drawSquare(window, x, y, color):
    sPoint = scaleBoardToGraphic((x, y))
    ePoint = scaleBoardToGraphic((x + 1, y + 1))
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('SQUARE:: start point : {}, end point : {}'.format(sPoint,
                                                                 ePoint))
    window.create_rectangle(sPoint[0], sPoint[1],
                            ePoint[0], ePoint[1],
                            fill=color)

def drawBoard(window, board):
    '''Draws the board in the canvas on the window'''

    window.create_rectangle(0, 0,
                            Config.WIDTH, Config.HEIGHT,
                            fill=Consts.TK_BG_COLOR)

    for y in range(board.height):
        for x in range(board.width):
            frame = board.getFrame(x, y)
            if frame in Consts.BOA_GRAPHIC_REPR:
                drawSquare(window, x, y, Consts.BOA_GRAPHIC_REPR[frame])
    if Consts.DEBUG and Consts.DEBUG_FRONT: print("_____")
    if board.currentPiece and board.currentPiece.repr and board.currentPiece.type:
        if Consts.DEBUG and Consts.DEBUG_FRONT: print("currentPieceType: ", board.currentPiece.type)
        for point in board.currentPiece.repr:
            if board.currentPiece.type in Consts.BOA_GRAPHIC_REPR:
                drawSquare(window, point[0], point[1], Consts.BOA_GRAPHIC_REPR[board.currentPiece.type])
    if Consts.DEBUG and Consts.DEBUG_FRONT: print("_____")
