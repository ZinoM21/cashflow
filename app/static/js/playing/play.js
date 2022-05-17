import {player, render_stats, createListElement, apiData} from "./setup.js";



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

buy.addEventListener("click", (e) => {
    popupBuy(createPopUpContainer());
    let popupContainerBG = document.getElementById("popupContainerBG")
    let cancelButton = document.getElementById("cancelButton");
    let stockButton = document.getElementById("stockButton")
    let realestateButton = document.getElementById("realestateButton")
    let businessButton = document.getElementById("businessButton")

    cancelButton.onclick = () => {
        popupContainerBG.remove()
        render_stats(player);
    };

    stockButton.onclick = () => {
        popupContainerBG.remove()
        popupStock(createPopUpContainer());
        let popupStockContainerBG = document.getElementById("popupContainerBG");
        let cancelButton = document.getElementById("cancelButton");
        let input_price = document.getElementById("input_price");
        let input_price_value = 0;
        let input_shares = document.getElementById("input_shares");
        let input_shares_value = 0;
        let total_stock_price_number = document.getElementById("total_stock_price_number");
        let next_button = document.getElementById("next_button")

        input_price.oninput = () => {
            input_price_value = parseInt(input_price.value)

            if (input_shares_value && input_shares_value) {
                total_stock_price_number.innerText = input_price_value * input_shares_value + "€";
            }
            else {
                total_stock_price_number.innerText = "0€"
            };
        };

        input_shares.oninput = () => {
            input_shares_value = parseInt(input_shares.value)

            if (input_shares_value && input_shares_value) {
                total_stock_price_number.innerText = input_price_value * input_shares_value + "€";
            }
            else {
                total_stock_price_number.innerText = "0€"
            };
        };

        cancelButton.onclick = () => {
            popupStockContainerBG.remove()
            render_stats(player);
        };

        next_button.onclick = () => {
            if (input_shares_value && input_shares_value) {
                let selected = document.forms['stockForm'].stockSelector.value;
                
                player.addStockToAssets(selected ,input_shares_value, input_price_value);
                player.addToLedger("Buy Stock " + selected, Math.round(input_shares_value * input_price_value * (-1)));

                popupStockContainerBG.remove()
                render_stats(player);
            };
        };

    };

    realestateButton.onclick = () => {
        popupContainerBG.remove()
        popupRealestate(createPopUpContainer());
    };

    businessButton.onclick = () => {
        popupContainerBG.remove()
        popupBusiness(createPopUpContainer());
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

let popupBuy = (popupContainer) => {
    let heading = document.createElement("h1");
    heading.innerText = "Buy";
    popupContainer.appendChild(heading);

    popupContainer.appendChild(document.createElement("br"));

    let heading2 = document.createElement("h2");
    heading2.innerText = "Opportunity";
    popupContainer.appendChild(heading2);

    let stockButton = document.createElement("button");
    stockButton.setAttribute("class", "button");
    stockButton.classList.add("popupButton");
    stockButton.setAttribute("id", "stockButton");
    stockButton.innerText = "Stock / Mutual";
    popupContainer.appendChild(stockButton);

    let realestateButton = document.createElement("button");
    realestateButton.setAttribute("class", "button");
    realestateButton.classList.add("popupButton");
    realestateButton.setAttribute("id", "realestateButton");
    realestateButton.innerText = "Real Estate";
    popupContainer.appendChild(realestateButton);

    let businessButton = document.createElement("button");
    businessButton.setAttribute("class", "button");
    businessButton.classList.add("popupButton");
    businessButton.setAttribute("id", "businessButton");
    businessButton.innerText = "Business";
    popupContainer.appendChild(businessButton);

};

let popupStock = (popupContainer) => {
    let heading = document.createElement("h1");
    heading.innerText = "Stock / Mutual";
    popupContainer.appendChild(heading)

    let form = document.createElement("form");
    form.setAttribute("id", "stockForm")
    popupContainer.appendChild(form);

    let selector = document.createElement("select");
    selector.setAttribute("name", "stockSelector");
    selector.setAttribute("id", "stockSelector");
    form.appendChild(selector);

    for (let option_dict of apiData.opportunities) {
        if (option_dict["category"] == "Stock / Mutual") {
            let option = document.createElement("option");
            option.setAttribute("value", option_dict["type"])
            option.innerText = option_dict["type"];
            selector.appendChild(option);
        };
    };

    let input_price = document.createElement("input");
    input_price.setAttribute("id", "input_price");
    input_price.setAttribute("type", "number");
    input_price.setAttribute("name", "input_price");
    input_price.setAttribute("placeholder", "Today's Price");
    input_price.setAttribute("required", "");
    popupContainer.appendChild(input_price);

    let input_shares = document.createElement("input");
    input_shares.setAttribute("id", "input_shares");
    input_shares.setAttribute("type", "number");
    input_shares.setAttribute("name", "input_shares");
    input_shares.setAttribute("placeholder", "Number of Shares");
    input_shares.setAttribute("required", "");
    popupContainer.appendChild(input_shares);


    let cash = createListElement("Cash on Hand:", player.getCash());
    popupContainer.appendChild(cash);

    let total_stock_price = createListElement("Total Price:", 0);
    total_stock_price.lastElementChild.setAttribute("id", "total_stock_price_number");
    popupContainer.appendChild(total_stock_price);

    let next_button = document.createElement("button");
    next_button.setAttribute("id", "next_button");
    next_button.setAttribute("class", "button");
    next_button.classList.add("popupButton");
    next_button.innerText = "Next";
    popupContainer.appendChild(next_button);

};

let popupRealestate = (popupContainer) => {

};

let popupBusiness = (popupContainer) => {

};


export {market_action, buy, sell, pay, collect, downsized, doodad, takeout, payoff, popupLoan, createPopUpContainer, game}