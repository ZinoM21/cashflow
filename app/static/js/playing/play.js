import {player, render_stats, createListElement} from "./setup.js";



// ------------- THE GAME -----------------

class Game {
    constructor (player) {
        this.player = player;
        this.startingTime = Date.now();
        this.bankLoanInterest = 10;
    }

    // Getter
    getBankLoanInterest() {
        return this.bankLoanInterest;
    };
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
    popupLoan(createPopUpContainer());
    player.takeOutLoan();
});

pay.addEventListener("click", (e) => {
    popupPay(createPopUpContainer());
    let popupContainerBG = document.getElementById("popupContainerBG")
    let charityButton = document.getElementById("charityButton");
    let cancelButton = document.getElementById("cancelButton");

    cancelButton.onclick = () => {
        popupContainerBG.remove()
        render_stats(player);
    };

    charityButton.onclick = () => {
        player.charity();
        popupContainerBG.remove()
        render_stats(player);
    };
});



// ------- Functions -------

// Creates basic popup structure
let createPopUpContainer = () => {
    let popupContainerBG = document.createElement("div");
    popupContainerBG.setAttribute("id", "popupContainerBG");
    document.querySelector("main").appendChild(popupContainerBG);
    
    let popupContainer = document.createElement("div");
    popupContainer.setAttribute("class", "popupContainer");
    popupContainerBG.appendChild(popupContainer);

    let cancelButton = document.createElement("div");
    cancelButton.setAttribute("id", "cancelButton");
    popupContainer.appendChild(cancelButton);

    return popupContainer
};

// Fills popup Container with content/views for PAY button
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


// Fills popup Container with content/views for taking out a loan
let popupLoan = (popupContainer) => {
    let heading = document.createElement("h1");
    heading.innerText = "Take out loan";
    popupContainer.appendChild(heading);



    let description = document.createElement("div");
    description.setAttribute("id", "loanDescription");
    popupContainer.appendChild(description);

    let firstP = document.createElement("p");
    firstP.innerText = "Bank loans have " + game.getBankLoanInterest() + "% interest."
    firstP.setAttribute("class", "loan-p")
    description.appendChild(firstP)

    let secondP = document.createElement("p");
    secondP.innerText = "This interest reduces your Payday."
    secondP.setAttribute("class", "loan-p")
    description.appendChild(secondP)



    let input = document.createElement("input");
    input.setAttribute("id", "loan_amount");
    input.setAttribute("type", "number");
    input.setAttribute("name", "loan_amount");
    input.setAttribute("placeholder", "e.g. 10000");
    input.setAttribute("required", "");
    popupContainer.appendChild(input);



    let loanEffects = document.createElement("div");
    loanEffects.setAttribute("class", "flexList");
    loanEffects.setAttribute("id", "loanEffects");
    popupContainer.appendChild(loanEffects);

    let heading2 = document.createElement("h2");
    heading2.innerText = "Effects of taking out loan:"
    loanEffects.appendChild(heading2);

    let currentPayday = createListElement("Current PayDay:", player.getPayday());
    currentPayday.lastElementChild.setAttribute("id", "loan-current_payday");
    loanEffects.appendChild(currentPayday);

    let newPayday = createListElement("New PayDay:", player.getPayday());
    newPayday.lastElementChild.setAttribute("id", "loan-new_payday");
    loanEffects.appendChild(newPayday);

    let currentCash = createListElement("Current Cash on Hand:", player.getCash());
    currentCash.lastElementChild.setAttribute("id", "loan-current_cash");
    loanEffects.appendChild(currentCash);

    let newCash = createListElement("New Cash on Hand:", player.getCash());
    newCash.lastElementChild.setAttribute("id", "loan-new_cash");
    loanEffects.appendChild(newCash);

    let loanAmount = createListElement("Loan Amount:", 0);
    loanAmount.lastElementChild.setAttribute("id", "loan-loan_amount");
    loanEffects.appendChild(loanAmount);

    let loanInterest = createListElement("Loan Interest Payment:", 0);
    loanInterest.lastElementChild.setAttribute("id", "loan-interest_payment");
    loanEffects.appendChild(loanInterest);



    let button = document.createElement("button");
    button.setAttribute("id", "takeOutLoan");
    button.setAttribute("class", "button");
    button.classList.add("popupButton");
    button.innerText = "Take Out Loan";
    popupContainer.appendChild(button);
};


export {market_action, buy, sell, pay, collect, downsized, doodad, takeout, payoff, popupLoan, createPopUpContainer, game}