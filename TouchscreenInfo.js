var {exec, execSync} = require("child_process");
const util = require('util');
//const exec = util.promisify(require('child_process').exec);

module.exports.GetTouchscreenSize = function(callback) {
    //exec(`sudo evtest 2>&1 | grep -i "touchscreen"`, {timeout: 1000}, (error, stdout, stderr)=> {
    exec(`evtest`, {timeout: 1000}, (error, stdout, stderr)=> {
        //inputList.kill();
        //console.log(`Output: ${stdout} STDError: ${stderr} Error: ${error}`);
        //let lines = stdout.split("\n");
        let touchscreenInputPathMatch = stderr.match(/^(.*\/input\/event[0-9]+):.+touchscreen/mi);
        if (touchscreenInputPathMatch == null) {
            throw new Error(`Could not find touchscreen device! Only found these:\n==========\n${stderr}`);
        }
        let touchscreenInputPath = touchscreenInputPathMatch[1];
        
        exec(`evtest ${touchscreenInputPath}`, {timeout: 1000}, (error, stdout, stderr)=> {
            let lines = stdout.split("\n");

            let widthNameLineNumber = lines.findIndex(a=>a.includes("ABS_MT_POSITION_X"));
            if (widthNameLineNumber == -1) {
                throw new Error("Could not find ABS_MT_POSITION_X max-value. Output:\n==========\n" + stdout);
            }
            let width = parseInt(lines[widthNameLineNumber + 3].match(/Max +([0-9]+)/)[1]);

            let heightNameLineNumber = lines.findIndex(a=>a.includes("ABS_MT_POSITION_Y"));
            let height = parseInt(lines[heightNameLineNumber + 3].match(/Max +([0-9]+)/)[1]);

            console.log(`Found touchscreen size: ${width}x${height}`);

            callback({width, height});
        });
    });

    //let process = exec(`sudo evtest 2>&1 | grep -i "touchscreen"`, {async: true});
    /*let process = exec(`sudo evtest 2>&1`, {async: true});
    process.stdout.on('data', function(data) {
        console.log("Hi" + data);
    });
    process.stderr.on('data', function(data) {
        console.log("Hi2" + data); 
    });
    process.on('close', (code) => {
      console.log(`Ze child process exited with code ${code}`);
    });
    setTimeout(()=> {
        process.kill();
        console.log("Killed");
        let width = 10;
        let height = 20;
        callback({width, height});
    }, 1000);*/
}

module.exports.GetTouchscreenSize_Sync = function() {
    let output = execSync(`evtest 2>&1 | grep -i "touchscreen"`, {timeout: 1000}).toString();
    //inputList.kill();
    console.log(`Output: ${stdout} STDError: ${stderr} Error: ${error}`);
    let width = 10;
    let height = 20;
    return {width, height};
}