var chroot = require('chroot')
var {execSync} = require("child_process");

// Set a deadzone of +/-3500 (out of +/-32k) and a sensitivty of 350 to reduce signal noise in joystick axis 
var joystick = new (require('joystick'))(0, 3500, 350)
//joystick.on('button', console.log)
//joystick.on('axis', console.log)

joystick.on("button", data=> {
    let {button, value} = data
    if (button == 0) {
        if (value) {
            PressButton()
        }
    }
});

function Log(str) { console.log(str) }
function PressButton() {
    console.log('Starting0 directory: ' + process.cwd());
    Log(execSync("ls").toString())
    //chroot('/foo', 'venryx')
    //Log(execSync("chroot /foo").toString())
    Log(execSync("python \"/home/venryx/Downloads/Root/Apps/@V/Input Assistant/Main/EscapeCHRoot.py\"").toString())
    
    console.log('Starting directory: ' + process.cwd());
    Log(execSync("ls").toString())
    /*try {
      process.chdir('/');
      console.log('New directory: ' + process.cwd());
    Log(execSync("ls").toString())
}
    catch (err) {
      console.log('chdir: ' + err);
    }*/

}

Log("Test1")
PressButton()
Log("Test2")