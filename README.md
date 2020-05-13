# Currency_Exchanger_Console
A very simple Command - Line Application written in python 3 which gets it's data from the https://exchangeratesapi.io/ API and let's you check out the latest currency change rates.

You can specify the amount you want to exchange from one currency to another or from one currency to all others that are available.

## Content

* [Installation](#Installation)
* [Usage](#Usage)

## Installation

First clone the repository with the `git clone` command. 
To use the curreny exchanger you should have installed python 3 on your machine.
Additional you need the `PrettyTable`- module and the `requests`- module.

To install them with the python package installer `pip` run `pip install requests` & `pip install Prettytable`.

## Usage

There are essentially two different ways how you can use this script.

**First**
* `python Currency_Exchanger <amount> <root_currency>`

This will give you all exchange rates and the exchanged amounts that are available with the provided currency as the root - currency.

**Second**
* `python Currency_Exchanger <amount> <root_currency> <target_currency>`

This will give you only the exchange rate and amount from the target - currency you provided.

**Other Things**

To get an overview of which currencies are available run:
* `python Currency_Exchanger currencies`

You can get help on how to use the tool by providing the help keyword or -h flag.
* `python Currency_Exchanger -h` or `python Currency_Exchanger help`
