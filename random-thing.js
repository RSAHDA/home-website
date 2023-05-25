// -------------------------------------------------------------------------------
// VARIABLES THAT CAN BE CHANGED.

const DEFAULT_SPEED = 127 // 255 = 7 meters / seconds
const DEFAULT_TURN_DURATION = 2

// -------------------------------------------------------------------------------
var current_deg = 0 // records degrees

async function move(dis, speed=DEFAULT_SPEED) { // distance in cm
    await roll(current_deg, speed, (dis / 39.3701) / DEFAULT_SPEED);
}

async function turn(deg, time=DEFAULT_TURN_DURATION) {
    while (deg > 360)
    {
        deg -= 360
    }
    current_deg += deg
    await spin(current_deg, time);
}

async function setdeg(deg, time=DEFAULT_TURN_DURATION) {
    current_deg = deg
    await spin(deg, time);
}

async function startProgram() {
    // aim the bot at start orientation to begin.
    await move(32)
    await spin(90)

    await move(36)
    await spin(90)

    await move(18)
    await spin(90)

    await move(10)
    await setdeg(180)

    await move(10)
    await setdeg(90)

    await move(10)
    await spin(90)

    await move(18)
    await spin(90)

    await move(13)
    await setdeg(180)

    await move(10)
    await setdeg(90)

    await move(10)
    await setdeg(180)

    await move(18)
    await spin(90)

    await move(36)
    await spin(90)

    await move(32)
}

