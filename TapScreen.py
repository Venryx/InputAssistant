import time
import sys
import os
from random import *

#import uinput
#from python-uinput-custom import *
import imp
dir_path = os.path.dirname(os.path.realpath(__file__))
uinput = imp.load_source('module.name', dir_path + '/python-uinput-custom.py')

def main():
    '''
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
    '''
    events = (
        uinput.ABS_MT_TRACKING_ID + (0, 65535, 0, 0),
        #(0x03, 0x39, 0, 65535, 0, 0),
        uinput.ABS_MT_POSITION_X + (0, 1920, 0, 0),
        #(0x03, 0x35, 0, 1920, 0, 0),
        uinput.ABS_MT_POSITION_Y + (0, 1080, 0, 0),
        #(0x03, 0x36, 0, 1080, 0, 0),
        uinput.ABS_MT_PRESSURE,
        uinput.ABS_MT_TOUCH_MAJOR + (0, 15, 0, 0),
        #(0x03, 0x30, 0, 15, 0, 0),
        uinput.BTN_TOUCH,
        uinput.ABS_X,
        uinput.ABS_Y,
        uinput.ABS_PRESSURE,
        uinput.ABS_MT_PRESSURE + (0, 255, 0, 0),
        #(0x03, 0x3a, 0, 255, 0, 0),
        uinput.ABS_MT_SLOT + (0, 9, 0, 0),
        #(0x03, 0x2f, 0, 9, 0, 0),

        #(0x0, 0),
        #(0x0, 2),

        #uinput.SYN_REPORT,
        uinput.BTN_LEFT,  
    )

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    length = int(sys.argv[3])
    index = int(sys.argv[4])
    touchscreenInputPath = sys.argv[5]
    print "Tapping at: " + str(x) + "x" + str(y)
    
    fd = os.open(touchscreenInputPath, os.O_WRONLY | os.O_NONBLOCK)
    with uinput.Device(events, "FakeTouchScreen", 0x06, fd=fd) as device:
    
    #with uinput.Device(events, "FakeTouchScreen", 0x06) as device:
        device.__uinput_fd = fd
        
        global_tracking_id = 1
        for i in range(20 / 20):
            # syn=False to emit an "atomic" (5, 5) event.
            '''device.emit(uinput.REL_X, 5, syn=False)
            device.emit(uinput.REL_Y, 5)'''

            '''device.emit(uinput.ABS_MT_POSITION_X, 5, syn=False)
            device.emit(uinput.ABS_MT_POSITION_Y, 5)'''

            #device.emit_click(uinput.BTN_LEFT, 1)Y
            '''device.emit(uinput.ABS_MT_TRACKING_ID, 20, syn=False);
            #device.emit_click(uinput.BTN_TOUCH, 1);
            device.emit(uinput.BTN_TOUCH, 1, syn=False);
            device.emit(uinput.ABS_MT_POSITION_X, x, syn=False);
            device.emit(uinput.ABS_MT_POSITION_Y, y, syn=False);
            #device.emit(uinput.SYN_REPORT, 0);
            device.syn()
            '''
            
            #device.emit(uinput.ABS_MT_TRACKING_ID, 20, syn=False);
            '''device.emit_click(uinput.BTN_TOUCH, 1);
            device.emit(uinput.ABS_X, x, syn=False);
            device.emit(uinput.ABS_Y, y);
            '''
            #device.emit(uinput.SYN_REPORT, 0);
            
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
            

            '''device.emit(uinput.ABS_MT_SLOT, 0, syn=False)
            device.emit(uinput.ABS_MT_TRACKING_ID, 0, syn=False)
            device.emit(uinput.BTN_TOUCH, 1, syn=False)
            device.emit(uinput.ABS_MT_POSITION_X, x, syn=False)
            device.emit(uinput.ABS_MT_POSITION_Y, y, syn=False)
            device.emit(uinput.BTN_TOUCH, 0, syn=False)
            device.syn()
            
            device.emit(uinput.ABS_MT_TRACKING_ID, -1, syn=False)
            device.syn()
            
            device.emit_click(uinput.BTN_LEFT, syn=False)
            device.syn()'''
            
            x2 = x + randint(1, 30);
            y2 = y + randint(1, 30);
            
            
            device.emit(uinput.ABS_MT_SLOT, index, syn=False);
            device.emit(uinput.ABS_MT_TRACKING_ID, global_tracking_id, syn=False); global_tracking_id += 1;
            device.emit(uinput.ABS_MT_POSITION_X, x, syn=False);
            device.emit(uinput.ABS_MT_POSITION_Y, y, syn=False);
            device.emit(uinput.ABS_MT_PRESSURE, 127, syn=False);
            device.emit(uinput.ABS_MT_TOUCH_MAJOR, 127, syn=False);
            device.emit(uinput.ABS_MT_WIDTH_MAJOR, 4, syn=False);
            #device.emit(uinput.BTN_TOUCH, 1, syn=False);
            #device.emit(uinput.SYN_MT_REPORT, 0, syn=False);
            #device.emit((0x0, 0), 0, syn=False);
            device.syn()
            
            if length != 0:
                sleep(length / 1000)
            
            device.emit(uinput.ABS_MT_SLOT, index, syn=False);
            device.emit(uinput.ABS_MT_TRACKING_ID, -1, syn=False);
            #device.emit((0x0, 2), 0, syn=False);
            #device.emit(uinput.BTN_TOUCH, 0, syn=False);
            #device.emit((0x0, 0), 0, syn=False);
            device.syn()
            

            # Just for demonstration purposes: shows the motion. In real
            # application, this is of course unnecessary.
            #time.sleep(0.01)
            #time.sleep(.1)
            #time.sleep(0.2)

            time.sleep(1)

if __name__ == "__main__":
    main()