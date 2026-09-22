# Supermarket Billing System

## 📌 Project Overview

The **Supermarket Billing System** is a simple Python-based console application designed to manage supermarket purchases and generate a customer bill.

The system stores products and their prices using Python dictionaries. Customers can view available products, add products to a shopping cart, specify quantities, and generate a bill containing the subtotal, 12% tax, and final grand total.

This project demonstrates the practical use of **Python dictionaries, loops, conditional statements, user input, and basic calculations**.

## 🎯 Objectives

* To develop a simple supermarket billing system using Python.
* To understand the use of dictionaries for storing product information.
* To manage customer shopping cart details.
* To calculate product-wise totals.
* To calculate subtotal, tax, and grand total.
* To validate user input such as product names and quantities.
* To generate a formatted customer bill.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Data Structure:** Dictionary
* **Interface:** Command Line / Console

## ✨ Features

### 1. Customer Name

The system asks the customer to enter their name before starting the shopping process.

### 2. View Products

Displays all available supermarket products along with their prices.

Example products include:

* Rice
* Sugar
* Milk
* Bread
* Eggs
* Oil
* Soap
* Shampoo
* Biscuits
* Tea

### 3. Add Product to Cart

Customers can select a product and enter the required quantity.

The system checks whether:

* The product is available.
* The quantity contains numbers.
* The quantity is greater than zero.

If the same product is added again, its quantity is increased in the cart.

### 4. Generate Bill

The system generates a detailed bill containing:

* Customer name
* Product name
* Quantity
* Product price
* Item total
* Subtotal
* 12% tax
* Grand total

### 5. Exit

The customer can exit the application without generating a bill.

## 📚 Python Concepts Used

| Concept              | Usage                                   |
| -------------------- | --------------------------------------- |
| Dictionary           | Stores product names and prices         |
| `cart = {}`          | Stores selected products and quantities |
| `input()`            | Accepts customer and shopping details   |
| `if-elif-else`       | Handles menu operations                 |
| `while` loop         | Repeatedly displays the menu            |
| `for` loop           | Displays products and calculates bill   |
| `in` operator        | Checks product availability             |
| `isdigit()`          | Validates quantity input                |
| Dictionary `items()` | Iterates through products and cart      |
| Arithmetic operators | Calculates totals and tax               |
| `round()`            | Rounds calculated amounts               |

## 💰 Billing Calculation

The system calculates the bill using the following formulas:

```text
Item Total = Product Price × Quantity

Subtotal = Sum of all Item Totals

Tax = Subtotal × 12%

Grand Total = Subtotal + Tax
```

### Example

```text
Subtotal      : ₹500
Tax (12%)     : ₹60
Grand Total   : ₹560
```

## 🔄 Program Workflow

```text
Start
  ↓
Enter Customer Name
  ↓
Display Main Menu
  ↓
View Products
  ↓
Add Products to Cart
  ↓
Enter Quantity
  ↓
Validate Product and Quantity
  ↓
Generate Bill
  ↓
Calculate Subtotal
  ↓
Calculate 12% Tax
  ↓
Calculate Grand Total
  ↓
Display Bill
  ↓
End
```

## 🖥️ Sample Output

```text
===========================================
        WELCOME TO SMART MART
      Visakhapatnam, Andhra Pradesh
===========================================

----------- MENU -----------
1. View Products
2. Add Product to Cart
3. Generate Bill
4. Exit

Enter your choice: 2

Enter Product Name: Rice
Enter Quantity: 2

Product Added Successfully!
```

### Sample Bill

```text
==============================================================
                    SMART MART
            Visakhapatnam, Andhra Pradesh
==============================================================
Customer Name : Harshini
==============================================================
Item           Qty       Price       Total
--------------------------------------------------------------
Rice           2         60          120
Milk           2         30          60
Bread          1         40          40
--------------------------------------------------------------
Subtotal : ₹ 220
Tax (12%): ₹ 26.4
Grand Total : ₹ 246.4
==============================================================
        THANK YOU FOR SHOPPING WITH US!
            VISIT AGAIN!
==============================================================
```

## 📁 Project Structure

```text
Supermarket-Billing-System/
│
├── supermarket_billing.py
└── README.md
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Save the Code

Save the program as:

```text
supermarket_billing.py
```

### Step 3: Run the Program

Open a terminal in the project folder and execute:

```bash
python supermarket_billing.py
```

## 🧮 Product Data

The system initially contains the following products:

| Product  | Price |
| -------- | ----: |
| Rice     |   ₹60 |
| Sugar    |   ₹45 |
| Milk     |   ₹30 |
| Bread    |   ₹40 |
| Eggs     |    ₹6 |
| Oil      |  ₹150 |
| Soap     |   ₹35 |
| Shampoo  |  ₹120 |
| Biscuits |   ₹20 |
| Tea      |  ₹180 |

## 🔐 Input Validation

The program validates the quantity entered by the customer.

For example:

```text
Enter Quantity: abc
Invalid Quantity! Enter numbers only.
```

If the customer enters zero or a negative value:

```text
Quantity should be greater than 0.
```

If the entered product is not available:

```text
Product Not Available.
```

## 🚀 Future Enhancements

The project can be enhanced by adding:

* Multiple customer billing.
* Product search functionality.
* Discounts and coupons.
* Stock management.
* Different tax rates.
* Bill saving functionality.
* Date and time on the bill.
* Payment method selection.
* Printable invoices.
* Graphical user interface.

## 📌 Limitations

* Product details are stored directly in the Python program.
* The cart is available only during the current program execution.
* Bills are displayed in the console.
* No permanent data storage is used.

## 👩‍💻 Conclusion

The **Supermarket Billing System** is a beginner-friendly Python project that demonstrates how dictionaries, loops, conditions, input validation, and arithmetic operations can be combined to build a practical billing application.

The project provides a simple way to manage products, create a shopping cart, and calculate the final bill with tax.
