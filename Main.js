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

let {games, lockVolume, primaryDevice_searchString, secondaryDevice_searchString} = require("./UserConfig");
let {GetTouchscreenSize, GetTouchscreenSize_Sync} = require("./TouchscreenInfo");

Log("Games:");
for (var [index, gameName] of Object.entries(Object.keys(games))) {
	Log(`\t${index}) ${gameName}`); //`
}
Log("");
Log("Please enter index of game:");

prompt.start();
prompt.get(
	{
		properties: {
			gameIndex: {
				//type: "integer",
				pattern: /^#?([0-9]+)$/,
				message: 'GameIndex must be a number',
				required: true
			},
			/*deviceName: {
				 description: `Input devices:\n==========\n${inputDeviceList_simple}\n==========\nType the name of your input device`,
				 //type: "integer",
				 //pattern: /^#?([0-9]+)$/,
				 message: 'DeviceName must be a string',
				 required: true
			},*/
		},
	},
	function(error, result) {
		if (error) {
			Log(error);
			return 1;
		}

		TryToStartGame(result.gameIndex.match(/[0-9]+/)[0]);
	}
);

//var inputDeviceList, touchscreenInputPath, touchscreenWidth, touchscreenHeight;

function TryToStartGame(gameIndex) {
	//let {width, height} = GetTouchscreenSize_Sync();
	console.log(`Searching for primary device... (${primaryDevice_searchString})`); //`
	GetTouchscreenSize(info => {
		global.inputDeviceList = info.inputDeviceList;
		global.touchscreenInputPath = info.touchscreenInputPath;
		global.touchscreenWidth = info.width;
		global.touchscreenHeight = info.height;

		let inputDeviceList_simple = inputDeviceList.split("\n")
			.filter(a => a.includes("/input/") && !a.includes("trying to scan"))
			.join("\n").replace(/\/dev\/input\//g, "");

		let lineWithPrimaryDevice = inputDeviceList_simple.split("\n").find(a => a.includes(primaryDevice_searchString));
		if (!lineWithPrimaryDevice) return void setTimeout(() => TryToStartGame(gameIndex), 1000);
		let primaryDevice_name = lineWithPrimaryDevice.match(/(.+):/)[1];
		console.log(`Primary device found: ${lineWithPrimaryDevice}`); //`

		console.log(`Found touchscreen size: ${info.width}x${info.height}`); //`

		StartForGame(gameIndex.match(/[0-9]+/)[0], primaryDevice_name);
	});
}

// for testing
var mainTrigger_func;
function StartTesting() {
	setInterval(mainTrigger_func, 1000);
}
// toggle this to 1 to test (have main trigger occur every 1s)
var testing = 0

function StartForGame(gameID, inputDeviceName) {
	if (inputDeviceName.startsWith("js")) {
		// Set a deadzone of +/-3500 (out of +/-32k) and a sensitivty of 350 to reduce signal noise in joystick axis 
		let joystickIndex = parseInt(inputDeviceName.match(/js([0-9]+)/)[1]);
		var joystick = new Joystick(joystickIndex, 3500, 350);
		//joystick.on('button', console.log)
		//joystick.on('axis', console.log)
	}

	let gameName = Object.keys(games)[gameID];
	let game = games[gameName];

	let lastTriggerTime = 0;

	if (testing) {
		mainTrigger_func = func; // for testing
		return;
	}

	if (inputDeviceName.startsWith("js")) {
		joystick.on("button", data => {
			let {number, value, time, init, type, id} = data;
			//console.log(`Button:${number};${value}`);
			if (number == 0 && value) {
				game.primaryAction();
			}
		});
	} else {
		const {spawn} = require('child_process');

		function StartDeviceListener() {
			const ls = spawn('cat', ["/dev/input/" + inputDeviceName]);
			ls.stdout.on('data', (data) => {
				//console.log(`Device-listener standard output: ${data}`);
				// if it's been less than X ms, this is probably part of previous trigger; ignore
				if (Date.now() - lastTriggerTime < (game.minInputInterval || 150)) return;
				lastTriggerTime = Date.now();

				game.primaryAction();
			});
			ls.stderr.on('data', (data) => {
				console.log(`Device-listener standard-error: ${data}`);
			});
			ls.on('close', (code) => {
				console.log(`Device-listener process exited with code ${code}. Restarting...`);
				StartDeviceListener();
			});
		}
		StartDeviceListener();
	}

	if (lockVolume != null) {
		setInterval(() => {
			exec(`amixer set "Master" ${lockVolume}%`); //`
			//exec(`amixer set "Master" unmute`);
		}, 200);
	}

	if (testing) StartTesting();

	Log(`Initialized. Game: ${gameName}`); //`
}

function chroot(path) {
	return posix.chroot(path);
}

function Log(str) {console.log(str)}
function EscapeCHRoot() {
	var dir = "./tempCHRoot";
	if (!fs.existsSync(dir)) {
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