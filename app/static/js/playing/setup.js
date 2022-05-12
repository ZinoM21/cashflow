
// -------------------- SETUP --------------------

// --- OBJECTS FOR BELOW ---

// Define object for storing API data in
class APIData{
    constructor () {
        this.json_data = null;
    };
};
const allProfessionsData = new APIData();


// -------- PICK PROFESSION --------

const pickProfession = document.getElementById('pickProfession');

pickProfession.addEventListener('click', (e) => {
    
    var ids_list = [];
    for (let profession of allProfessionsData.json_data) {
        ids_list.push(profession["id"]);
    };

    // Get one random profession
    var random_profession_id = ids_list[Math.floor(Math.random() * ids_list.length)];

    // Display name of profession in HTML
    show(random_profession_id, allProfessionsData.json_data);
});


// --- Functions for above -----

// Get data with route to API
async function getData(url, data_object) {
    // Fetch and store response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    data_object.json_data = await response.json();
}; 
getData(api_url, allProfessionsData);

// Display name of profession in HTML
function show(id, data) {
    data.filter(function (entry) {
        if (entry.id === id) {
            document.getElementById("randomizedProfession").innerHTML = entry.Name;
            document.getElementById("hiddenID").innerHTML = entry.id;
        }
    });
}


// -------- SET DREAM --------

const dreamButton = document.getElementById('chooseDream');
const dreamInput = document.getElementById('dreamInput');
const dreamSetter = document.getElementById('dreamSetter');
const dreamHeading = document.getElementById('dreamHeading');
const writtenDream = document.getElementById('writtenDream');

dreamButton.addEventListener('click', (e) => {
    dreamInput.style.display = "inline-block";
    dreamSetter.style.display = "inline-block";
    dreamHeading.style.display = "none";
    writtenDream.style.display = "none";
});

dreamSetter.addEventListener('click', (e) => {
    dreamInput.style.display = "none";
    dreamSetter.style.display = "none";
    dreamHeading.style.display = "block";
    writtenDream.style.display = "block";
    writtenDream.innerHTML = dreamInput.value;
});







// ----------- START -------------

// --- OBJECTS FOR BELOW ---

// Define object for player
class Player {
    constructor (id, dream) {
        this.professionID = id;
        this.dream = dream;
        this.ledger_array = [];
    };

    // Getter
    getCashflow() {
        if (this.cashflow_dict) {
            return Object.values(this.cashflow_dict).reduce((a, b) => a + b);
        }
        else {
            return 0;
        };
    };

    getExpenses() {
        if (this.expenses_dict) {
            return Object.values(this.expenses_dict).reduce((a, b) => a + b);
        }
        else {
            return 0;
        };
    };

    getTotalIncome() {
        return this.salary + this.getCashflow();
    };

    getPayday() {
        return this.getTotalIncome() - this.getExpenses();
    };

    getProgress() {
        return this.getExpenses() / this.getCashflow();
    };

    getCash() {
        let sum = 0;
        if (this.ledger_array) {
            for (const ledger_entry of this.ledger_array) {
                sum = sum + ledger_entry["amount"];
            };
        };
        return sum
    };

    getDownsized() {
        return this.getExpenses() * (-1);
    };


    addToLedger(reference, amount) {
        this.ledger_array.push({"reference": reference, "amount": amount})
    };

};
const player = new Player();

// ---- START BUTTON ----

const startButton = document.getElementById('start');

startButton.addEventListener('click', (e) => {
    
    var inputID = document.getElementById("hiddenID").innerText;
    var inputDream = writtenDream.innerText;

    if (inputID && inputDream) {
        
        changeToGameView();

        player.professionID = inputID;

        player.dream = inputDream;

        initialize_stats(player, allProfessionsData.json_data);

        render_stats(player);
    
    } else {
        let messages = []
        messages.push('Please pick a profession & write down your dream.');
        clearPreviousErrors();
        AddNewErrors(messages);
        }
    
});


// --- FUNCTIONS FOR ABOVE -----

// Add errors
let clearPreviousErrors = () => document.querySelectorAll('.generatedErrors').forEach( (e) => e.remove());

let AddNewErrors = (messages) => {
    for (let i = 0; i < messages.length; i++) {
        const newP = document.createElement("p");
        newP.setAttribute("class", "generatedErrors")
        newP.setAttribute("id", "error")
        newP.innerText = messages[i];
        document.querySelector('#setup').appendChild(newP);
    }
}

function changeToGameView() {
    document.querySelector('#setup').style.display = 'none';
    document.querySelector('#game').style.display = 'grid';
};


