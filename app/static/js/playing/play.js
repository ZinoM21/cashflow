

// ------------- THE GAME -----------------


class Game {
    constructor (Player) {
        this.Player = Player;
        this.startingTime = Date.now()
    }
}



// ----- Event Listeners for all buttons -----

const buy = document.getElementById('Buy')
const sell = document.getElementById('Sell')
const pay = document.getElementById('Pay')
const collect = document.getElementById('Collect')
const downsized = document.getElementById('Sell')
const doodad = document.getElementById('Doodad')
const takeout = document.getElementById('TakeOut')
const payoff = document.getElementById('PayOff')