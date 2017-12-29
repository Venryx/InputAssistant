import time
import sys
import os
from random import *

#import uinput
import imp
dir_path = os.path.dirname(os.path.realpath(__file__))
uinput = imp.load_source('module.name', dir_path + '/python-uinput-custom.py')

def main():
    events = (
        uinput.ABS_MT_SLOT + (0, 9, 0, 0),
        uinput.ABS_MT_TRACKING_ID + (0, 65535, 0, 0),
        uinput.ABS_MT_POSITION_X + (0, 1920, 0, 0),
        uinput.ABS_MT_POSITION_Y + (0, 1080, 0, 0),
        uinput.ABS_MT_PRESSURE + (0, 255, 0, 0),
        uinput.ABS_MT_TOUCH_MAJOR + (0, 15, 0, 0),
        uinput.BTN_TOUCH,
        uinput.ABS_X,
        uinput.ABS_Y,
        uinput.ABS_PRESSURE,
        #uinput.SYN_REPORT, #(0x0, 0),
        #uinput.SYN_MT_REPORT, #(0x0, 2),
    )

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    touchscreenInputPath = sys.argv[3]

    print "Tapping at: " + str(x) + "x" + str(y)
    
    fd = os.open(touchscreenInputPath, os.O_WRONLY | os.O_NONBLOCK)
    with uinput.Device(events, "FakeTouchScreen", 0x06, fd=fd) as device:
        global_tracking_id = 1

        # for testing
        '''for i in range(20 / 20):
            time.sleep(1)
            x2 = x + randint(1, 30);
            y2 = y + randint(1, 30);'''
        
        '''device.emit(uinput.ABS_MT_SLOT, 0, syn=False)
        device.emit(uinput.ABS_MT_TRACKING_ID, 20, syn=False)
        device.emit(uinput.BTN_TOUCH, 1, syn=False)
        device.emit(uinput.ABS_MT_POSITION_X, 425, syn=False)
        device.emit(uinput.ABS_MT_POSITION_Y, 400, syn=False)
        device.emit(uinput.ABS_MT_SLOT, 1, syn=False)
        device.emit(uinput.ABS_MT_TRACKING_ID, 21, syn=False)
        device.emit(uinput.ABS_MT_POSITION_X, 650, syn=False)
        device.emit(uinput.ABS_MT_POSITION_Y, 400, syn=False)
        #device.emit(uinput.SYN_REPORT, 0, syn=False)
        device.syn()
        device.emit(uinput.ABS_MT_SLOT, 0, syn=False)
        device.emit(uinput.ABS_MT_POSITION_X, 450, syn=False)
        device.emit(uinput.ABS_MT_POSITION_Y, 400, syn=False)
        device.emit(uinput.ABS_MT_SLOT, 1, syn=False)
        device.emit(uinput.ABS_MT_POSITION_X, 550, syn=False)
        device.emit(uinput.ABS_MT_POSITION_Y, 400, syn=False)
        device.emit(uinput.ABS_MT_SLOT, 0, syn=False)
        device.emit(uinput.ABS_MT_TRACKING_ID, -1, syn=False)
        device.emit(uinput.ABS_MT_SLOT, 1, syn=False)
        device.emit(uinput.ABS_MT_TRACKING_ID, -1, syn=False)
        device.emit(uinput.BTN_TOUCH, 0, syn=False)
        #device.emit(uinput.SYN_REPORT, 0, syn=False)
        device.syn() '''

        '''device.emit(uinput.ABS_MT_POSITION_X, x, syn=False)
        device.emit(uinput.ABS_MT_POSITION_Y, y, syn=False)
        device.emit(uinput.ABS_MT_PRESSURE, 71, syn=False)
        device.emit(uinput.ABS_X, x, syn=False)
        device.emit(uinput.ABS_Y, y, syn=False)
        device.emit(uinput.ABS_PRESSURE, 71, syn=False)
        device.syn()'''
        
        device.emit(uinput.ABS_MT_SLOT, 9, syn=False);
        device.emit(uinput.ABS_MT_TRACKING_ID, global_tracking_id, syn=False); global_tracking_id += 1;
        #device.emit(uinput.BTN_TOUCH, 1, syn=False);
        device.emit(uinput.ABS_MT_POSITION_X, x, syn=False);
        device.emit(uinput.ABS_MT_POSITION_Y, y, syn=False);
        device.emit(uinput.ABS_MT_PRESSURE, 127, syn=False);
        device.emit(uinput.ABS_MT_TOUCH_MAJOR, 127, syn=False);
        device.emit(uinput.ABS_MT_WIDTH_MAJOR, 4, syn=False);
        #device.emit(uinput.SYN_MT_REPORT, 0, syn=False);
        device.syn()
        
        device.emit(uinput.ABS_MT_TRACKING_ID, -1, syn=False);
        #device.emit(uinput.BTN_TOUCH, 0, syn=False);
        #device.emit(uinput.SYN_MT_REPORT, 0, syn=False);
        device.syn()

if __name__ == "__main__":
    main()