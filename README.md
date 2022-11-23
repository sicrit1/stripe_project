# stripe_project
This project demonstrates work of Django and Stripe API

For install the project:

1. If poetry doesn't installed: curl -sSL https://install.python-poetry.org | python3 -
2. Create an account on https://dashboard.stripe.com/register.
3. Clone repository stripe_project local
4. Run command: poetry install
5. Create .env in stripe_project directory. Add STRIPE_PUBLIC_KEY and STRIPE_PRIVATE_KEY in .env like as in env.example
6. Run server: poetry run python manage.py runserver
