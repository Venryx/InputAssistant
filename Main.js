//var chroot = require("chroot")
var fs = require("fs");
var posix = require("posix")
var {exec, execSync} = require("child_process");
var prompt = require("prompt");

// Set a deadzone of +/-3500 (out of +/-32k) and a sensitivty of 350 to reduce signal noise in joystick axis 
var joystick = new (require("joystick"))(0, 3500, 350)
//joystick.on('button', console.log)
//joystick.on('axis', console.log)

EscapeCHRoot();
let {screenWidth, screenHeight} = GetAndroidInfo();

let games = {
    0: "SmashCopsHeat",
    1: "Getaway",
};
Log("Games:");
for (var i in games) {
    Log(`\t${i}) ${games[i]}`);
}
Log("");
Log("Please enter index of game:");

prompt.start();

prompt.get(['gameIndex'], function (err, result) {
    if (err) { 
        Log(error);
        return 1;
    }
    StartForGame(result.gameIndex);
});


function StartForGame(gameID) {
    if (gameID == 0) {
        joystick.on("button", data=> {
            let {number, value, time, init, type, id} = data;
            //console.log(`Button:${number};${value}`);
            if (number == 0) {
                if (value) {
                    DoRam();
                }
            }
        });
    } else if (gameID == 1) {
        joystick.on("button", data=> {
            let {number, value, time, init, type, id} = data;
            if (number == 0) {
                if (value) {
                    UsePower();
                }
            }
        });
    }
    
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
    exec(`adb shell input tap ${parseInt((xPercent * .01) * screenWidth)} ${parseInt((yPercent * .01) * screenHeight)}`);
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