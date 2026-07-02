# Inventory Management System

## Project Objective

The objective of this project is to develop a menu-driven Inventory Management System using Python. The system will help users manage product information, maintain stock records, and perform basic inventory operations efficiently. The project will be developed using Object-Oriented Programming (OOP), file handling, and exception handling concepts.

---

## Features

The Inventory Management System will support the following operations:

- Add Product
- View All Products
- Update Product Details
- Delete Product
- Search Product
- Sell Product
- Update Stock Quantity
- Save Products to JSON File
- Load Products from JSON File
- Input Validation and Exception Handling

---

## Product Data Structure

Each product will contain the following information:

| Field        | Data Type |
| ------------ | --------- |
| Product ID   | Integer   |
| Product Name | String    |
| Category     | String    |
| Price        | Float     |
| Quantity     | Integer   |

---

## Classes

### Product

Represents a single product in the inventory.

**Attributes**

- Product ID
- Product Name
- Category
- Price
- Quantity

---

### InventoryManagementSystem

Manages all inventory operations.

**Methods**

- Add Product
- View Products
- Update Product
- Delete Product
- Search Product
- Sell Product
- Save Products
- Load Products

---

## Data Structure Design

```text
InventoryManagementSystem
        │
        ▼
   Product List
        │
        ▼
     Product Object
```

Each Product object stores:

- Product ID
- Product Name
- Category
- Price
- Quantity

---

## Program Flow

```text
Start
   │
   ▼
Load Products from JSON
   │
   ▼
Display Main Menu
   │
   ├── Add Product
   ├── View Products
   ├── Update Product
   ├── Delete Product
   ├── Search Product
   ├── Sell Product
   └── Exit
           │
           ▼
Save Products
           │
           ▼
End Program
```

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON File Handling
- Exception Handling

---

## Author

Vivek Bhushan
AI/ML Intern
