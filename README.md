# QA Automation Test Suite

A professional API test suite built with Python and pytest,
demonstrating real-world QA automation practices.

## What's covered

- Complete CRUD testing — GET, POST, PUT, DELETE
- Shared fixtures via conftest.py — zero repeated setup code
- Environment variables via .env — no hardcoded secrets
- Parametrized tests — multiple inputs, one clean function
- Session-based requests — shared headers across all tests
- Custom failure messages on every assertion

## Project Structure

- conftest.py — shared fixtures (base_url, api_session)
- test_users.py — user endpoint tests
- test_param.py : test general endpoints with parameters
- test_posts.py — post endpoint tests with parametrize
- test_comments.py — comment endpoint tests with parametrize
- .env — environment variables (not pushed to GitHub)
- .gitignore — excluded files

## How to run

1. Clone the repo
2. Create and activate virtual environment
3. Install dependencies: pip install pytest requests python-dotenv
4. Add .env file with BASE_URL=https://jsonplaceholder.typicode.com
5. Run: pytest -v

## Tools and Technologies

- Python
- pytest
- requests
- python-dotenv
- Git and GitHub

## Author

Iqrar | Aspiring QA Automation Engineer
GitHub: https://github.com/IQRAR2941