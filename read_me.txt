This program reads files stored in the "macros" folder which follow a certain syntax. Three examples are included to present all features

The syntax for the file is as follows:
    Each line is an instruction
    An instruction is split up into "{key(s)} {press type} {duration}"

    Key(s) be either a singular one, or numerous. If it's numerous, seperate them using a plus sign.
    The key names are identical to pyautogui's (https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)

    The press type simply denotes whether the aforementioned key is pressed down or up
    It can either be "up" "down" or "press"
    "press" will press the key down, wait the duration, then immediately release it without having to specify keyUp.

    The duration is the amount in milliseconds that the program should wait until reading the next instruction.

E.g.
    f1+w down 500
    f1 up 2000
    w up 0
    a press 50
    d press 100

    This would initially hold down F1 and W for 500ms, then let go of F1. Two seconds later, it would let go of W. Immediately afterwards, it presses A for 50ms, lets go, and presses D for 100ms


If the syntax is incorrect, the program *will* crash. This might lead to a key being left held down
PyAutoGUI also has a feature where moving your cursor to the top left corner of your screen will automatically raise an exception. Similarly, it *will* let the program crash.
And you may risk a key being left held down.

You can simply press any key to rectify this.
