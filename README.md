# Beautify-Her-Django
A salon booking appointment django based project that allows users showcase their services and allow other users reach out to them for their services.

# Features
- Registration and logging in users.
- Services upload by service providers.
- Booking of appointments by customers.
- Products page( viewing, updating, creating and deleting)
- Allow adding of products to cart.

# Usage
To run the project:
1. Clone the repository
2. Create a virtual environment. If you already have an existing virtual environment you can skip the creation step. Navigate to where the virtual environment is and activate the environment.
   ```bash
      $ python -m venv name_of_environment
      $ name_of_environment\Scripts\activate
   ```
3. Install requirements. 
   ```bash
      $ pip install -r requirements.txt
   ```
4. Apply migration.
   ```bash
      $ python manage.py migrate
   ```
5. Run the application by starting the server
   ```bash
      $ python manage.py runserver
   ```
