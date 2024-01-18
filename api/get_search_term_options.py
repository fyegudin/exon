from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data for demonstration
data = [
    {"option_value": "apple", "product_page_url": "somesiteproduct1.com"},
    {"option_value": "banana", "product_page_url": "somesiteproduct2.com"},
    {"option_value": "orange", "product_page_url": "somesiteproduct3.com"},
    {"option_value": "pear", "product_page_url": "somesiteproduct4.com"},
]


@app.route('/getSearchTermOptions', methods=['GET'])
def get_search_term_options():
    search_term = request.args.get('search_term')

    # Implement logic based on the ranking mechanism
    # This is a simplified example, you may need to adapt it based on your actual implementation

    # Filter options based on the search term
    filtered_options = [option for option in data if search_term in option['option_value']]

    # Sort options based on total grade (simplified logic)
    filtered_options.sort(key=lambda x: x["product_page_url"])

    # Prepare response
    if filtered_options:
        response = {"status": "success", "data": filtered_options}
    else:
        response = {"status": "success", "data": [], "msg": "No Data Found"}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
