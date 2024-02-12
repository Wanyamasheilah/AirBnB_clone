# AirBnB Clone Project

## Description

The AirBnB Clone project is a part of a larger web application development. It involves building a command-line interface (CLI) for managing AirBnB objects. This project focuses on creating a foundation for the AirBnB application, including defining object classes, serialization, deserialization, and basic object storage.

## Command Interpreter

The command interpreter is a fundamental component of this project. It allows users to interact with the system and manage various AirBnB objects. The interpreter provides the following functionalities:

- Create new objects, such as User, State, City, Place, etc.
- Retrieve objects from storage (file, database, etc.).
- Perform operations on objects, such as counting, computing statistics, and more.
- Update attributes of objects.
- Delete objects from the system.

## Getting Started

To start using the AirBnB Clone command interpreter, follow these steps:

1. Clone this repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/airbnb-clone.git
   ```

2. Change into the project directory:

   ```sh
   cd airbnb-clone
   ```

3. Run the command interpreter:

   ```sh
   ./console
   ```

## How to Use

The command interpreter allows you to interact with the system using commands. Here are some common commands and how to use them:

- **Create a new object:**

  To create a new object, use the `create` command followed by the class name. For example, to create a new User object:

  ```sh
  (hbnb) create User
  ```

- **Retrieve objects:**

  To retrieve objects, use the `show` or `all` command followed by the class name and optional object ID. For example, to show a specific User object:

  ```sh
  (hbnb) show User 12345
  ```

- **Perform operations:**

  The interpreter supports various operations on objects, such as counting or computing statistics. The syntax for these operations may vary based on the specific task.

- **Update attributes:**

  To update attributes of an object, use the `update` command followed by the class name, object ID, attribute name, and new value. For example, to update a User's email:

  ```sh
  (hbnb) update User 12345 email "newemail@example.com"
  ```

- **Delete objects:**

  To delete an object, use the `destroy` command followed by the class name and object ID. For example, to delete a State object:

  ```sh
  (hbnb) destroy State 54321
  ```

## Examples

Here are some usage examples:

1. Creating a new User:

   ```sh
   (hbnb) create User
   ```

2. Retrieving a specific Place object:

   ```sh
   (hbnb) show Place 98765
   ```

3. Updating a City's name:

   ```sh
   (hbnb) update City 23456 name "New City Name"
   ```

4. Deleting a Review:

   ```sh
   (hbnb) destroy Review 34567
   ```

This is just a basic overview of the AirBnB Clone command interpreter. The project will continue to evolve and include additional features and functionalities in future phases.

Author: Pascal Obala<itsobby>


