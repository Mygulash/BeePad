# DEAD CODE, NOT DONE!

print("Hackpad Testing!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Extra features
from kmk.extensions.RGB import RGB

print(dir(board))

keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP26, board.GP27,board.GP28)
keyboard.row_pins = (board.GP29, board.GP2, board.GP1)

keyboard.keymap = [
    [
        KC.B, KC.E, KC.P,
        KC.A, KC.D, KC.C,
        KC.F, KC.G, KC.DOT,
    ]
]

if __name__ == '__main__':
    keyboard.go()