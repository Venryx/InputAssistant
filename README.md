# InputAssistant

Translates input from a joystick/clicker into actions within Android games. (for Chromebooks with Android support)

### Setup

1) Download this repo to disk. (in crouton chroot)
2) Install [NodeJS](https://nodejs.org).
3) Run "npm install". (in repo folder)
4) Run "node ./FixNodeModules.js". (not actually necessary atm)
5) Run "apt-get install pip".
6) Run "pip install python-uinput".

### Usage

1) Connect joystick or bluetooth clicker/shutter button. (by default, uses shutter; can change in code)
2) Run "./Start.sh". (can run from ChromeOS using "enter-chroot" command)

Joystick/clicker actions will now translate into Android game actions, as specified in the script files.

### Troubleshooting

##### I get an error about ADB access not being authorized (old)

Before running the `Start.sh` script, open your Chromebook's crosh shell and type "adb connect 100.115.92.2", then "adb shell", then click "allow" in the permission-request dialog. (with "remember this computer" checked)

If it doesn't show the dialog, try restarting your Chromebook.