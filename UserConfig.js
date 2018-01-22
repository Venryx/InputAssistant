let {TapScreen, TypeString, PressKey, TapScreen_2} = require("./InputSimulator");

module.exports = {
    lockVolume: 100,
    primaryDevice_searchString: "Satechi",
    secondaryDevice_searchString: "",
    games: {
        "Smash Cops Heat": {
            primaryAction: ()=> {
                //TapScreen(5, 90);
                //TypeText("t");
                //PressKey("KEYCODE_T");
                PressKey(48);
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
                /*setTimeout(()=> {
                    TapScreen_2(99, 60, 500, 9);
                }, 200);*/
            },
        },
    }
};