# Assuming you have a database module and API module


class Database:
    def __init__(self):
        # Simulated tables
        self.websites = []
        self.products = []
        self.websites_products = []
        self.search_engine_ranking = []
        self.ranking_parameters = []

    def insert_website(self, website):
        self.websites.append(website)

    def insert_product(self, product):
        self.products.append(product)

    def insert_website_product_relation(self, relation):
        self.websites_products.append(relation)

    def insert_ranking_parameter(self, parameter):
        self.ranking_parameters.append(parameter)

    def insert_search_engine_ranking(self, ranking):
        self.search_engine_ranking.append(ranking)

    def insert_test_data_into_db(self, test_data):
        # for data in test_data:
        # Insert data based on the structure of your JSON
        seniority = test_data.get("seniority")
        keywords = test_data.get("keywords", [])
        references = test_data.get("references")


    def calculate_total_grade(self, website_id, product_id):
        # Simulated calculation based on ranking parameters
        pass


