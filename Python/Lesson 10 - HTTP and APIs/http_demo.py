# ----------------------------- Hands-On HTTP and APIs -----------------------------
# ----------------------------- Exercise 1: Using the requests library -----------------------------
# Use this base URL for the exercises: - `https://jsonplaceholder.typicode.com`

# import requests
# BASE_URL = "https://jsonplaceholder.typicode.com"

# GET_URL = f"{BASE_URL}/posts/1"

# response = requests.get(GET_URL)

# print(response.status_code)
# print(response.reason)

# # ------------------------------ Exercise 2: Read Response Metadata ------------------------------
# # Request `/posts/1` and print:

# # - `Content-Type` response header
# # - Total response time in milliseconds (`response.elapsed`)

# # ✅ *Check*: Output shows a `Content-Type` containing `application/json` and a numeric time value.

# print(response.headers['Content-Type'])

# print(response.elapsed.total_seconds() * 1000)  # Convert to milliseconds

# # ------------------------------ Exercise 3: Parse JSON Safely ------------------------------
# # **Goal**: Request `/posts/1`, parse JSON, and print:

# # - `userId`
# # - `id`
# # - `title`

# # Also add a `try/except` block that handles JSON parse errors gracefully.

# try:
#     data = response.json()
#     print(f"userId: {data['userId']}")
#     print(f"id: {data['id']}")
#     print(f"title: {data['title']}")

# except requests.RequestException as e:
#     print(f"Error parsing JSON: {e}")

# # ✅ *Check*: The three fields print correctly, and your code does not crash if JSON parsing fails.

# # ---------------------------- Exercise 4: Send Query Parameters ----------------------------
# # **Goal**: Request `/comments` with query params (`postId=1`) using `params={...}` and print:

# # - Number of comments returned
# # - Email from the first comment

# # ✅ *Check*: Program reports a non-zero comment count and prints a valid email string.

# params = {'postId': 1}
# response = requests.get(f"{BASE_URL}/comments", params=params)

# print(f"Number of comments returned: {len(response.json())}")

# print(f"Email from the first comment: {response.json()[0]['email']}")

# #------------------------------- Stretch (Optional) ---------------------------------------------------------
# # ### Handle HTTP and Network Errors

# # **Goal**: Build a small helper function `fetch(url)` that:

# # - Uses `timeout=3`
# # - Calls `response.raise_for_status()`
# # - Catches and prints friendly messages for:
# #   - `requests.exceptions.Timeout`
# #   - `requests.exceptions.HTTPError`
# #   - `requests.exceptions.RequestException`

# # Test with:

# # - A valid endpoint: `/posts/1`
# # - An invalid endpoint: `/not-a-real-route`

# # ✅ *Check*: Valid request succeeds; invalid request prints a clear error without crashing.

# def fetch(url):
#     try:
#         response = requests.get(url, timeout=3)
#         response.raise_for_status()
#         return response.json()

#     except requests.exceptions.Timeout:
#         print("Request timed out. Please try again later.")
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#     except requests.exceptions.RequestException as req_err:
#         print(f"An error occurred: {req_err}")

# ------------------------- HANDS-ON 2 ---------------------------------------------------------------------
# ---------------------------- Authentication with Python `requests` ---------------------------------------
# This exercise set focuses on common authentication patterns used with HTTP APIs.

# For these exercises, use:

# - `https://httpbin.org`

# Security note:

# - Do not hardcode real credentials or tokens in source code.
# - Prefer environment variables for secrets.

# ------------------------ Exercise 1: Basic Authentication ------------------------
# **Goal**: Use HTTP Basic Auth to call:

# - `/basic-auth/student/pass123`

# Use username `student` and password `pass123` in your request.

# ✅ *Check*: Successful call returns status code `200` and JSON showing authentication success.

from urllib import response

import requests


# auth_url = "https://httpbin.org/basic-auth/student/pass123"

# response = requests.get(auth_url, auth=('student', 'pass123'))

# print(response.status_code)
# print(response.json())

# # ------------------------ Exercise 2: Bearer Token Header   ------------------------
# # **Goal**: Send a request to `/bearer` with an `Authorization` header in this format:

# # - `Authorization: Bearer <token>`

# # Use a placeholder token value such as `abc123`.

# # ✅ *Check*: Response indicates bearer authentication succeeded.

# url = "https://httpbin.org/bearer"

# token = "abc123"

# headers = {"Authorization": f"Bearer {token}"}

# response = requests.get(url, headers=headers)

# print(response.status_code)

# print(response.json())

# # -------------------------------- Exercise 3: API Key in Header and Query String --------------------------------

# # **Goal**: Send two requests to `/get`:

# # - One with header: `X-API-Key: demo-key-001`
# # - One with query param: `?api_key=demo-key-001`

# # Print the echoed value from the response JSON each time.

# # ✅ *Check*: You can see the API key echoed once under headers and once under args.

# get_url = "https://httpbin.org/get"

# api_key = "demo-key-001"

# # Request with header
# headers = {"X-API-Key": api_key}

# response1 = requests.get(get_url, headers=headers)

# print("Response with header:")

# print(response1.json())

# # Request with query parameter

# params = {"api_key": api_key}

# response2 = requests.get(get_url, params=params)

# print("Response with query parameter:")
# print(response2.json())

# ---------------------------------- Exercise 4: Session Cookies -------------------------------------------
# **Goal**: Use `requests.Session()` to:

# 1. Set a cookie with `/cookies/set/course_token/python-lesson-10`
# 2. Fetch `/cookies` with the same session
# 3. Print the stored cookies from the response

# ✅ *Check*: The `course_token` cookie appears in the final `/cookies` response.

session = requests.Session()

cookie_url = "https://httpbin.org/cookies/set/course_token/python-lesson-10"
def set_cookie():

    session.get(cookie_url)
    
set_cookie()

fetch_cookies_url = "https://httpbin.org/cookies"

response = session.get(fetch_cookies_url)

print(response.json())
