# Trading Application

This is a Django-based trading application that interacts with the Binance API. The application allows users to log in, fetch current prices of currencies, place orders, check live order status, and cancel orders.

## Features

- User authentication (login and registration)
- Fetch current prices of cryptocurrencies
- Place buy/sell orders
- Check the status of live orders
- Cancel existing orders

## Project Structure

```
trading_app/
├── binance_env/                # Virtual environment (not included in project files)
├── trading_app/
│   ├── manage.py               # Command-line utility for interacting with the Django project
│   ├── trading_app/
│   │   ├── __init__.py         # Indicates that the directory should be treated as a Python package
│   │   ├── settings.py         # Configuration settings for the Django project
│   │   ├── urls.py             # URL routing for the Django application
│   │   ├── wsgi.py             # Entry point for WSGI-compatible web servers
│   │   └── asgi.py             # Entry point for ASGI-compatible web servers
│   ├── accounts/
│   │   ├── __init__.py         # Indicates that the directory should be treated as a Python package
│   │   ├── models.py           # User model and related models
│   │   ├── views.py            # Views for user authentication
│   │   ├── urls.py             # URL routing for the accounts app
│   │   └── forms.py            # Forms for user authentication
│   ├── trading/
│   │   ├── __init__.py         # Indicates that the directory should be treated as a Python package
│   │   ├── models.py           # Models related to trading
│   │   ├── views.py            # Views for trading functionalities
│   │   ├── urls.py             # URL routing for the trading app
│   │   └── binance_api.py      # Functions for interacting with the Binance API
│   └── templates/
│       ├── accounts/
│       │   └── login.html      # HTML template for the user login page
│       └── trading/
│           ├── dashboard.html   # HTML template for the trading dashboard
│           ├── order_status.html # HTML template for displaying order status
│           └── place_order.html  # HTML template for placing a new order
├── requirements.txt             # Lists dependencies required for the project
└── README.md                    # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd trading_app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv binance_env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     binance_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source binance_env/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the migrations:**
   ```
   python manage.py migrate
   ```

6. **Start the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/accounts/login/` to log in.
- Use the trading dashboard to view current prices and manage orders.

## License

This project is licensed under the MIT License.