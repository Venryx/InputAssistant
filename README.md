# InputAssistant

Translates input from a joystick into actions within Android games. (for Chromebooks with Android support)

### Setup

1) Download this repo to disk.
2) Install NodeJS.
3) Run "npm install". (in repo folder)
4) Run "node ./FixNodeModules.js".

### Usage

1) Connect joystick.
2) Run "./Start.sh".

Joystick actions will now translate into Android game actions, as specified in the script files.

### Troubleshooting

##### I get an error about ADB access not being authorized

Before running the `Start.sh` script, open your Chromebook's crosh shell and type "adb connect 100.115.92.2", then "adb shell", then click "allow" in the permission-request dialog. (with "remember this computer" checked)

If it doesn't show the dialog, try restarting your Chromebook.