// Initialize stats of chosen profession and store in player object
function initialize_stats(player, data) {

    // --- Set variables ---
    for (let profession of data) {
        if (player.professionID == profession["id"]) {

            player.professionName = profession["Name"]

            player.salary = parseInt(profession["Salary"]);

            player.expenses_dict = {
                "Taxes": parseInt(profession["Taxes"]),
                "Other Expenses": parseInt(profession["Other Expenses"]),
                "Home Mortgage Payment": parseInt(profession["Home Mortgage Payment"]), 
                "School Loan Payment": parseInt(profession["School Loan Payment"]),
                "Car Loan Payment": parseInt(profession["Car Loan Payment"]),
                "Credit Card Payment": parseInt(profession["Credit Card Payment"]),                
                "Bank Loan Payment": parseInt(profession["Bank Loan Payment"]),
            };
        
        
            player.addToLedger("PayDay", player.getPayday());

            player.liabilities_dict = {
                "Home Mortgage": parseInt(profession["Home Mortgage"]),
                "School Loans": parseInt(profession["School Loans"]),
                "Car Loans": parseInt(profession["Car Loans"]),
                "Credit Card Debt": parseInt(profession["Credit Card Debt"]),
            };
        
            player.progressPercentage = Math.round((player.getCashflow() / player.getExpenses()) * 100)
        };  
    };
}

function render_stats(player) {
    // Add stats to view

    // Income
    document.getElementById('headingGame').innerText = player.professionName;
    document.getElementById('cashflowTotalNUM').innerText = player.getCashflow();
    renderList(player.cashflow_dict, document.getElementById('cashflowContainer'));
    
    document.getElementById('salaryNUM').innerText = player.salary;
    document.getElementById('totalIncomeNUM').innerText = player.getTotalIncome();

    // Assets
    renderList(player.assets_dict, document.getElementById('assetsContainer'));                       

    // Expenses
    document.getElementById('expensesTopNUM').innerText = player.getExpenses();
    document.getElementById('expensesBottomNUM').innerText = player.getExpenses();
   
    renderList(player.expenses_dict, document.getElementById('expensesContainer'));

    // Liabilities
    renderList(player.liabilities_dict, document.getElementById('liabilitiesContainer'));

    // Ledger
    renderList(player.ledger_array, document.getElementById('ledgerContainer'));

    // Cash
    document.getElementById('cashNUM').innerText = player.getCash() + "€";

    // Payday
    document.getElementById('paydayNUM').innerText = player.getPayday();

    // Progress bar
    setProgress(player.progressPercentage);
};


// Creates and adds an entry for the list of cashflow, assets, ledger, liabilities and expenses to DOM 
function createListElement (name, number) {
    const element = document.createElement("div");
    element.setAttribute("class", "ListElement");

    const elementName = document.createElement("span");
    elementName.setAttribute("class", "ListElementName");
    elementName.innerText = name;
    element.appendChild(elementName);

    const elementNumber = document.createElement("span");
    elementNumber.setAttribute("class", "ListElementNumber");
    elementNumber.innerText = number + "€";
    element.appendChild(elementNumber);

    return element
};


// Creates a list of entries for cashflow, assets, ledger, liabilities and expenses
function renderList (dict_or_array, html_container) {

    // remove all previous entries from DOM 
    while (html_container.lastElementChild) {
        html_container.removeChild(html_container.lastElementChild);
    };

    // adds everything inside the dict_or_array to DOM
    if (dict_or_array) {
        // For the ledger, because it is an array of dicts
        if (typeof dict_or_array === "object" && Array.isArray(dict_or_array)) {
            for (const dict of dict_or_array) {
                if (parseInt(dict["amount"]) >= 0) {
                    html_container.appendChild(createListElement(dict["reference"], "+" + parseInt(dict["amount"])));
                }
                else {
                    html_container.appendChild(createListElement(dict["reference"], parseInt(dict["amount"])));
                };
            };
        }
        // For everything else that needs a list, because they are all only dicts
        else {
            for (const [key, value] of Object.entries(dict_or_array)) {
                if (value > 0) {
                    html_container.appendChild(createListElement(key, value));
                };
            };
        };
    };
};


// sets progress bar to correct position based on cashflow and expenses
function setProgress (percent) {
    const percentage = document.getElementById('percentage');
    percentage.innerText = percent;

    const bar = document.getElementById('progressBarInner');
    bar.style.width = String(percent) + "%";
};

export {player, render_stats};