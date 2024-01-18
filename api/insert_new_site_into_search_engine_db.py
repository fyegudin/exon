import requests


def insert_new_site_into_search_engine_db(url, seniority, keywords, references):
    # Define the API endpoint URL
    api_url = "https://your-api-base-url/insertNewSiteIntoSearchEngineDb"

    # Prepare the data to be sent in the request
    data = {
        "URL": url,
        "Seniority": seniority,
        "Keywords": keywords,
        "References": references
    }

    # Make the API request
    response = requests.post(api_url, json=data)

    # Check the response status
    if response.status_code == 200:
        print("Site inserted successfully.")
    else:
        print(f"Failed to insert site. Status code: {response.status_code}, Error: {response.text}")


# Example usage
insert_new_site_into_search_engine_db("https://example.com", 3, ["apple", "banana"], 2)

