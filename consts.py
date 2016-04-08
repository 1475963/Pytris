#!/usr/bin/python

## consts placeholder

''' main consts '''

USAGE         = "USAGE:\t./pytris [nothanks]"
DEBUG         = True
DEBUG_FRONT   = False
DEBUG_BACK    = True

''' tkinter consts '''

TK_BG_COLOR         = '#ffffff'
TK_BG_STICKS_COLOR  = '#000000'
TK_COLOR_BLACK      = '#000000'
TK_COLOR_SKYBLUE    = '#33ccff'
TK_COLOR_YELLOW     = '#ffff00'
TK_COLOR_VIOLET     = '#ff00ff'
TK_COLOR_ORANGE     = '#ff9933'
TK_COLOR_BLUE       = '#0000ff'
TK_COLOR_RED        = '#ff0000'
TK_COLOR_GREEN      = '#00ff00'
TK_UPDATE_TIMER     = 250

''' board consts '''

BOA_HEIGHT          = 22
BOA_WIDTH           = 12
BOA_DEFAULT_SPAWN   = (BOA_WIDTH / 3, 0)
BOA_FIELD_TYPECODE  = 'B'
BOA_EMPTY_REPR      = 0
BOA_VIRT_PIECE_I    = 1 # 'I' which is 73 in ASCII
BOA_REAL_PIECE_I    = [(0, 0), (1, 0), (2, 0), (3, 0)] #x, y
BOA_VIRT_PIECE_O    = 2 # 'O' which is 79 in ASCII
BOA_REAL_PIECE_O    = [(1, 0), (2, 0), (1, 1), (2, 1)]
BOA_VIRT_PIECE_T    = 3 # 'T' which is 84 in ASCII
BOA_REAL_PIECE_T    = [(1, 0), (0, 1), (1, 1), (2, 1)]
BOA_VIRT_PIECE_L    = 4 # 'L' which is 76 in ASCII
BOA_REAL_PIECE_L    = [(0, 0), (1, 0), (2, 0), (0, 1)]
BOA_VIRT_PIECE_J    = 5 # 'J' which is 74 in ASCII
BOA_REAL_PIECE_J    = [(0, 0), (1, 0), (2, 0), (2, 1)]
BOA_VIRT_PIECE_Z    = 6 # 'Z' which is 90 in ASCII
BOA_REAL_PIECE_Z    = [(0, 0), (1, 0), (1, 1), (2, 1)]
BOA_VIRT_PIECE_S    = 7 # 'S' which is 83 in ASCII
BOA_REAL_PIECE_S    = [(1, 0), (2, 0), (0, 1), (1, 1)]
BOA_VALID_REPR      = [BOA_EMPTY_REPR,
                       BOA_VIRT_PIECE_I,
                       BOA_VIRT_PIECE_O,
                       BOA_VIRT_PIECE_T,
                       BOA_VIRT_PIECE_L,
                       BOA_VIRT_PIECE_J,
                       BOA_VIRT_PIECE_Z,
                       BOA_VIRT_PIECE_S]
BOA_REAL_REPR       = { BOA_VIRT_PIECE_I: BOA_REAL_PIECE_I,
                        BOA_VIRT_PIECE_O: BOA_REAL_PIECE_O,
                        BOA_VIRT_PIECE_T: BOA_REAL_PIECE_T,
                        BOA_VIRT_PIECE_L: BOA_REAL_PIECE_L,
                        BOA_VIRT_PIECE_J: BOA_REAL_PIECE_J,
                        BOA_VIRT_PIECE_Z: BOA_REAL_PIECE_Z,
                        BOA_VIRT_PIECE_S: BOA_REAL_PIECE_S }
BOA_GRAPHIC_REPR    = { BOA_VIRT_PIECE_I: TK_COLOR_SKYBLUE,
                        BOA_VIRT_PIECE_O: TK_COLOR_YELLOW,
                        BOA_VIRT_PIECE_T: TK_COLOR_VIOLET,
                        BOA_VIRT_PIECE_L: TK_COLOR_ORANGE,
                        BOA_VIRT_PIECE_J: TK_COLOR_BLUE,
                        BOA_VIRT_PIECE_Z: TK_COLOR_RED,
                        BOA_VIRT_PIECE_S: TK_COLOR_GREEN }
