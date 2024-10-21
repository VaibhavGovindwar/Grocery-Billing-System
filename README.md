# Grocery-Billing-System

## Project Overview

This is a Python-based billing system for a grocery store. It allows users to enter item names and their prices, calculates the total cost, and applies a 5% discount on the final bill. The program outputs a neatly formatted bill using the `PrettyTable` library for a professional look. The program continuously accepts input until the user decides to quit by typing "q", and then displays the final total with the discount applied.

## Features

- **Itemized Bill**: Add multiple items with their prices and see a well-structured bill.
- **Discount Calculation**: Automatically applies a 5% discount on the total amount.
- **Input Validation**: The system continuously accepts valid input until the user decides to quit.
- **Neat Formatting**: The final bill is displayed in a tabular format using the PrettyTable library.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/VaibhavGovindwar/grocery-store-billing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd grocery-store-billing
   ```

3. Install the required dependency:
   ```bash
   pip install prettytable
   ```

4. Run the program:
   ```bash
   python grocery_store.py
   ```

5. Enter item names and prices. Type 'q' when done.

## Sample Output

Here’s an example of how the output looks:

```
------ Welcome to V Grocery Store ------
Enter Item Name: shampoo
Enter the price: 98
Enter Item Name: soap
Enter the price: 49
Enter Item Name: wheat flour
Enter the price: 110
Enter Item Name: tooth brush
Enter the price: 25
Enter Item Name: q
+-------------+--------------+
| Item Name:  | Item Price:  |
+-------------+--------------+
|   shampoo   |      98      |
|     soap    |      49      |
| wheat flour |     110      |
| tooth brush |      25      |
|   Discount  |     14.1     |
|    Total    |    267.9     |
+-------------+--------------+

 Your Total Amount is:  267.9

Thank you for Shopping
 Have a Nice Day

```
## Screenshots
### 1. **Adding Items**  
![Screenshot 2024-10-21 194555](https://github.com/user-attachments/assets/00b6bc91-4021-4711-bf8b-da81bac276f5)
### 2. **Displaying Bill**  
![Screenshot 2024-10-21 194606](https://github.com/user-attachments/assets/066a1627-41a9-48bd-8ef0-c10d22f13d9d)
## Future Enhancements
- **CSV Integration**: Create a `grocery.csv` file to store item data, making it reusable for future sessions.
- **User Interface**: Build a graphical interface to make the program more user-friendly and accessible.
## Technologies Used
- **Python**: Core logic for the billing system.
- **PrettyTable**: For displaying the itemized bill in a tabular format.
## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request to suggest improvements or fix bugs.
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
