# Cryptocurrency Wallet

################################################################################

# Part Zero - Perform the initial imports
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

################################################################################

# Part One - Import Ethereum Transaction Functions into the Fintech Finder Application

# From `crypto_wallet.py import the functions generate_account, get_balance and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

# Fintech Finder Candidate Information
# This Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
candidate_database = {
    "Lane": ["Lane", "0x2B4CCc58879801dE607d9928bFe6bB38868e10BB", "4.3", .20, "lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

# Define the function 'get_people'
def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################

# Part Two - Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Define a new `st.sidebar.write` function that will display the balance of the customers account
ether_balance = get_balance(w3, account.address)

# Write the returned ether balance to the sidebar
st.sidebar.write(ether_balance)

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################

# Part Three - Sign and Execute a Payment Transaction

# Calculate the canadates total wage by multiplying the hourly rate by the number of hours worked
total_wage = hourly_rate * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(total_wage)

################################################################################# 

# Part Four - Call the `send_transaction` function and pass it three parameters:
if st.sidebar.button("Send Transaction"):

    # Create a variable that will take three parameters : account, candidate_address, & total_wage
    transaction_hash = send_transaction(w3, account, candidate_address, total_wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# Writes FinTech Finder candidates to the Streamlit page
get_people()

################################################################################