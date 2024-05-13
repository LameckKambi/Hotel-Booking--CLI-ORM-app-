# Hotel Booking System

The Hotel Booking System is a command-line interface (CLI) application.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)

## Introduction

 The app is built with Python and SQLAlchemy. It allows users to create and manage hotels, create bookings for available hotels, and perform various operations through a user-friendly CLI menu.


## Installation

To get started with this project, follow these steps, but before, make sure you've installed VScode & Python 3 and are running a `zsh` or `bash` terminal and then you can run the following commands in your terminal:

1. Clone the repository:

```bash
git clone https://github.com/your-username/Hotel-Booking--CLI-ORM-app
```

2. Navigate to the project directory:

```
cd your-repo
```
3. Create a virtual environment (optional but recommended):

```bash
python -m venv env
```
4. Activate the virtual environment: On Unix or macOS:
```bash
source env/bin/activate
```
5. Install the required dependencies:
```bash
pip install sqlalchemy
```

# Usage
- Once you have cloned the repository and navigated to the project directory, you can run the code by executing the cli.py file by simply pasting the command below on the terminal in VS code and pressing Enter:

```
python cli.py
```



# File Structure
The project is organized into the following files:
```
hotel-booking-system/
├── models.py
├── cli.py
├── db.py
├── hotel.db
└── README.md
```

- **models.py**: Contains the SQLAlchemy model definitions for Hotel and Booking classes, as well as the ORM methods.
- **cli.py**: Implements the Command Line Interface logic and user interaction.
- **db.py**: Handles the database setup and session management.
- **hotel.db**: The SQLite database file (created automatically).
- **README.md**: This file, providing documentation for the project.


# Contributing
- Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.


## Authors

- [`Lameck Kambi`](https://github.com/LameckKambi)


**Additional Notes**

- Feel free to customize the application.

- Explore the codebase and experiment with adding new features or functionalities.

### License
This project is licensed under the [MIT License](#License).
```
This project is licensed under the [MIT License](#license).
Copyright 2024 Lameck Kambi.
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```


### Acknowledgments

I would like to express my gratitude to the following individuals and organizations for their contributions, support, and resources that have been invaluable in the development of the project.

- **Technical Mentor:** As a team we would like to acknowledge and appreciate our  technical mentor [`Mr Ian okumu`](https://github.com/otsembo) for his invaluable guidance throughout the project

- **Moringa School:** I appreciate [`Moringa school`](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiK9-Tw_aKEAxU2QUECHcwOCDoYABAAGgJ3cw&ase=2&gclid=EAIaIQobChMIivfk8P2ihAMVNkFBAh3MDgg6EAAYASAAEgJSB_D_BwE&ohost=www.google.com&cid=CAASJORoHa2LLpPz846DBxVhhEyz_mIvcNnHZ_R4tWoL3IuSCcmYsA&sig=AOD64_04tJFd3Gstl7m-sNfbwiempwyFwg&q&nis=4&adurl&ved=2ahUKEwifmODw_aKEAxUhRKQEHaoDBq0Q0Qx6BAgFEAE) and its staff for guiding me and  providing me with the necessary resources to undertake this project.