let {TapScreen, TypeString, PressKey, TapScreen_2} = require("./InputSimulator");

function TapScreen_2_Portrait(x, y) {
    TapScreen_2(35 + (x * .3), y);
}

module.exports = {
    lockVolume: 100,
    primaryDevice_searchString: "Satechi",
    secondaryDevice_searchString: "",
    games: {
        "Smash Cops Heat": {
            primaryAction: ()=> {
                TapScreen_2(5, 90);
                //TypeText("t");
                //PressKey("KEYCODE_T");
                //PressKey(48);
                console.log("Doing ram.");
            },
        },
        "Getaway": {
            primaryAction: ()=> {
                PressKey(66);
            },
        },
        "World of Tanks Blitz": {
            primaryAction: ()=> {
                console.log("Firing weapon.");
                TapScreen_2(87, 68);
            },
        },
        "Modern Air Combat": {
            primaryAction: ()=> {
                console.log("Firing weapon.");
                TapScreen_2(99, 30, 0, 9);
                setTimeout(()=> {
                    clickIndex = global.lastClickIndex == 8 ? 7 : 8; 
                    TapScreen_2(99, 60, 3000, clickIndex);
                    global.lastClickIndex = clickIndex;
                }, 200);
            },
        },
        "Stickman Soccer": {
            primaryAction: ()=> {
                TapScreen_2(88, 77 - 5, 100, 9);
            },
        },
        "Stickman Football": {
            minInputInterval: 500,
            primaryAction: ()=> {
                //console.log("Acting...");
                TapScreen_2(88, 77 - 5, 100, 9);
                //TapScreen_2(85, 90, 0, 9);
                /*setTimeout(()=> {
                    TapScreen_2(99, 60, 500, 9);
                }, 200);*/
            },
        },
        "War Machines": {
            primaryAction: ()=> {
                TapScreen_2(85, 90);
            },
        },
        "War Wings": {
            primaryAction: ()=> {
                TapScreen_2(90, 90);
            },
        },
        "Gunship Strike": {
            primaryAction: ()=> {
                TapScreen_2(90, 90, 1000, 9);
            },
        },
        "Tactile Wars": {
            primaryAction: ()=> {
                TapScreen_2(95, 0);
            },
        },
        "Stickman Hockey": {
            primaryAction: ()=> {
                TapScreen_2(88, 77 - 5, 100, 9);
            },
        },
        "Double-Turret Tank Game": {
            primaryAction: ()=> {
                TapScreen_2(77, 90);
                TapScreen_2(90, 90);
            },
        },
        "Smashy Road": {
            primaryAction: ()=> {
                TapScreen_2(25, 50);
            },
        },
        "Crash of Cars": {
            primaryAction: ()=> {
                TapScreen_2(90, 30);
            },
        },
        "Skid Police": {
            primaryAction: ()=> {
                TapScreen_2(80, 90);
            },
        },  
        "Overload": {
            primaryAction: ()=> {
                TapScreen_2(92, 55);
                TapScreen_2(85, 57);
            },
        },
        "Kion": {
            primaryAction: ()=> {
                TapScreen_2(92, 88);
            },
        },
        "Bike Game": {
            primaryAction: ()=> {
                TapScreen_2(90, 65);
            },
        },
        "Clash Royale": {
            primaryAction: ()=> {
                // use card in front of king tower
                TapScreen_2_Portrait(Math.random() * 100, 70);
                
                let random = Math.random();
                if (random <= 1/4) TapScreen_2_Portrait(25, 90);
                else if (random <= 2/4) TapScreen_2_Portrait(45, 90);
                else if (random <= 3/4) TapScreen_2_Portrait(65, 90);
                else if (random <= 4/4) TapScreen_2_Portrait(85, 90);
            },
        },
    }
};