# Session Authentication API

## Description
This project implements a session authentication system using Flask. It provides an API for user authentication, allowing users to log in and log out using sessions.

## Author
Edwin Kambale

## Project Structure
alx-backend-user-data/0x02-Session_authentication ├── api # API module containing views and authentication logic ├── main_0.py # Main script for creating a user and handling basic authentication ├── main_1.py #  ├── main_2.py #  ├── main_3.py # ├── main_4.py # ├── models # Contains model definitions └── README.md # Project documentation


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bwambale03/alx-backend-user-data.git
   cd alx-backend-user-data/0x02-Session_authentication

## Set up a virtual environment
python3 -m venv env
source env/bin/activate

# Usage
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app

## Endpoints
POST /api/v1/auth_session/login: Logs in a user.
DELETE /api/v1/auth_session/logout: Logs out a user.

# License
This project is licensed under the MIT License.

