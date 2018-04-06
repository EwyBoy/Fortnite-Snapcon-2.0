import Tkinter
import ctypes
import time
import keyboard
import mouse

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actual Functions
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


mode = False
label = Tkinter.Label(text='ERROR', font=('Times New Roman', '18'), fg='azure2', bg='deepskyblue2')

print 'Fortnite - Snapcon Version 2.0.0'
print 'Developed by: EwyBoy 03.18.2018\n'
print 'License: The MIT License Copyright (c) <2018> <EwyBoy> Permission is hereby granted, \n' \
      'free of charge, to any person obtaining a copy of this software and associated documentation files (the \n' \
      '"Software"), to deal in the Software without restriction, including without limitation the rights to use, \n' \
      'copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit \n' \
      'persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright \n' \
      'notice and this permission notice shall be included in all copies or substantial portions of the Software. THE \n' \
      'SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO \n' \
      'THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \n' \
      'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF \n' \
      'CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER \n' \
      'DEALINGS IN THE SOFTWARE.\n'


# If the mode is true it takes the input and simulates a keypress on that key the performs a mouse click
def build(keycode):
    if mode:
        PressKey(keycode)
        ReleaseKey(keycode)
        time.sleep(0.05)
        mouse.click()


# Draws the UI-Overlay
def funcOverlay():
    label.master.geometry("+1750+740")
    label.master.overrideredirect(True)
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)

    if mode:
        label.configure(text='Snap Build: ON')
    else:
        label.configure(text='Snap Build: OFF')
    label.update()
    label.pack()


# Flips the MODE boolean and tells the UI-overlay to update it's label
def switchMode():
    global mode
    mode ^= True
    time.sleep(0.1)
    funcOverlay()
    if mode:
        label.configure(text='Snap Build: ON')
        print('Snap Build: ON')
    else:
        label.configure(text='Snap Build: OFF')
        print('Snap Build: OFF')


# Have to Switch mode twice to get the UI to render properly
# Don't ask why, cause if I knew why it would NOT be done like this
print('Firing up overlay UI and testing modes:')
switchMode()
print('Snap Build: ON | Confirmed Working..')
switchMode()
print('Snap Build: OFF | Confirmed Working..')

print('')
print('Script is now ready to use!')
print('')


# Main loop that handles key presses
def funcLoop():
    global mode

    while True:
        try:
            # Toggles between normal and military buildings using the '|' (pipe) key
            if keyboard.is_pressed('|'):
                switchMode()

            # <1> # Build Wall | 0x3B = f1
            elif keyboard.is_pressed('1'):
                build(0x3B)

            # <1> # Build Floor | 0x3C = f2
            elif keyboard.is_pressed('2'):
                build(0x3C)

            # <1> # Build Stairs | 0x3D = f3
            elif keyboard.is_pressed('3'):
                build(0x3D)

            # <1> # Build Trap | 0x3F = f5
            elif keyboard.is_pressed('4'):
                build(0x3F)

            else:
                pass
        except:
            break


# Main method
if __name__ == '__main__':
    funcLoop()
    funcOverlay()