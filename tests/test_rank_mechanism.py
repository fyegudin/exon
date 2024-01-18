import requests

from tools.seniority import calculate_seniority

from api.get_search_term_options import app

# Assuming the Flask app is running on http://127.0.0.1:5000
base_url = 'http://127.0.0.1:5000'


def test_success_case_with_valid_search_term(search_term):
    # Please run the api getSearchTermOptions first from api/get_search_term_options.py
    #       app.run(debug=True)
    appearance = 0
    response = requests.get(f'{base_url}/getSearchTermOptions?search_term={search_term}')
    assert response.status_code == 200, "No response from api getSearchTermOptions"
    try:
        resp = response.json()
        assert resp["status"] == "success", "Status response not success"
        for data in resp["data"]:
            if search_term in data["option_value"]:
                appearance = 1
        assert appearance == 1, f"value {search_term} not in response"
    except requests.exceptions.JSONDecodeError:
        print(f'Failed to parse JSON. Response content: {response.text}')


def test_success_case_with_invalid_search_term(invalid_search_term):
    # Please run the api getSearchTermOptions first from api/get_search_term_options.py
    #       app.run(debug=True)
    appearance = 0
    response = requests.get(f'{base_url}/getSearchTermOptions?search_term={invalid_search_term}')
    assert response.status_code == 200, "No response from api getSearchTermOptions"
    try:
        resp = response.json()
        assert resp["status"] == "success", "Status response not success"
        assert resp["msg"] == "No Data Found", f"Not expected message {resp['msg']} "
        for data in resp["data"]:
            if invalid_search_term in data["option_value"]:
                appearance = 1
        assert appearance == 0, f"value {invalid_search_term} in response"
    except requests.exceptions.JSONDecodeError:
        print(f'Failed to parse JSON. Response content: {response.text}')


def test_error_case(search_term):
    # Please run the api getSearchTermOptions first from api/get_search_term_options.py
    #       app.run(debug=True)
    response = requests.get(f'{base_url}/getSearchTermOptionsWithError')
    assert response.status_code == 404, f"Get unexpected response {response.status_code}"
    try:
        response.json()
    except requests.exceptions.JSONDecodeError:
        print(f'Failed to parse JSON. Response content: {response.text}')


def test_ranking_with_priority(database, search_engine, search_term, data_test):
    # Please run the api getSearchTermOptions first from api/get_search_term_options.py
    #       app.run(debug=True)
    appearance = 0
    response = requests.get(f'{base_url}/getSearchTermOptions?search_term={search_term}')
    assert response.status_code == 200, "No response from api getSearchTermOptions"
    try:
        resp = response.json()
        assert resp["status"] == "success", "Status response not success"
        for data in resp["data"]:
            if search_term in data["option_value"]:
                appearance = 1
        assert appearance == 1, f"value {search_term} not in response"
    except requests.exceptions.JSONDecodeError:
        print(f'Failed to parse JSON. Response content: {response.text}')
    for data in data_test:
        # Assuming you have a function to insert test data into the database
        database.insert_test_data_into_db(data)

        # Call the function to calculate total grade with priority
        total_grade = search_engine.calculate_total_grade_with_priority(data)

        # Add assertions to check if the total grade is calculated correctly
        expected_result = calculate_seniority(data["seniority"]) + len(data["keywords"]) * 5 + data["references"] * 15
        assert total_grade == expected_result
