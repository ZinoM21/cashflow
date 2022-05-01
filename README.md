# Cashflow Board Game - Companion App

---

## Description

### Problem

When you want to play the board game [_Cashflow - How to get out of the rat race_](https://store.richdad.com/products/cashflow-board-game "CASHFLOW Board game (2020)") by the author Robert Kyosaki, you will encounter the problem of annoying calculations.
Because the game is about income and expenses, assets and liabilities, and the interaction of these, it forces you to do calculations **all the time**.

You could do them all by hand, but that will 
* increase the time spent playing this game and
* decrease the game fun.

### Motivation

Because the already [existing companion mobile app](https://apps.apple.com/us/app/cashflow-financial-statement-calculator/id419229056 "CASHFLOW Financial Statement Calculator") for this board game is 
1. old
2. not responsive
3. not well designed
4. and only for iOS devices

I wanted to develop a beautiful, responsive and intuitie web app which runs on every browser and operating system.

### Solution

It should calculate important measures of game progress (like assets, liabilities, income from salary and cash flow from assets, expenses from taxes, liabilities and other) so that the user can focus on the game and not the calculations.

The app should do that while also being very intuitively designed so that every user knows exactly what to do.

---

## Features

### Minimum Viable Product

>As a user, I want to see my (fictional) balance and be able to change it by getting income from payday and paying expenses.

>As a user, I want to see my collection of liabilities like mortgages and loans and be able to pay them off 

>As a user, I want to see my collection of assets like real estate, stocks, businesses and gold an be able to buy and sell these assets

### Nice-to-have features

* having a starting point where one could choose different professions and so also different income starting levels
* switching from the inner ring of the board to the “fast track” (later in the game)
* being able to use only one device for the whole game, so that only one user operates the app (game master function)
* being able to connect different devices, so that everyone can see other players in his interface (multiplayer function)

---

## Challenges along the Way
more to come here

---

## How to Install and  Run the application

### 1. Install the latest python3 version

You should install a version of python3. On Mac, it should cone pre-installed but you should consider updating if you do not have a version of python3 but python2 (check your version by running `python3 --version` in the command line).

### 2. Create a virtual environment

Because the project will have some required packages like flask and we do not want to interfere with all the packages on your computer, you have to create a virtual environment. Enter `python3 -m venv venv` into the command line.

> Note: It is crucial that you do this step while being in the right directory. This should be a copy of this GitHub repository on your computer.

If you want to run your local flask server, you will need to do that with the virtual environment activated.

To activate your virtual environment, type `source venv/bin/activate` on Mac & Linux.

(Be sure deactivate the virtual environment when you want to use the command line like normal again. Run `deactivate` for that. If the comamnd line doesn't show "(venv)" it means, the environment isn't active.)

### 3. Define environment variables in a .env file

First, create a .env file inside of the directory. In here you have to set some basic variables for your virtual environment to work properly.

Paste these in the .env file and save:

`FLASK_ENV=development`

`DATABASE_URL=sqlite:///database.db`

`FLASK_APP=run.py`

`SECRET_KEY=`

> Important: you need to set a secret key after the equal sign. You can fin random keys [here](https://randomkeygen.com).

### 4. Install all required packages

> Be sure that your virtual environment is activated!

Then run `python -m pip install -r requirements.txt`

This will install all packages that are used in this project automatically. No need to install extra packages.

### 5. Database Setup

You will need to run four commands in your terminal to set up the database and fill it with some initial data for the game:

> Be sure that your virtual environment is activated and you did step 4!

1. `flask db init`
2. `flask db migrate -m 'first migration'`
3. `flask db upgrade`
4. `python -m app.scripts.seed`

### 6. Run the server

Now everything is ready to run:

* Run the server with `flask run`
* Stop the server with the keyboard shortcut ctrl+c

---

## How to Use 

It is pretty easy. 

If you want to start a game, press start playing on the landing page or in the navigation bar.

If you want to log in to save your games, click the account button at the top right.

If you want to go to the landing page, just click on the "Cashflow Companion" logo at the top left. 

> If you have other questions, go to /faq while the server runs.

---

## Credits
more to come here