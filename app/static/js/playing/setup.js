

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
    
    console.log(allProfessionsData.json_data);
    
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
};


// ---- START BUTTON ----

const startButton = document.getElementById('start');

startButton.addEventListener('click', (e) => {
    
    var inputID = document.getElementById("hiddenID").innerText;
    var inputDream = writtenDream.innerText;

    if (inputID && inputDream) {
        
        changeToGameView();

        // for (let profession of allProfessionsData.json_data) {
        //     ids_list.push(profession["id"]);
        // };
        
        const player = new Player(inputID, inputDream);

        initialize_stats(player, allProfessionsData.json_data);

        console.log(player.professionID)

        //render_stats();
    
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

            player.cashflow = parseInt(profession["Cashflow"]);
            player.salary = parseInt(profession["Salary"]);
            player.totalIncome = player.cashflow + player.salary;
        
            player.taxes = parseInt(profession["Taxes"]);
            player.otherExp = parseInt(profession["Other Expenses"]);
            player.homePayment = parseInt(profession["Home Mortgage Payment"]);
            player.schoolPayment = parseInt(profession["School Loan Payment"]);
            player.carPayment = parseInt(profession["Car Loan Payment"]);
            player.creditPayment = parseInt(profession["Credit Card Payment"]);
            player.bankPayment = parseInt(profession["Bank Loan Payment"]);
        
            player.expenses = player.taxes + player.otherExp + player.homePayment + player.schoolPayment + player.carPayment + player.creditPayment + player.bankPayment;
        
            player.payday = player.totalIncome - player.expenses;
        
            player.cash = player.payday;
        
            player.homeLoan = parseInt(profession["Home Mortgage"]);
            player.schoolLoan = parseInt(profession["School Loans"]);
            player.carLoan = parseInt(profession["Car Loans"]);
            player.creditDebt = parseInt(profession["Credit Card Debt"]);
        
            player.progressPercentage = Math.round((player.cashflow / player.expenses) * 100)
        };  
    };


    // Add initial stats to view
    document.getElementById('headingGame').innerText = player.professionName;

    document.getElementById('cashflowTotalNUM').innerText = player.cashflow;
    document.getElementById('salaryNUM').innerText = player.salary;
    document.getElementById('totalIncomeNUM').innerText = player.totalIncome;
                                        
    document.getElementById('expensesTopNUM').innerText = player.expenses;
    document.getElementById('expensesBottomNUM').innerText = player.expenses;
   
    var expensesListElementTaxes = createListElement("Taxes", player.taxes);
    document.getElementById('expensesListContainer').appendChild(expensesListElementTaxes);

    var expensesListElementOther = createListElement("Other Expenses", player.otherExp);
    document.getElementById('expensesListContainer').appendChild(expensesListElementOther);

    var expensesListElementHome = createListElement("Home Mortgage Payment", player.homePayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementHome); 
    
    var expensesListElementSchool = createListElement("School Loan Payment", player.schoolPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementSchool);
    
    var expensesListElementCar = createListElement("Car Loan Payment", player.carPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementCar);

    var expensesListElementCredit = createListElement("Credit Card Payment", player.creditPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementCredit);

    var expensesListElementBank = createListElement("Bank Loan Payment", player.bankPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementBank);
    

    var liabilitiesListElementHome = createListElement("Home Mortgage", player.homeLoan);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementHome);

    var liabilitiesListElementSchool = createListElement("School Loans", player.schoolLoan);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementSchool);

    var liabilitiesListElementCar = createListElement("Car Loans", player.carLoan);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementCar);

    var liabilitiesListElementCredit = createListElement("Credit Card Debt", player.creditDebt);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementCredit);

    var cashElement = createListElement("Cash", player.cash);
    cashElement.setAttribute('id', 'cashElement');
    document.getElementById('ledgerContainer').appendChild(cashElement);

    document.getElementById('paydayNUM').innerText = player.payday;

    setProgress(player.progressPercentage);
}


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
}

function setProgress (percent) {
    const percentage = document.getElementById('percentage');
    percentage.innerText = percent;

    const bar = document.getElementById('progressBarInner');
    bar.style.width = String(percent) + "%";
}