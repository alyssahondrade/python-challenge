# python-challenge
Module 3 Challenge - UWA/edX Data Analytics Bootcamp
Github repository at: [https://github.com/alyssahondrade/python-challenge.git](https://github.com/alyssahondrade/python-challenge.git)

## Table of Contents
1. [Introduction](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#introduction)
    1. [Goal - PyBank](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#goal---pybank)
    2. [Goal - PyPoll](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#goal---pypoll)
    3. [Repository Structure](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#repository-structure)
2. [Approach](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#approach)
    1. [PyBank](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#pybank)
    2. [PyPoll](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#pypoll)
4. [References](https://github.com/alyssahondrade/python-challenge/blob/main/README.md#references)

## Introduction
### Goal - PyBank
The goal of **PyBank** is to create a Python script that analyses the financial records of a company. Using the dataset `budget_data.csv`, calculate the following:
1. Total number of months in the dataset
2. Net total amount of "Profit/Losses" over the period
3. Changes in "Profit/Losses" over the period, and the average of those changes
4. The greatest increase in profits (date and amount) over the period
5. The greatest decrease in profits (date and amount) over the period

### Goal - PyPoll
The goal of **PyPoll** is to create a Python script that analyses the election votes of a small, rural US town.


### Repository Structure
- `PyBank/` directory contains
- `PyBank/analysis/` directory contains results for
- `PyBank/resources/` directory contains `budget_data.csv`
- `PyPoll/` directory
- `PyPoll/analysis/` directory contains results for
- `PyPoll/resources/` directory contains


## Approach
1. Setup the repository for the project, as per instructions.
2. Understand the dataset, the following observations were made:
    1. **PyBank** `budget_data.csv`
       1. Data consists of 2 columns, with a header in the first row.
       2. The first column consists of a date, with the format: `MMM-YY`, there are no duplicate values.
       3. The second column has both positive and negative values, all integers.
    2. **PyPoll** `election_data.csv`
       1. Data consists fo 3 columns, with a header in the first row.
       2. The first column is the Ballot ID, which can be considered as an integer.
       3. The second and third columns are strings.
       4. Using `Data > Remove Duplicates`:
           1. There are 3 unique values for county: `Jefferson, Denver, Arapahoe`.
           2. There are 3 unique values for candidate: `Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane`.
           3. There are nil duplicates for Ballot Id.

### PyBank
1. Import `budget_data.csv`.
2. Store the header row using `next()`.
3. Calculate the following:
    1. Total number of months, by incrementing `total_months` in the for-loop.
    2. Net total amount of `Profit/Losses`, by incrementing the sum of `net_profit` in the for-loop.
    3. Changes in `Profit/Losses`:
       1. Create a new list to capture the `Profit/Losses` column using the for-loop, called `profit_column`.
       2. Calculate and append the results to `average_change` list, in a for-loop outside the csv reader routine, called `changes`.
    4. Average changes, use the `mean` function from the `statistics` module over the `average_change` list.
    5. The greatest increase and decrease in profits:
       1. Create a new list to capture the `Date` column using the for-loop, called `date_column`.
       2. Using a for-loop and if-statements, hold and compare `greatest_increase` and `greatest_decrease` with each value in `changes`.
4. Format the results and store each string in a list `results_format`, this will avoid repetition when printing to both terminal and text file.
5. Define a relative output path for the text file: `analysis/PyBank_results.txt`
6. Use a for-loop to print to both terminal and text file.

### PyPoll

## References
