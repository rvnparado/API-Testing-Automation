import requests
import json
from time import sleep

# API Base URL
BASE_URL = "http://localhost:3000/api"


def test_create_user():
    print("\n=== Testing User Creation ===")
    # Test data
    user_data = {
        "username": "testuser1",
        "email": "testuser1@example.com",
        "age": 25,
        "role": "user"
    }

    # Make POST request
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Basic assertions
    assert response.status_code == 201, "Expected status code 201"
    assert response.json()[
        "username"] == user_data["username"], "Username doesn't match"
    return response.json()["id"]


def test_get_user(user_id):
    print("\n=== Testing Get User ===")
    # Make GET request
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Basic assertions
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()["id"] == user_id, "User ID doesn't match"


def test_update_user(user_id):
    print("\n=== Testing User Update ===")
    # Test data
    updated_data = {
        "username": "testuser1_updated",
        "email": "testuser1_updated@example.com",
        "age": 26,
        "role": "admin"
    }

    # Make PUT request
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Basic assertions
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()[
        "username"] == updated_data["username"], "Username wasn't updated"


def test_get_all_users():
    print("\n=== Testing Get All Users ===")
    # Make GET request
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Basic assertions
    assert response.status_code == 200, "Expected status code 200"
    assert isinstance(response.json(), list), "Expected a list of users"


def test_delete_user(user_id):
    print("\n=== Testing User Deletion ===")
    # Make DELETE request
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # Basic assertions
    assert response.status_code == 200, "Expected status code 200"

    # Verify user is deleted
    get_response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert get_response.status_code == 404, "User should not exist after deletion"


def test_error_cases():
    print("\n=== Testing Error Cases ===")

    # Test 1: Create user with missing required fields
    print("\nTest: Create user with missing email")
    response = requests.post(
        f"{BASE_URL}/users", json={"username": "incomplete"})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400, "Expected status code 400"

    # Test 2: Get non-existent user
    print("\nTest: Get non-existent user")
    response = requests.get(f"{BASE_URL}/users/9999")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 404, "Expected status code 404"


def run_all_tests():
    try:
        # Create a user and get their ID
        user_id = test_create_user()

        # Wait a bit between requests
        sleep(1)

        # Run other tests
        test_get_user(user_id)
        test_update_user(user_id)
        test_get_all_users()
        test_delete_user(user_id)
        test_error_cases()

        print("\n✅ All tests passed successfully!")

    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")


if __name__ == "__main__":
    # Make sure the server is running before starting tests
    try:
        requests.get(f"{BASE_URL}/users")
        run_all_tests()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to the server. Make sure it's running on http://localhost:3000")
