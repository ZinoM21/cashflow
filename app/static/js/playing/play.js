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

const market_action = document.getElementById('marketAction')
const buy = document.getElementById('Buy')
const sell = document.getElementById('Sell')
const pay = document.getElementById('Pay')
const collect = document.getElementById('Collect')
const downsized = document.getElementById('Downsized')
const doodad = document.getElementById('Doodad')
const takeout = document.getElementById('TakeOut')
const payoff = document.getElementById('PayOff')


collect.addEventListener ("click", (e) => {
    player.addToLedger("PayDay", player.getPayday());
    render_stats(player);
});

downsized.addEventListener ("click", (e) => {
    player.addToLedger("Downsized!", player.getDownsized());
    render_stats(player);
});

takeout.addEventListener("click", (e) => {
    player.takeOutLoan();
});

pay.addEventListener("click", (e) => {
    popupPay(createPopUpContainer());
    let popupContainerBG = document.getElementById("popupPayContainerBG")
    let charityButton = document.getElementById("charityButton");
    let cancelButton = document.getElementById("cancelButton");

    cancelButton.onclick = () => {
        popupContainerBG.remove()
        render_stats(player);
    };

    charityButton.onclick = () => {
        player.addToLedger("Charity Donation", player.getTotalIncome() * 0.1 * (-1));
        popupContainerBG.remove()
        render_stats(player);
    };
});

let createPopUpContainer = () => {
    let popupContainerBG = document.createElement("div");
    popupContainerBG.setAttribute("class", "popupContainerBG");
    popupContainerBG.setAttribute("id", "popupPayContainerBG");
    document.querySelector("main").appendChild(popupContainerBG);
    
    let popupContainer = document.createElement("div");
    popupContainer.setAttribute("class", "popupContainer");
    popupContainerBG.appendChild(popupContainer);

    let cancelButton = document.createElement("div");
    cancelButton.setAttribute("id", "cancelButton");
    popupContainer.appendChild(cancelButton);

    return popupContainer
};

let popupPay = (popupContainer) => {
    let heading = document.createElement("h1");
    heading.innerText = "Pay";
    popupContainer.appendChild(heading);

    let charityButton = document.createElement("button");
    charityButton.setAttribute("class", "button");
    charityButton.classList.add("popupButton");
    charityButton.setAttribute("id", "charityButton");
    charityButton.innerText = "Charity";
    popupContainer.appendChild(charityButton);

    let lendmoneyButton = document.createElement("button");
    lendmoneyButton.setAttribute("class", "button");
    lendmoneyButton.classList.add("popupButton");
    lendmoneyButton.innerText = "Lend Money";
    popupContainer.appendChild(lendmoneyButton);

    let paymoneyButton = document.createElement("button");
    paymoneyButton.setAttribute("class", "button");
    paymoneyButton.classList.add("popupButton");
    paymoneyButton.innerText = "Pay Money";
    popupContainer.appendChild(paymoneyButton);
};

let removeAllWithClass = (className) => {
    document.querySelectorAll(className).forEach(e => e.remove())
};


export {market_action, buy, sell, pay, collect, downsized, doodad, takeout, payoff}