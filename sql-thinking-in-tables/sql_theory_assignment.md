# SQL Theory Assignment

---

## 1. Why databases are important in real-world AI systems

Databases are very important in real-world AI systems because they help store, manage, and retrieve large amounts of data efficiently. AI systems rely heavily on data to learn patterns, make predictions, and improve performance. Without databases, managing this data would be difficult and unorganized.

In many applications such as recommendation systems, chatbots, and e-commerce platforms, AI models need structured data to work properly. Databases provide a reliable way to store and access this information.

### Examples of data stored in databases
- User information (name, email, preferences)
- Transaction data (orders and payments)
- Product information
- Activity logs and interactions

### Why structured storage is necessary
Structured storage helps organize data in a clear format so that it can be easily searched, updated, and analyzed. This improves efficiency, reduces errors, and allows AI systems to process data faster.

---

## 2. Relational database mental model

A relational database organizes data into **tables**, which makes it easy to manage and connect related information.

### Tables
A table represents a specific type of entity. For example, a table may represent users, products, or orders.

Example tables:
- Users
- Orders
- Products

### Rows
Rows represent individual records in a table. Each row contains information about a single entity.

Example:  
In a Users table, one row represents one user.

### Columns
Columns represent the attributes or properties of the entity.

Example in a Users table:
- user_id
- name
- email

Each table should represent only **one entity** to keep the database organized and avoid unnecessary duplication of data.

---

## 3. Primary Key

A **primary key** is a column in a table that uniquely identifies each record in that table.

Example:

| user_id | name  | email            |
|---------|-------|------------------|
| 1       | Ali   | ali@email.com    |
| 2       | Ahmed | ahmed@email.com  |

In this example, **user_id** is the primary key.

### Properties of a primary key
- It must be **unique** for every row.
- It **cannot be NULL**.
- It helps identify records clearly.

### Importance of primary keys
Primary keys help maintain data integrity and ensure that each record can be uniquely identified within the table.

---

## 4. What is a database schema

A **database schema** is the structure or blueprint of a database. It defines how data is organized and how different tables relate to each other.

A schema includes:
- Tables in the database
- Columns in each table
- Data types of columns
- Relationships between tables

Example schema:

Users Table
- user_id (integer)
- name (text)
- email (text)

Orders Table
- order_id (integer)
- user_id (integer)
- product_name (text)

### Importance of schema
Schemas help maintain a consistent and organized structure in the database. They also make it easier for developers to understand how data is stored and connected.

---

## 5. Relationships between tables

Relational databases allow tables to be connected through relationships.

For example, in an e-commerce system:
- A **Users** table stores user information.
- An **Orders** table stores purchase details.

Each user can have multiple orders.

### Foreign Key

A **foreign key** is a column in one table that refers to the primary key in another table.

Example:

Orders Table

| order_id | user_id | product |
|----------|---------|---------|
| 101      | 1       | Laptop  |
| 102      | 2       | Phone   |

Here, **user_id** in the Orders table is a foreign key that refers to the **user_id** in the Users table.

### Why relationships are important
- They connect related data between tables.
- They reduce data duplication.
- They allow complex queries and efficient data retrieval.

---

## Conclusion

Relational databases play a crucial role in managing structured data for AI systems. Concepts like tables, rows, columns, primary keys, schemas, and relationships help organize data efficiently and maintain data consistency. These structures make it easier for AI systems and applications to store, access, and analyze large amounts of information.