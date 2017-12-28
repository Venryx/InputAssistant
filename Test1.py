import time
import sys

import uinput

def main():
    '''
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
    '''
    events = (
        uinput.ABS_MT_TRACKING_ID,
        uinput.ABS_MT_POSITION_X,
        uinput.ABS_MT_POSITION_Y,
        uinput.ABS_MT_PRESSURE,
        uinput.ABS_MT_TOUCH_MAJOR,
        uinput.BTN_TOUCH,
        uinput.ABS_X,
        uinput.ABS_Y,
        uinput.ABS_PRESSURE,
        uinput.ABS_MT_PRESSURE,

        #uinput.ABS_MT_SLOT,
        #uinput.SYN_REPORT,
        #uinput.BTN_LEFT,  
    )

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print "X:" + str(x) + "; Y:" + str(y)

    with uinput.Device(events) as device:
        print "Device: " + str(device)
        for i in range(20 * 1000):
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

            print "clicking"

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

            device.emit(uinput.ABS_MT_TRACKING_ID, 112, syn=False)
            device.emit(uinput.ABS_MT_POSITION_X, 2159, syn=False)
            device.emit(uinput.ABS_MT_POSITION_Y, 892, syn=False)
            device.emit(uinput.ABS_MT_PRESSURE, 87, syn=False)
            device.emit(uinput.ABS_MT_TOUCH_MAJOR, 31, syn=False)
            device.emit_click(uinput.BTN_TOUCH, syn=False)
            #device.emit(uinput.BTN_TOUCH, 1, syn=False)
            device.emit(uinput.ABS_X, 2159, syn=False)
            device.emit(uinput.ABS_Y, 892, syn=False)
            device.emit(uinput.ABS_PRESSURE, 87, syn=False)
            device.syn()
            time.sleep(.926169 - .926149)
            device.emit(uinput.ABS_MT_PRESSURE, 89, syn=False)
            device.emit(uinput.ABS_PRESSURE, 89, syn=False)
            device.syn()
            time.sleep(.930645 - .926169)
            device.emit(uinput.ABS_MT_PRESSURE, 91, syn=False)
            device.emit(uinput.ABS_PRESSURE, 91, syn=False)
            device.syn()
            time.sleep(.937608 - .930645)
            device.emit(uinput.ABS_MT_PRESSURE, 93, syn=False)
            device.emit(uinput.ABS_PRESSURE, 93, syn=False)
            device.syn()
            time.sleep(.944590 - .937608)
            device.emit(uinput.ABS_MT_PRESSURE, 94, syn=False)
            device.emit(uinput.ABS_PRESSURE, 94, syn=False)
            device.syn()
            time.sleep(.951592 - .944590)
            device.emit(uinput.ABS_MT_PRESSURE, 93, syn=False)
            device.emit(uinput.ABS_PRESSURE, 93, syn=False)
            device.syn()
            time.sleep(.958621 - .951592)
            device.emit(uinput.ABS_MT_PRESSURE, 88, syn=False)
            device.emit(uinput.ABS_MT_TOUCH_MAJOR, 30, syn=False)
            device.emit(uinput.ABS_PRESSURE, 88, syn=False)
            device.syn()
            time.sleep(.971123 - .958621)
            device.emit(uinput.ABS_MT_TRACKING_ID, -1, syn=False)
            device.emit(uinput.BTN_TOUCH, 0, syn=False)
            device.emit(uinput.ABS_PRESSURE, 0, syn=False)
            device.syn()


            # Just for demonstration purposes: shows the motion. In real
            # application, this is of course unnecessary.
           # time.sleep(0.01)
            #time.sleep(.008)
            #time.sleep(0.2)

            time.sleep(1)

if __name__ == "__main__":
    main()