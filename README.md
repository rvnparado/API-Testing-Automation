# API Testing Automation

This repository contains a simple yet powerful API testing framework built with Python, demonstrating automated testing of a RESTful User API without relying on complex testing frameworks.

## Project Structure
```
API-Testing-Automation/
├── api_test.py         # Main test script
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Features

- Complete CRUD operations testing (Create, Read, Update, Delete)
- Error case handling
- Status code verification
- Response body validation
- No external testing framework dependencies
- Clear and readable test output

## Prerequisites

- Python 3.x
- pip (Python package installer)
- A running instance of the User API server (provided in separate repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rvnparado/API-Testing-Automation.git
cd API-Testing-Automation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tests

1. Make sure your API server is running on http://localhost:3000
2. Run the tests:
```bash
python api_test.py
```

## Test Cases

The automation suite includes the following test cases:

1. User Creation
   - Creates a new user with valid data
   - Verifies response status code and user data

2. User Retrieval
   - Gets user by ID
   - Gets all users
   - Verifies response format and content

3. User Update
   - Updates existing user information
   - Verifies changes are applied correctly

4. User Deletion
   - Deletes a user
   - Verifies user no longer exists

5. Error Cases
   - Tests missing required fields
   - Tests non-existent user scenarios

## Sample Output

```
=== Testing User Creation ===
Status Code: 201
Response: {
  "id": 1,
  "username": "testuser1",
  "email": "testuser1@example.com",
  "age": 25,
  "role": "user"
}

... [more test outputs] ...

✅ All tests passed successfully!
```

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for any bugs found or feature requests.

## License

This project is open source and available under the MIT License.

## Author

Raven Parado 