from tools.seniority import calculate_seniority


class SearchEngine:
    def __init__(self):
        # Initialize any necessary data or connections here
        pass

    def get_search_term_options(self):
        # Simulate fetching search term options from the database
        # This is a simplified example, you may need to adapt it based on your actual implementation

        # Simulated data for demonstration
        options = [
            {"option_value": "apple", "product_page_url": "somesiteproduct1.com"},
            {"option_value": "banana", "product_page_url": "somesiteproduct2.com"},
            {"option_value": "orange", "product_page_url": "somesiteproduct3.com"},
            {"option_value": "pear", "product_page_url": "somesiteproduct4.com"},
        ]

        # Calculate total grade with priority for each option
        for option in options:
            website_id, product_id = self.get_website_product_ids(option["product_page_url"])
            parameters = self.get_ranking_parameters(website_id, product_id)
            total_grade = self.calculate_total_grade_with_priority(parameters)
            option["total_grade"] = total_grade

        # Sort options based on total grade (simplified logic)
        options.sort(key=lambda x: x["total_grade"], reverse=True)

        return {"status": "success", "data": options}

    def get_website_product_ids(self, product_page_url):
        # Implement logic to get website and product IDs based on the product page URL
        # This is a simplified example, you may need to adapt it based on your actual implementation
        website_id = 1  # Simulated website ID
        product_id = 101  # Simulated product ID
        return website_id, product_id

    def get_ranking_parameters(self, website_id, product_id):
        # Implement logic to get ranking parameters for a given website + product pair
        # This is a simplified example, you may need to adapt it based on your actual implementation
        parameters = {
            "seniority_points": 1,
            "keyword_points": 5,
            "reference_points": 15,
        }
        return parameters

    def calculate_total_grade_with_priority(self, parameters):
        # Logic to calculate total grade with priority
        seniority_grade = calculate_seniority(parameters["seniority"])  # Simulated seniority grade
        keyword_grade = len(parameters["keywords"]) * 5  # Simulated keyword grade
        reference_grade = parameters["references"] * 15  # Simulated reference grade

        # Calculate the total grade based on the specified priority
        total_grade = (
                seniority_grade
                + keyword_grade
                + reference_grade
        )

        return total_grade
