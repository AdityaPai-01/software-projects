# User Management System 👤

A simple Python-based user management system built as a learning project.

The project handles user data, registration, authentication, login, and application logging using Python's built-in `logging` module.

## Features ✨

* User registration
* User login and authentication
* JSON-based data storage
* Basic CLI interface
* Application logging using Python's `logging` module
* Separate handling of user data, application logic, and UI

## User Manual 📖

The program uses simple commands to navigate the interface.

| Command | Action                     |
| ------- | -------------------------- |
| `!L`    | Login                      |
| `!R`    | Register a new user        |
| `!Q`    | Exit the current interface |

## Logging 📝

The project uses Python's built-in `logging` module to keep track of important events while the program is running.

The logs include things such as:

* Successful operations
* Login attempts
* Failed operations
* Warnings
* Errors

The log file is stored in:

```text
data/logdata.txt
```

Example:

```text
2026-09-25 10:46:58,872 | INFO | manager.user_manager | Login successful: username 'example'
```

## Running the Program 🚀

Make sure Python is installed, then run:

```bash
python main.py
```

The program will initialize the required data and start the command-line interface.

## AI Usage 🤖

AI was used during the development of this project as a learning and debugging aid.

It was mainly used to:

* Understand concepts and Python features
* Discuss possible approaches to problems
* Improve code readability and structure
* Debug issues and understand errors
* Learn how to use Python's `logging` module and integrate it into the project

The actual project structure, implementation, and final code were developed and adapted by the author.

## Notes 📌

This project was created primarily as a learning project to practice Python programming, object-oriented programming, file handling, authentication logic, logging, and Git.