from faker import Faker
import random


class GenerateData:
    def __init__(self):
        self.fake = Faker()

    def generate_fake_product_data(self):
        product_name = self.fake.word()  # Generates a random word for product name
        url = self.fake.url()  # Generates a random url
        references = random.randint(1, 10)  # Generates a random integer between 1 and 10 for references
        date_created = self.fake.date_this_decade()  # Generates a random date in the current decade

        return {
            "product_name": product_name,
            "url": url,
            "references": references,
            "date_created": date_created
        }


# Example usage
data_generator = GenerateData()

for _ in range(5):
    product_data = data_generator.generate_fake_product_data()
    print(product_data)
