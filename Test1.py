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
        uinput.BTN_TOUCH,
        uinput.ABS_X,
        uinput.ABS_Y,
        #uinput.SYN_REPORT
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
            device.emit_click(uinput.BTN_TOUCH, 1);
            device.emit(uinput.ABS_X, x, syn=False);
            device.emit(uinput.ABS_Y, y);
            #device.emit(uinput.SYN_REPORT, 0);

            # Just for demonstration purposes: shows the motion. In real
            # application, this is of course unnecessary.
            #time.sleep(0.01)
            time.sleep(.008)
            #time.sleep(0.2)

if __name__ == "__main__":
    main()