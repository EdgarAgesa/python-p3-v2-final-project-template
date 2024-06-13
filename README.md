# Study Group Management System

This is a command-line interface (CLI) application for managing study groups, subjects, and study sessions.

By **Edgar Agesa** 


## Description

The Study Group Management System is a simple and efficient tool for managing study groups, subjects, and study sessions. The application uses a SQLite database to store and retrieve data, making it easy to use and maintain.

The application provides the following features:

- Create, read, update, and delete (CRUD) operations for study groups, subjects, and study sessions.
- Assign subjects to study groups.
- Schedule study sessions for specific dates and times.
- List all study groups and their associated subjects and study sessions.

## Installation

To install the Study Group Management System, follow these steps:

1. Fork and Clone the repository:
   ```
   git clone git@github.com:EdgarAgesa/python-p3-v2-final-project-template.git
   ```

2. Navigate to the project directory:
   ```
   cd python-p3-v2-final-project-template
   ```

3. Install the required dependencies:
   ```
   pipenv install
   pipenv shell
   ```

## Usage

To run the application, execute the following command:

```
python3 lib/cli.py
```

The application will display a menu with options to perform various operations on study groups, subjects, and study sessions.

## Features

- Create, read, update, and delete (CRUD) operations for study groups, subjects, and study sessions.
- Assign subjects to study groups.
- Schedule study sessions for specific dates and times.
- List all study groups and their associated subjects and study sessions.

## Database Schema

The database schema consists of three tables: study_groups, subjects, and study_sessions.

- study_groups table:
  - id (integer, primary key)
  - name (text)

- subjects table:
  - id (integer, primary key)
  - name (text)
  - study_group_id (integer, foreign key referencing study_groups(id))

- study_sessions table:
  - id (integer, primary key)
  - date (text)
  - time (text)
  - study_group_id (integer, foreign key referencing study_groups(id))

## Technologies Used

- Python 3.8.13
- SQLite database
- Pipenv for managing project dependencies

## Support and Contact Details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at <edgarasige@gmail.com>

## License

MIT License

Copyright (c) 2024 Edgar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.