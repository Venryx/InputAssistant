var {exec, execSync} = require("child_process");

module.exports.TapScreen = function TapScreen(xPercent, yPercent) {
    //Log(screenWidth+ ";" + screenHeight + ";" + parseInt((yPercent * .01) * screenHeight));
    let xPos = parseInt((xPercent * .01) * screenWidth);
    let yPos = parseInt((yPercent * .01) * screenHeight);
    //exec(`adb shell input tap ${xPos} ${yPos}`);
    //exec(`adb shell input swipe ${xPos} ${yPos} ${xPos} ${yPos}`);
    exec(`xdotool mousemove ${xPos} ${yPos} click 1`); //`
}
module.exports.TypeText = function TypeText(text) {
    exec(`adb shell input text "${text}"`);
}
module.exports.PressKey = function PressKey(keyNameOrNumber) {
    exec(`adb shell input keyevent ${keyNameOrNumber}`); //`
}

module.exports.TapScreen_2 = function TapScreen_2(xPercent, yPercent, length = 0, index = 9) {
    x = parseInt(touchscreenWidth * (xPercent / 100));
    y = parseInt(touchscreenHeight * (yPercent / 100));
exec(`sudo /usr/bin/python "${__dirname}/TapScreen.py" ${x} ${y} ${length} ${index} ${touchscreenInputPath}`, (error, stdout, stderr)=> {
        console.log(`Python output: ${stdout}`);
    });
}