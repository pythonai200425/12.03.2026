# REST API Homework

## Goal

Create a small **REST API** in **FastAPI** for managing a collection of objects

The API you build must manage **books**

## Assignment Description

In this homework, you will build a REST API that supports the main CRUD operations:

* **GET** – get all books
* **GET /{id}** – get a book by id
* **POST** – create a new book
* **PUT /{id}** – replace an existing book
* **PATCH /{id}** – update part of a book
* **DELETE /{id}** – delete a book

Your API should manage a list of objects in memory using Python data structures such as a list of dictionaries

## Required Endpoints

Your API should include all of the following:

### 1. GET all

Create an endpoint that returns all records

* `/books`

### 2. GET by id

Create an endpoint that returns one record by its `id`

If the `id` does not exist, return an error with status code **404**

* `/books/{id}`

### 3. POST

Create an endpoint that adds a new record

Requirements:

* accept data from the user
* create a new unique `id`
* save the new object in the list
* return a success message and the created object

### 4. PUT

Create an endpoint that replaces the full object by `id`

Requirements:

* if the object exists, replace all its fields
* if the object does not exist, return **404**

### 5. PATCH

Create an endpoint that updates only part of an object by `id`

Requirements:

* allow updating only the fields sent by the user
* keep old values for fields that were not sent
* if the object does not exist, return **404**

### 6. DELETE

Create an endpoint that deletes an object by `id`

Requirements:

* if the object exists, remove it from the list
* return a message with the deleted object
* if the object does not exist, return **404**

Example for a book fields:

* `id`
* `title`
* `author`
* `year`
* `description` optional

You should use **Pydantic models** for validation

Your API should start with an initial list of books stored in memory using a list of dictionaries.

Example idea:

```python
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "description": "Fantasy novel"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "description": "Dystopian novel"},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "description": "Software development practices"}
]
```
You should also manage an **auto-increment id** when new books are created.

Good luck 🚀

Submit email: **[pythonai200425+rest1@gmail.com](mailto:pythonai200425+rest1@gmail.com)**
