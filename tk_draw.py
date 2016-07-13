# module to draw things with tkinter

from tkinter import *
import sys
import consts as Consts


def getInstance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()


def clickHandler(event, pBoard):
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('click at x : (%d), y : (%d)' % (event.x, event.y))


def keyPressHandler(event, board):
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('keystroke pressed : ', event.keycode)
    if event.keycode in Consts.TK_KEY_EXIT:
        print('You decided to quit, pussy') # Need an upgrade, should have a dict of lambda functions
        sys.exit()
    elif event.keycode in Consts.TK_KEY_LEFT:
        # Left
        board.moveCurrent(-1)
    elif event.keycode in Consts.TK_KEY_RIGHT:
        # Right
        board.moveCurrent(1)
    elif event.keycode in Consts.TK_KEY_ROT_CW90:
        # Rotation clockwise 90
        board.rotateCurrent()
    elif event.keycode in Consts.TK_KEY_ACCELERATE:
        board.accelerate()


def keyReleaseHandler(event, board):
    if event.keycode in Consts.TK_KEY_ACCELERATE:
        board.decelerate()


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
    canvas = Canvas(pInstance, width=Consts.TK_WIN_WIDTH, height=Consts.TK_WIN_HEIGHT)
    canvas.bind('<KeyPress>',
                lambda event, board=pBoard: keyPressHandler(event, board))
    canvas.bind('<KeyRelease>',
                lambda event, board=pBoard: keyReleaseHandler(event, board))
    canvas.bind('<ButtonPress-1>',
                lambda event, board=pBoard: clickHandler(event, board))
    canvas.focus_set()
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
        return ((pPoint[0] * (Consts.TK_WIN_WIDTH / Consts.BOA_WIDTH)),
                (pPoint[1] * (Consts.TK_WIN_HEIGHT / Consts.BOA_HEIGHT)))


def drawSquare(window, x, y, color):
    sPoint = scaleBoardToGraphic((x, y))
    ePoint = scaleBoardToGraphic((x + 1, y + 1))
    """
    if Consts.DEBUG and Consts.DEBUG_FRONT:
        print('SQUARE:: start point : {}, end point : {}'.format(sPoint,
                                                                 ePoint))
    """
    window.create_rectangle(sPoint[0], sPoint[1],
                            ePoint[0], ePoint[1],
                            fill=color)


def drawBoard(window, board):
    '''Draws the board in the canvas on the window'''

    window.create_rectangle(0, 0,
                            Consts.TK_WIN_WIDTH, Consts.TK_WIN_HEIGHT,
                            fill=Consts.TK_BG_COLOR)

    for y in range(board.height):
        for x in range(board.width):
            frame = board.getFrame(x, y)
            if frame in Consts.BOA_GRAPHIC_REPR:
                drawSquare(window, x, y, Consts.BOA_GRAPHIC_REPR[frame])
#    if Consts.DEBUG and Consts.DEBUG_FRONT: print("_____")
    if board.currentPiece and board.currentPiece.repr and board.currentPiece.type:
#        if Consts.DEBUG and Consts.DEBUG_FRONT: print("currentPieceType: ", board.currentPiece.type)
        for point in board.currentPiece.repr:
            if board.currentPiece.type in Consts.BOA_GRAPHIC_REPR:
                drawSquare(window, point[0], point[1], Consts.BOA_GRAPHIC_REPR[board.currentPiece.type])
#    if Consts.DEBUG and Consts.DEBUG_FRONT: print("_____")
