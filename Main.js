//var chroot = require("chroot")
var fs = require("fs");
var posix = require("posix")
var Joystick = require("joystick");
var {exec, execSync} = require("child_process");
var prompt = require("prompt");

/*EscapeCHRoot();
let {screenWidth, screenHeight} = GetAndroidInfo();
Log(`Connected to Android. Screen size: ${screenWidth}x${screenHeight}`);*/
// not needed atm; we use touchscreen width/height instead, for send-input pathway
//let screenWidth = 1920;
//let screenHeight = 1080;

let {GetTouchscreenSize, GetTouchscreenSize_Sync} = require("./TouchscreenInfo");

let games = {
    0: "SmashCopsHeat",
    1: "Getaway",
    2: "World of Tanks Blitz",
};
Log("Games:");
for (var i in games) {
    Log(`\t${i}) ${games[i]}`);
}
Log("");
Log("Please enter index of game:");

prompt.start();

var touchscreenWidth, touchscreenHeight;


prompt.get(
    {
        properties: {
            gameIndex: {
                //type: "integer",
                pattern: /^#?([0-9]+)$/,
                message: 'GameIndex must be a number',
                required: true
            },
        },
    },
    function (error, result) {
        if (error) {
            Log(error);
            return 1;
        }
        

        GetTouchscreenSize(({width, height})=> {
            //let {width, height} = GetTouchscreenSize_Sync();
            touchscreenWidth = width;
            touchscreenHeight = height;
            StartForGame(0, result.gameIndex.match(/[0-9]+/)[0]);
            //StartForGame(result.gameIndex);    
        });
    }
);

// for testing
var mainTrigger_func;
function StartTesting() {
    setInterval(mainTrigger_func, 1000);
}
// toggle this to 1 to test (have main trigger occur every 1s)
var testing = 0

function StartForGame(joystick, gameID) {
    if (joystick) {
        // Set a deadzone of +/-3500 (out of +/-32k) and a sensitivty of 350 to reduce signal noise in joystick axis 
        var joystick = new Joystick(0, 3500, 350);
        //joystick.on('button', console.log)
        //joystick.on('axis', console.log)
    }
    let lastTriggerTime = 0;
    function AddListener_OnMainTrigger(func) {
        if (testing) {
            mainTrigger_func = func; // for testing
            return;
        }
        
        if (joystick) {
            joystick.on("button", data=> {
                let {number, value, time, init, type, id} = data;
                //console.log(`Button:${number};${value}`);
                if (number == 0 && value) {
                    func();
                }
            });
        } else {
            const { spawn } = require('child_process');
            const ls = spawn('cat', ['/dev/input/event11']);
            ls.stdout.on('data', (data) => {
              //console.log(`stdout: ${data}`);
                // if it's been less than 100ms, this is probably part of previous trigger; ignore
                if (Date.now() - lastTriggerTime < 150) return;
                lastTriggerTime = Date.now();

                func();
            });
            ls.stderr.on('data', (data) => {
              console.log(`stderr: ${data}`);
            });
            ls.on('close', (code) => {
              console.log(`child process exited with code ${code}`);
            });
        }
    }

    if (gameID == 0) {
        AddListener_OnMainTrigger(DoRam);
    } else if (gameID == 1) {
        AddListener_OnMainTrigger(UsePower);
    } else if (gameID == 2) {
        AddListener_OnMainTrigger(FireWeapon);
    }

    if (testing) StartTesting();
    
    Log(`Initialized. Game: ${games[gameID]}`);
}

function chroot(path) {
    return posix.chroot(path);
}

function Log(str) { console.log(str) }
function EscapeCHRoot() {
    var dir = "./tempCHRoot";
    if (!fs.existsSync(dir)){
        fs.mkdirSync(dir);
    }
    chroot(dir);
    for (var i = 0; i < 100; i++) {
        process.chdir("..");
    }
    chroot(".");
}

function GetAndroidInfo() {
    // connect, in case not already connected
    execSync("adb connect 100.115.92.2");

    let resolutionStr = execSync(`adb shell dumpsys window | grep cur= |tr -s " " | cut -d " " -f 4|cut -d "=" -f 2`).toString();
    return {screenWidth: parseInt(resolutionStr.split("x")[0]), screenHeight: parseInt(resolutionStr.split("x")[1])};
}

function TapScreen(xPercent, yPercent) {
    //Log(screenWidth+ ";" + screenHeight + ";" + parseInt((yPercent * .01) * screenHeight));
    let xPos = parseInt((xPercent * .01) * screenWidth);
    let yPos = parseInt((yPercent * .01) * screenHeight);
    //exec(`adb shell input tap ${xPos} ${yPos}`);
    //exec(`adb shell input swipe ${xPos} ${yPos} ${xPos} ${yPos}`);
    exec(`xdotool mousemove ${xPos} ${yPos} click 1`);
}
function TypeText(text) {
    exec(`adb shell input text "${text}"`);
}
function PressKey(keyNameOrNumber) {
    exec(`adb shell input keyevent ${keyNameOrNumber}`);    
}

// for Smash Cops Heat game
function DoRam() {
    //TapScreen(5, 90);
    //TypeText("t");
    //PressKey("KEYCODE_T");
    PressKey(48);
    console.log("Doing ram.");
}

// for Getaway
function UsePower() {
    PressKey(66);
}

// for World of Tanks Blitz
function FireWeapon() {
    console.log("Firing weapon.");
    TapScreen_2(90.3, 75.9);

    // temp
    //TapScreen_2 = ()=>{};
}

let path = "/home/venryx/Downloads/Root/Apps/@V/Input Assistant/Main";
function TapScreen_2(xPercent, yPercent) {
    x = parseInt(touchscreenWidth * (xPercent / 100));
    y = parseInt(touchscreenHeight * (yPercent / 100));
    exec(`sudo /usr/bin/python "${path}/TapScreen.py" ${x} ${y}`, (error, stdout, stderr)=> {
        Log(`Python output: ${stdout}`);
    });
}