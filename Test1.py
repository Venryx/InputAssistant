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
        #uinput.ABS_MT_SLOT,
        #uinput.ABS_MT_TRACKING_ID,
        #uinput.BTN_TOUCH,
        #uinput.ABS_MT_POSITION_X,
        #uinput.ABS_MT_POSITION_Y,
        #uinput.SYN_REPORT,

        uinput.ABS_X,
        uinput.ABS_Y,
        uinput.BTN_LEFT,  
    )

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print "X:" + str(x) + "; Y:" + str(y)

    with uinput.Device(events) as device:
        print "Device: " + str(device)
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
            device.emit_click(uniput.BTN_TOUCH, 1, syn=False)
            device.emit(uinput.ABS_X, 2159, syn=False)
            device.emit(uinput.ABS_Y, 892, syn=False)
            device.emit(uinput.ABS_PRESSURE, 87, syn=False)
            Event: time 1514433201.926149, -------------- SYN_REPORT ------------
            time.sleep(.926169 - .926149)
            Event: time 1514433201.926169, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 89
            Event: time 1514433201.926169, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 89
            Event: time 1514433201.926169, -------------- SYN_REPORT ------------
            time.sleep(.930645 - .926169)
            Event: time 1514433201.930645, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 91
            Event: time 1514433201.930645, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 91
            Event: time 1514433201.930645, -------------- SYN_REPORT ------------
            time.sleep(.937608 - .930645)
            Event: time 1514433201.937608, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 93
            Event: time 1514433201.937608, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 93
            Event: time 1514433201.937608, -------------- SYN_REPORT ------------
            time.sleep(.944590 - .937608)
            Event: time 1514433201.944590, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 94
            Event: time 1514433201.944590, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 94
            Event: time 1514433201.944590, -------------- SYN_REPORT ------------
            time.sleep(.951592 - .944590)
            Event: time 1514433201.951592, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 93
            Event: time 1514433201.951592, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 93
            Event: time 1514433201.951592, -------------- SYN_REPORT ------------
            time.sleep(.958621 - .951592)
            Event: time 1514433201.958621, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 88
            Event: time 1514433201.958621, type 3 (EV_ABS), code 48 (ABS_MT_TOUCH_MAJOR), value 30
            Event: time 1514433201.958621, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 88
            Event: time 1514433201.958621, -------------- SYN_REPORT ------------
            time.sleep(.971123 - .958621)
            Event: time 1514433201.971123, type 3 (EV_ABS), code 57 (ABS_MT_TRACKING_ID), value -1
            Event: time 1514433201.971123, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
            Event: time 1514433201.971123, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 0


            # Just for demonstration purposes: shows the motion. In real
            # application, this is of course unnecessary.
            time.sleep(0.01)
            #time.sleep(.008)
            #time.sleep(0.2)

if __name__ == "__main__":
    main()