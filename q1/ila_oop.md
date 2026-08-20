# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation means putting related data and methods together inside a class. For example, a product class can have properties like productName, price and quantity, with methods like addStock() and sellProduct(). This makes the inventory safer and more organized because the product information can be controlled through its methods.

### 2. Abstraction
Abstraction means showing only the important details and hiding the complicated parts. In the inventory system, the store owner can use a method like sellProduct() without needing to know all the steps happening inside the program, this makes the program easier to use and understand.

### 3. Inheritance
Inheritance allows one class to get  properties and methods from another class, for example, a general product class can be used as a parent class for foodProduct and drinkProduct and this helps avoid repeating the same code and makes it easier to add different types of products

### 4. Polymorphism
Polymorphism is the ability of different types of objects to respond to the same function call or interface in their own unique way, for example, both FoodProduct and DrinkProduct can have a method called displayInfo(), but each class can show its information differently. This makes the inventory system more flexible when adding new types of products.

## Reflection
I think encapsulation would be the most useful for the sari-sari store inventory system, it can keep the product name, price and quantity organized in one object, it can also prevent the data from being changed incorrectly by using methods to update the stock, because of this, I think encapsulation would make the inventory program easier to manage and understand.
