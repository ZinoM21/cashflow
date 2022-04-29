const setupDiv = document.querySelector('#setup');
const gameDiv = document.querySelector('#game')

// ---- Functions for later use ----

// Get data with route to API
async function getData(url) {
    console.log("Before fetch")
    const response = await fetch(url);
    console.log("After fetch")
    
    // Storing data in form of JSON
    var jsonData = await response.json();

    return jsonData
} 

// Display name of profession in HTML
function show(id, data) {
    data.filter(function (entry) {
        if (entry.id === id) {
            document.getElementById("randomizedProfession").innerHTML = entry.Name;
            document.getElementById("hiddenID").innerHTML = entry.id;
        }
    });
}

// Functions:
let clearPreviousErrors = () => document.querySelectorAll('.generatedErrors').forEach( (e) => e.remove());

let AddNewErrors = (messages) => {
    for (let i = 0; i < messages.length; i++) {
        const newP = document.createElement("p");
        newP.setAttribute("class", "generatedErrors")
        newP.setAttribute("id", "error")
        newP.innerText = messages[i];
        setupDiv.appendChild(newP);
    }
}



// --------------- SETUP --------------

// ---- PICK PROFESSION ----

const pickProfession = document.getElementById('pickProfession');

pickProfession.addEventListener('click', (e) => {
    
    // Get data with route to API
    // Storing data in form of JSON)
    console.log("In event listener, Before fetch")
    getData(api_url).then( professions_json => {

        // Create list of the ids of all professions
        var ids_list = [];
        for (let profession of professions_json) {
            ids_list.push(profession["id"]);
        };

        // Get one random profession
        var random_profession_id = ids_list[Math.floor(Math.random() * ids_list.length)];

        // Display name of profession in HTML
        show(random_profession_id, professions_json);
    });
});



// ---- SET DREAM ----

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



// ---- START BUTTON ----

const startButton = document.getElementById('start');

startButton.addEventListener('click', (e) => {
    
    e.preventDefault()

    var chosenProfessionID = document.getElementById("hiddenID").innerText;
    var chosenDream = writtenDream.innerText;

    

    if (chosenProfessionID && chosenDream) {
        
        setupDiv.style.display = 'none';
        gameDiv.style.display = 'grid';

        initialize_stats(chosenProfessionID, chosenDream);
        
        // var xhr = new XMLHttpRequest();
        // xhr.open("POST", post_url, true);
        // xhr.setRequestHeader('Content-Type', 'application/json');
        // xhr.send(JSON.stringify({
        //     id: chosenProfessionID,
        //     dream: chosenDream
        //     }));
        // xhr.onload = function() {
        //     var new_url = this.responseURL;
        //     console.log(this.response);
        //     window.location.href=new_url + "/" + chosenProfessionID + "/" + chosenDream;
        // };
    } else {
        let messages = []
        messages.push('Please pick a profession & write down your dream.');
        clearPreviousErrors();
        AddNewErrors(messages);
        }
    
});






// ------------- THE GAME -----------------


// --- Initialize stats ---
async function initialize_stats(id, dream) {

    // Get data with route to API
    // Storing data in form of JSON
    var chosenProfession = {};
    await getData(api_url).then( professions_json => {
        professions_json.filter(function (entry) {
            if (entry.id == id) {
                chosenProfession = entry;
            };
        });
    });


    // --- Set variables ---
    var profName = chosenProfession["Name"]

    var cashflow = parseInt(chosenProfession["Cashflow"]);
    var salary = parseInt(chosenProfession["Salary"]);
    var totalIncome = cashflow + salary;

    var taxes = parseInt(chosenProfession["Taxes"]);
    var otherExp = parseInt(chosenProfession["Other Expenses"]);
    var homePayment = parseInt(chosenProfession["Home Mortgage Payment"]);
    var schoolPayment = parseInt(chosenProfession["School Loan Payment"]);
    var carPayment = parseInt(chosenProfession["Car Loan Payment"]);
    var creditPayment = parseInt(chosenProfession["Credit Card Payment"]);
    var bankPayment = parseInt(chosenProfession["Bank Loan Payment"]);

    var expenses = taxes + otherExp + homePayment + schoolPayment + carPayment + creditPayment + bankPayment;

    var payday = totalIncome - expenses;

    var homeLoan = parseInt(chosenProfession["Home Mortgage"]);
    var schoolLoan = parseInt(chosenProfession["School Loans"]);
    var carLoan = parseInt(chosenProfession["Car Loans"]);
    var creditDebt = parseInt(chosenProfession["Credit Card Debt"]);


    // Add initial stats to view
    document.getElementById('headingGame').innerText = profName;

    document.getElementById('cashflowTotalNUM').innerText = cashflow;
    document.getElementById('salaryNUM').innerText = salary;
    document.getElementById('totalIncomeNUM').innerText = totalIncome;
                                        
    document.getElementById('expensesTopNUM').innerText = expenses;
    document.getElementById('expensesBottomNUM').innerText = expenses;
   
    var expensesListElementTaxes = createListElement("Taxes", taxes);
    document.getElementById('expensesListContainer').appendChild(expensesListElementTaxes);

    var expensesListElementOther = createListElement("Other Expenses", otherExp);
    document.getElementById('expensesListContainer').appendChild(expensesListElementOther);

    var expensesListElementHome = createListElement("Home Mortgage Payment", homePayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementHome); 
    
    var expensesListElementSchool = createListElement("School Loan Payment", schoolPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementSchool);
    
    var expensesListElementCar = createListElement("Car Loan Payment", carPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementCar);

    var expensesListElementCredit = createListElement("Credit Card Payment", creditPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementCredit);

    var expensesListElementBank = createListElement("Bank Loan Payment", bankPayment);
    document.getElementById('expensesListContainer').appendChild(expensesListElementBank);
    

    var liabilitiesListElementHome = createListElement("Home Mortgage", homeLoan);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementHome);

    var liabilitiesListElementSchool = createListElement("School Loans", schoolLoan);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementSchool);

    var liabilitiesListElementCar = createListElement("Car Loans", carLoan);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementCar);

    var liabilitiesListElementCredit = createListElement("Credit Card Debt", creditDebt);
    document.getElementById('liabilitiesContainer').appendChild(liabilitiesListElementCredit);


    document.getElementById('paydayNUM').innerText = payday;
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