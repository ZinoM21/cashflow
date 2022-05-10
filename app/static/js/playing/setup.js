
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
    };

    cashflow() {
        if (this.cashflow_dict) {
            return Object.values(this.cashflow_dict).reduce((a, b) => a + b);
        }
        else {
            return 0;
        }
    };

    assets() {
        if (this.assets_dict) {
            return Object.values(this.assets_dict).reduce((a, b) => a + b);
        }
    };

    expenses() {
        return Object.values(this.expenses_dict).reduce((a, b) => a + b);
    };

    liabilities() {
        return Object.values(this.liabilities_dict).reduce((a, b) => a + b);
    }

    totalIncome() {
        return this.salary + this.cashflow();
    };

    payday() {
        return this.totalIncome() - this.expenses();
    };

    progress() {
        return this.expenses() / this.cashflow();
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

            // player.cashflow = parseInt(profession["Cashflow"]);
            player.salary = parseInt(profession["Salary"]);
            // player.sumIncome();
            // player.totalIncome = player.cashflow + player.salary;

            player.expenses_dict = {
                "Taxes": parseInt(profession["Taxes"]),
                "Other Expenses": parseInt(profession["Other Expenses"]),
                "Home Mortgage Payment": parseInt(profession["Home Mortgage Payment"]), 
                "School Loan Payment": parseInt(profession["School Loan Payment"]),
                "Car Loan Payment": parseInt(profession["Car Loan Payment"]),
                "Credit Card Payment": parseInt(profession["Credit Card Payment"]),                
                "Bank Loan Payment": parseInt(profession["Bank Loan Payment"]),
            };
        
        
            player.cash = player.payday();

            player.liabilities_dict = {
                "Home Mortgage": parseInt(profession["Home Mortgage"]),
                "School Loans": parseInt(profession["School Loans"]),
                "Car Loans": parseInt(profession["Car Loans"]),
                "Credit Card Debt": parseInt(profession["Credit Card Debt"]),
            };
        
            player.progressPercentage = Math.round((player.cashflow() / player.expenses()) * 100)
        };  
    };
}

function render_stats(player) {
    // Add stats to view

    // Income
    document.getElementById('headingGame').innerText = player.professionName;
    document.getElementById('cashflowTotalNUM').innerText = player.cashflow();
    renderList(player.cashflow_dict, document.getElementById('cashflowContainer'));
    
    document.getElementById('salaryNUM').innerText = player.salary;
    document.getElementById('totalIncomeNUM').innerText = player.totalIncome();

    // Assets
    renderList(player.assets_dict, document.getElementById('assetsContainer'));                       

    // Expenses
    document.getElementById('expensesTopNUM').innerText = player.expenses();
    document.getElementById('expensesBottomNUM').innerText = player.expenses();
   
    renderList(player.expenses_dict, document.getElementById('expensesContainer'));

    // Liabilities
    renderList(player.liabilities_dict, document.getElementById('liabilitiesContainer'));

    // Ledger / Cash
    document.getElementById('cashNUM').innerText = player.cash + "€";

    renderList(player.ledger_dict, document.getElementById('ledgerContainer'));

    // Payday
    document.getElementById('paydayNUM').innerText = player.payday();

    // Progress bar
    setProgress(player.progressPercentage);
};

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

function renderList (dict, html_container) {
    while (html_container.lastElementChild) {
        html_container.removeChild(html_container.lastElementChild);
    };
    if (dict) {
        for (const [key, value] of Object.entries(dict)) {
            if (value > 0) {
                html_container.appendChild(createListElement(key, value));
            };
        };
    };
};

function setProgress (percent) {
    const percentage = document.getElementById('percentage');
    percentage.innerText = percent;

    const bar = document.getElementById('progressBarInner');
    bar.style.width = String(percent) + "%";
};

export {player, render_stats};