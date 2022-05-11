import {player, render_stats} from "./setup.js";


// ------------- THE GAME -----------------

class Game {
    constructor (player) {
        this.player = player;
        this.startingTime = Date.now()
    }
}

const game = new Game();

// ----- Event Listeners for all buttons -----

const buy = document.getElementById('Buy')
const sell = document.getElementById('Sell')
const pay = document.getElementById('Pay')
const collect = document.getElementById('Collect')
const downsized = document.getElementById('Downsized')
const doodad = document.getElementById('Doodad')
const takeout = document.getElementById('TakeOut')
const payoff = document.getElementById('PayOff')


collect.addEventListener ("click", (e) => {
    player.addToLedger("PayDay", player.payday());
    render_stats(player);
});

downsized.addEventListener ("click", (e) => {
    player.addToLedger("Downsized!", player.getDownsized());
    render_stats(player);
});