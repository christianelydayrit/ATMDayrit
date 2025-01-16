# ATMDayrit
 
Python ATM System
This is a simple ATM System implemented in Python that uses .txt files to store and manage user accounts, passwords, and balances. The system provides essential ATM functionalities, ensuring secure and straightforward banking operations with validation and user-friendly prompts. I created this project during my 3rd year to practice and enhance my knowledge of Python.

Features:

-Create Account
Users can create an account with a name, 4-digit PIN, and initial deposit.
Checks if the account already exists before proceeding.
Saves account details (Name, PIN, Balance) securely in a .txt file.

-Withdraw Funds
Allows users to withdraw funds if their balance is sufficient.
Displays an error message if the withdrawal amount exceeds the balance.
Generates a receipt with details of the transaction (optional).

-Deposit Funds
Enables users to deposit money into their account.
Updates the balance and provides an option to generate a receipt.

-Transfer Funds
Allows transferring money to another user account.
Validates if the recipient account exists before processing the transfer.
Ensures sufficient balance in the sender's account.
Provides a receipt for both sender and recipient upon request.

-Check Balance
Displays the current account balance.
Validates the user's PIN before showing account details.

-Change PIN
Allows users to securely update their PIN.
Ensures the new PIN is confirmed before saving changes.

-Transaction Validation
Input errors such as invalid characters, incorrect PIN, or insufficient funds trigger appropriate error messages.
Prompts users to retry or cancel during invalid inputs.

-Post-Transaction Options
After every transaction, users are asked if they want to perform another transaction or exit.

-Receipts
Each money transaction (Withdraw, Deposit, Transfer) provides an option to generate a detailed receipt.
Receipts include:
Date & Time of Transaction
Account Name
Transaction Type
Amount Involved
Updated Account Balance

-Error Handling
Invalid inputs (e.g., letters in numeric fields, nonexistent accounts) result in clear error messages.
Users can retry or cancel the operation when an error occurs.



